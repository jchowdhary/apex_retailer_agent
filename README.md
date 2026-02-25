# Retail Coach Agent - ADK Implementation

An intelligent AI agent designed to help retail operations teams identify anomalies, audit compliance violations, and make data-driven operational decisions. This is the ADK (Agent Development Kit) implementation of the Retail Coach Agent.

## 🎯 Project Goal

The Retail Coach Agent leverages advanced LLM capabilities to:
- **Scan operational data** for high-level anomalies in retail performance metrics
- **Drill down into transaction details** for root cause analysis
- **Audit compliance violations** against Standard Operating Procedures (SOPs)
- **Provide actionable insights** to improve retail operations and ensure policy adherence

The agent acts as a compliance auditor and operational coach, helping retail teams maintain standards while optimizing performance.

## 📁 Directory Structure

```
adkretailagent/
├── README.md                      # This file
├── validated_insights.csv         # Validated operational insights
├── .git/                          # Git repository
├── .gitignore                     # Git ignore rules
└── retailcoachagent/              # Main agent package
    ├── __init__.py
    ├── agent.py                   # Agent logic with operational tools
    ├── data_engineering.ipynb     # Data pipeline notebook
    ├── gold_daily_performance.csv # Aggregated daily performance metrics
    ├── fact_enriched.csv          # Detailed transaction data with enrichment
    ├── validated_insights.csv     # Validated operational insights
    ├── SOP-FIN-003.txt            # Financial & Discount Policy SOP
    ├── SOP-LOG-002.txt            # Logistics SOP
    ├── SOP-OPS-004.txt            # Operations SOP
    ├── SOP-QA-001.txt             # Quality Assurance SOP
    └── data/                      # Raw data directory
        ├── bronze_dim_location.csv
        ├── bronze_dim_product.csv
        └── bronze_fact_sales.csv
```

## 🛠️ Key Components

### Agent Tools

1. **Tool A: Scan Gold CSV** (`tool_a_scan_gold`)
   - Scans daily performance metrics for anomalies
   - Identifies stores with excessive return rates (>10% of items sold)

2. **Tool B: Drill Down** (`tool_b_drill_down`)
   - Retrieves detailed transaction information for a specific location and date
   - Provides product-level insights on returns and discounts

3. **Tool C: Load SOP** (`tool_c_load_sop`)
   - Retrieves relevant Standard Operating Procedures
   - Supports: SOP-FIN-003, SOP-LOG-002, SOP-OPS-004, SOP-QA-001

4. **Tool D: Audit Anomalies** (`tool_audit_anomalies`)
   - Identifies unauthorized discounts (>15% per SOP-FIN-003)
   - Detects phantom inventory (sales with zero revenue)
   - Flags compliance violations requiring action

### Data Assets

- **gold_daily_performance.csv**: Aggregated daily KPIs by location
- **fact_enriched.csv**: Detailed transaction records with enriched context
- **validated_insights.csv**: Pre-validated operational insights
- **SOP-*.txt**: Compliance guidelines and operational procedures

## 📋 Requirements

Before you begin, ensure you have:

- **Python 3.10+**: Runtime environment
- **uv**: Python package manager - [Install](https://docs.astral.sh/uv/getting-started/installation/)
- **Google Cloud SDK**: For GCP services - [Install](https://cloud.google.com/sdk/docs/install)
- **pandas**: Data processing library
- **google-adk**: Google Agent Development Kit

## 🚀 Quick Start

### 1. Navigate to This Directory

```bash
cd adkretailagent
```

### 2. Install Dependencies

If using uv:
```bash
uv install
```

Or with pip:
```bash
pip install -r requirements.txt
```

### 3. Set Up Google Cloud Authentication

```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

### 4. Run the Agent

```bash
python -m retailcoachagent.agent
```

Or with uv:
```bash
uv run python -m retailcoachagent.agent
```

### 5. Test the Agent

```bash
python -m pytest tests/ -v
```

## 📊 Working with Data

The agent processes retail data through a data engineering pipeline:

```bash
# Launch Jupyter notebook for data exploration
jupyter notebook retailcoachagent/data_engineering.ipynb
```

### Data Flow
1. **Bronze Layer**: Raw data ingestion
   - `retailcoachagent/data/bronze_dim_location.csv`
   - `retailcoachagent/data/bronze_dim_product.csv`
   - `retailcoachagent/data/bronze_fact_sales.csv`

2. **Gold Layer**: Aggregated performance metrics
   - `retailcoachagent/gold_daily_performance.csv` - Daily KPIs

3. **Enriched**: Detailed transaction data
   - `retailcoachagent/fact_enriched.csv` - Enhanced with context

## 🔍 Example Usage

### Query 1: Identify High-Return Locations
```
User: "Show me stores with excessive return rates"
Agent: Uses Tool A to scan gold data → Identifies locations with >10% return rates → Provides summary
```

### Query 2: Audit Compliance Violations
```
User: "Audit recent transactions for SOP violations"
Agent: Uses Tool D → Identifies unauthorized discounts and phantom inventory → Suggests corrective actions
```

### Query 3: Investigate Specific Transaction
```
User: "Tell me about returns at location 42 on 2024-01-15"
Agent: Uses Tool B → Loads transaction details → Uses Tool C to reference SOP → Provides analysis
```

## 🧪 Testing

### Run All Tests
```bash
pytest -v
```

### Run Specific Test File
```bash
pytest retailcoachagent/tests/test_agent.py -v
```

### Run with Coverage
```bash
pytest --cov=retailcoachagent tests/
```

## 🔧 Development Workflow

1. **Edit agent logic** in `retailcoachagent/agent.py`
2. **Test locally** with `python -m retailcoachagent.agent`
3. **Run tests** with `pytest -v`
4. **Update data** by refreshing CSV files in `retailcoachagent/`
5. **Iterate** based on results

## � Adding New Tools

To add a new tool to the agent:

1. Create a function in `retailcoachagent/agent.py`:
```python
def tool_new_feature():
    """Your tool description"""
    # Implementation here
    return result
```

2. Register it with the agent in the same file

3. Add tests in the appropriate test directory

4. Update this README with the new tool documentation

## 📊 Project Statistics

- **Agent Model**: Gemini 2.5 Flash
- **Python Version**: 3.10+
- **Main Package**: `retailcoachagent`
- **Entry Point**: `retailcoachagent.agent`

## 🐛 Troubleshooting

### Import Errors
```bash
# Reinstall dependencies
uv install --refresh
```

### Data File Not Found
```bash
# Ensure you're in the correct directory
pwd
# Should show: /path/to/adkretailagent
```

### GCP Authentication Issues
```bash
gcloud auth login
gcloud auth application-default login
```

### Python Version Issues
Check your Python version:
```bash
python --version
# Should be 3.10 or higher
```

## 📞 Support

For issues or questions:
1. Review the agent code in `retailcoachagent/agent.py`
2. Check test files for usage examples
3. Review the data engineering notebook for data insights

## 📄 License

This project is part of the ADK (Agent Development Kit) ecosystem.

---

**Last Updated**: February 2026  
**Agent Version**: 0.1.0  
**Status**: Active Development
