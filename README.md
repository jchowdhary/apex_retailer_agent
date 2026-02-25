# Retail Coach Agent

An intelligent AI agent designed to help retail operations teams identify anomalies, audit compliance violations, and make data-driven operational decisions. The agent uses Google's Agent Development Kit (ADK) to provide real-time insights into retail sales data and operational procedures.

## 🎯 Project Goal

The Retail Coach Agent leverages advanced LLM capabilities to:
- **Scan operational data** for high-level anomalies in retail performance metrics
- **Drill down into transaction details** for root cause analysis
- **Audit compliance violations** against Standard Operating Procedures (SOPs)
- **Provide actionable insights** to improve retail operations and ensure policy adherence

The agent acts as a compliance auditor and operational coach, helping retail teams maintain standards while optimizing performance.

## 📁 Project Structure

```
adk-starter-pack/
├── retailcoachagent/              # Main retail coach agent
│   ├── agent.py                   # Agent logic with operational tools
│   ├── gold_daily_performance.csv # Aggregated daily performance metrics
│   ├── fact_enriched.csv          # Detailed transaction data with enrichment
│   ├── validated_insights.csv     # Validated operational insights
│   ├── SOP-*.txt                  # Standard Operating Procedures
│   └── data_engineering.ipynb     # Data pipeline notebook
├── adkretailagent/                # Alternative agent implementation
├── adk-a2a-backup/                # A2A protocol agent reference
└── adksample/                     # Sample ADK project structure
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
- **make**: Build automation tool (pre-installed on Unix-based systems)

### Python Dependencies

The project uses the following key dependencies:
- `google-adk`: Google Agent Development Kit
- `google-cloud-aiplatform`: For agent deployment and evaluation
- `pandas`: Data processing and analysis
- `pytest`: Testing framework

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd /home/jayant/adk-starter-pack
make install
```

Or manually with uv:
```bash
uv install
```

### 2. Set Up Google Cloud

Authenticate with Google Cloud:
```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

### 3. Run the Agent Locally

```bash
make playground
```

This launches an interactive development environment where you can test the agent in real-time with auto-reload on code changes.

### 4. Run Tests

```bash
make test
```

Runs unit and integration tests to verify agent functionality.

### 5. Run Evaluations

```bash
make eval
```

Evaluates agent performance against predefined evalsets.

## 📊 Working with Data

The agent processes retail data through a data engineering pipeline:

```bash
# Launch Jupyter notebook for data exploration
jupyter notebook retailcoachagent/data_engineering.ipynb
```

### Data Flow
1. **Bronze Layer**: Raw data ingestion
   - `data/bronze_dim_location.csv`
   - `data/bronze_dim_product.csv`
   - `data/bronze_fact_sales.csv`

2. **Gold Layer**: Aggregated performance metrics
   - `gold_daily_performance.csv` - Daily KPIs

3. **Enriched**: Detailed transaction data
   - `fact_enriched.csv` - Enhanced with context

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

## 📝 Commands Reference

| Command | Description |
|---------|-------------|
| `make install` | Install all dependencies using uv |
| `make playground` | Launch interactive development environment |
| `make test` | Run unit and integration tests |
| `make eval` | Run evaluation against evalsets |
| `make lint` | Run code quality checks (ruff) |
| `make deploy` | Deploy agent to Google Agent Engine |
| `make inspector` | Launch A2A Protocol Inspector |

For full details, see the [Makefile](adk-a2a-backup/Makefile).

## 🧪 Testing

### Unit Tests
```bash
pytest tests/unit/ -v
```

### Integration Tests
```bash
pytest tests/integration/ -v
```

### All Tests
```bash
make test
```

## 🔧 Development Workflow

1. **Edit agent logic** in `retailcoachagent/agent.py`
2. **Test interactively** with `make playground` (auto-reloads on save)
3. **Run tests** with `make test`
4. **Evaluate** with `make eval`
5. **Deploy** when ready with `make deploy`

## 🚢 Deployment

### Deploy to Google Agent Engine

```bash
gcloud config set project YOUR_PROJECT_ID
make deploy
```

### Register with Gemini Enterprise (Optional)

```bash
make register-gemini-enterprise
```

## 📚 Documentation

- **ADK Cheatsheet**: [Agent definitions, tools, callbacks](https://raw.githubusercontent.com/GoogleCloudPlatform/agent-starter-pack/refs/heads/main/agent_starter_pack/resources/docs/adk-cheatsheet.md)
- **Evaluation Guide**: [Eval config, metrics, best practices](https://raw.githubusercontent.com/GoogleCloudPlatform/agent-starter-pack/refs/heads/main/agent_starter_pack/resources/docs/adk-eval-guide.md)
- **Deployment Guide**: [Infrastructure, CI/CD setup](https://raw.githubusercontent.com/GoogleCloudPlatform/agent-starter-pack/refs/heads/main/agent_starter_pack/resources/docs/adk-deploy-guide.md)
- **ADK Documentation**: [Full API reference](https://google.github.io/adk-docs/llms.txt)

## 🤝 Contributing

1. Create a new branch for features/fixes
2. Make changes in `retailcoachagent/agent.py`
3. Add tests in `tests/`
4. Run `make lint` to check code quality
5. Run `make test` to verify functionality
6. Submit pull request

## 📊 Project Statistics

- **Agent Model**: Gemini 2.5 Flash
- **Python Version**: 3.10+
- **Main Dependencies**: google-adk, google-cloud-aiplatform, pandas
- **Test Framework**: pytest with asyncio support

## 🐛 Troubleshooting

### Import Errors
```bash
# Ensure dependencies are installed
make install
```

### Data File Not Found
```bash
# Verify you're running from project root
cd /home/jayant/adk-starter-pack
```

### GCP Authentication Issues
```bash
gcloud auth login
gcloud auth application-default login
```

### Port Already in Use (Playground)
Change the port in your make command:
```bash
PORT=8001 make playground
```

## 📞 Support

For issues or questions:
1. Check the [ADK documentation](https://google.github.io/adk-docs/)
2. Review the [GEMINI.md](adk-a2a-backup/GEMINI.md) for AI-assisted debugging
3. Run `make playground` for interactive testing

## 📄 License

This project follows the licensing guidelines of the Google Cloud Platform Agent Starter Pack.

---

**Last Updated**: February 2026  
**Agent Version**: 0.1.0  
**Status**: Active Development
