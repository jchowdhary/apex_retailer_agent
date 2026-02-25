# from google.adk.agents.llm_agent import Agent

# root_agent = Agent(
#     model='gemini-2.5-flash',
#     name='root_agent',
#     description='A helpful assistant for user questions.',
#     instruction='Answer user questions to the best of your knowledge',
# )

import pandas as pd
from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent
import os

# Tool A: Scan Gold CSV for high-level anomalies 
def tool_a_scan_gold():
    df = pd.read_csv('retailcoachagent/gold_daily_performance.csv')
    # Find stores with returns > 10% of items sold
    anomalies = df[df['is_returned'] > (df['quantity'] * 0.10)]
    return anomalies.tail(5).to_string()

# Tool B: Drill down into transaction details 
def tool_b_drill_down(location_id, date):
    df = pd.read_csv('retailcoachagent/fact_enriched.csv')
    details = df[(df['location_id'] == location_id) & (df['date'] == date)]
    return details[['product_name', 'return_reason', 'discount_amount', 'gross_sales_amt']].to_string()

# Tool C: Ingest SOP text into context window
def tool_c_load_sop(sop_id):
    try:
        with open(f"retailcoachagent/{sop_id}.txt", 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "SOP not found."

# Tool D: Audit Anomalies 
def tool_audit_anomalies():
    """
    Scans the enriched sales data to identify SOP violations.
    Returns a string summary of findings for the agent to analyze.
    """
    # 1. Load the data the tool needs
    df = pd.read_csv('retailcoachagent/gold_daily_performance.csv')
    
    # 2. Run the logic
    # Identify unauthorized discounts (>15%)
    anomalies = df[df['discount_percentage'] > 15]
    
    # Identify phantom inventory (sales = 0 but quantity > 0)
    phantom_stock = df[(df['gross_sales_amt'] == 0) & (df['quantity'] > 0)]
    
    # 3. Format the result for the agent to read
    report = f"--- Anomaly Audit Report ---\n"
    report += f"Unauthorized Discounts Found: {len(anomalies)}\n"
    report += f"Phantom Inventory Records Found: {len(phantom_stock)}\n"
    
    if len(anomalies) > 0:
        report += f"\nSample of Discounts: \n{anomalies[['location_id', 'discount_percentage']].head().to_string()}"
        
    return report

# Save Insight Utility 
def save_insights(insight_text):
    output_file = 'retailcoachagent/validated_insights.csv'
    new_row = pd.DataFrame([{"timestamp": pd.Timestamp.now(), "insight": insight_text, "status": "Validated"}])
    new_row.to_csv(output_file, mode='a', header=not os.path.exists(output_file), index=False)
    return f"Insight saved to {output_file}"

# Define the RetailCoach LLMAgent
retailer_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='retailer_agent',
    description='Analyzes sales anomalies and grounds solutions in company SOPs.',
    instruction="""
    You are the Apex Beauty RetailCoach Agent. 
    1. Use tool_a_scan_gold to find an anomaly and using all csv to find the context of the anomaly.
    2. Use tool_b_drill_down to find the specific 'Why'.
    3. Read below the sop_id and their context to find the relevant SOP. Use tool_c_load_sop to pass the correct filename read the SOP and find the 'Immediate Action'.
        SOP ID:"SOP-QA-001"
        When: Product Adverse Reaction Protocol. Action: If 2+ incidents in 48h, mark SKU 'Do Not Sell' and submit Level 1 Quality Alert.

        SOP ID:"SOP-FIN-003"
        When: Pricing and Discount Policy.

        SOP ID:"SOP-LOG-002"
        When:E-commerce Fulfillment Standards like for late returns during Peak, waive shipping fees and offer 10% courtesy coupon.

        SOP ID:"SOP-OPS-004"
        When:Inventory OSA Protocol like if Top 20 SKU is empty, perform backroom check and adjust system inventory to ZERO.
   
    4. Provide a grounded insight citing the sop_id and Section.
    5. Save your final insight using save_insights.
    """,
    tools=[tool_a_scan_gold, tool_b_drill_down, tool_c_load_sop, tool_audit_anomalies, save_insights],
    output_key="retailer_agent_response"
)

# 2. Judge Agent: Reads {retailer_agent_response} and provides an audit report
judge_agent = LlmAgent(
    model='gemini-2.5-flash',
    name="JudgeAgent",
    instruction="""
    You are an auditor. Review the following RetailCoach output: {retailer_agent_response}.
    1. Verify if the agent cited a valid SOP.
    2. Check if the anomaly detection matches the data logic.
    3. Provide a score (1-5) and specific feedback if the agent missed anything.
    """,
    output_key="audit_report" # Saves the judge's feedback to state
)

# --- 2. Create the SequentialAgent ---
# This agent orchestrates the pipeline by running the sub_agents in order.
retailcoach_pipeline_agent = SequentialAgent(
    name="retailcoach_pipeline_agent",
    sub_agents=[retailer_agent, judge_agent],
    description="Orchestrates the RetailCoach analysis and subsequent audit by the JudgeAgent.",
)

root_agent = retailcoach_pipeline_agent
