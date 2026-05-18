# SharePoint Discovery Agent

Dell-branded enterprise AI discovery and migration assessment platform for SharePoint Online and OneDrive.

## Overview

The SharePoint Discovery Agent is an enterprise AI-powered platform that automates the discovery and assessment of Microsoft 365 environments for migration planning. Built with the DeepAgents framework, it provides a supervisor-based orchestration pattern with structured state management, human approval checkpoints, and comprehensive reporting.

## Features

- **Automated Discovery**: Comprehensive inventory of SharePoint sites, OneDrive, users, permissions, and storage
- **Assessment**: Migration readiness evaluation with risk identification and recommendations
- **Planning**: Strategic execution planning with dependency mapping and optimization
- **Environment Preparation**: Automated prerequisite installation and authentication configuration
- **Script Execution**: Autonomous execution of discovery scripts with self-healing capabilities
- **Reporting**: Dell-approved executive and technical reports with actionable recommendations

## Architecture

The platform uses the DeepAgents framework with the following architecture:

```
Main Deep Agent (create_deep_agent)
├── Intake Subagent - Question-based intake, collects credentials
├── Planning Subagent - Planning and strategy
├── Installation Subagent - Prerequisite setup with verification
├── Execution Subagent - Discovery with self-healing
└── Reporting Subagent - Dell-approved report generation
```

### Tech Stack

- **Python 3.11+**
- **PowerShell Core 7.0+** (pwsh)
- **DeepAgents** - Agent framework with create_deep_agent()
- **LangChain** - Tool integration
- **PnP.PowerShell** - SharePoint/OneDrive discovery
- **Configurable LLM** - OpenAI, Anthropic, or other models

## Installation

### Prerequisites

- Python 3.11 or higher
- PowerShell Core (pwsh) 7.0 or higher
- Global Administrator access to Microsoft 365 tenant
- Network connectivity to Microsoft 365 services

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd SharePoint-Discovery-Agent
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\Activate.ps1  # Windows
   source venv/bin/activate   # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run the agent**
   ```bash
   python main.py
   ```

### Autonomous Mode

Run in autonomous mode for demonstration:
```bash
python main.py --autonomous
```

## Usage

### Interactive Mode

In interactive mode, the agent will:
1. Ask for tenant name, tenant ID, and client ID
2. Guide you through discovery requirements
3. Request approval at execution and reporting checkpoints
4. Generate Dell-approved reports

### Autonomous Mode

In autonomous mode, the agent will:
1. Use default values for intake
2. Auto-approve all checkpoints
3. Execute discovery scripts automatically
4. Generate reports without user intervention

## Workflow Phases

1. **Intake** - Gather requirements and authentication credentials
2. **Planning** - Create execution plan and strategy
3. **Installation** - Verify prerequisites and install PnP.PowerShell
4. **Execution** - Run discovery scripts with self-healing
5. **Reporting** - Generate Dell-approved assessment reports

## Configuration

Configuration is managed through `config/settings.py` with defaults, and environment variables in `.env` for sensitive values like API keys.

### How Configuration Works

Pydantic Settings loads configuration in this order:
1. Default values in `config/settings.py`
2. Environment variables from `.env` (overrides defaults if present)
3. Environment variables from system (overrides both above)

### Configuration in config/settings.py

The following settings have defaults defined in `config/settings.py`:
- `llm_provider`: Default is "openai" (options: openai, anthropic, azure, google)
- `model`: Default is "gpt-4.1-mini" (e.g., gpt-4, claude-sonnet-4-6, etc.)
- `log_level`: Default is "INFO"
- `log_format`: Default is "json"
- `max_retries`: Default is 3
- `max_iterations`: Default is 10
- `require_human_approval`: Default is True

### Environment Variables (.env)

The `.env` file should only contain sensitive values like API keys. These override the None defaults in settings.py:

```env
# OpenAI
OPENAI_API_KEY=your-openai-api-key
# Anthropic
ANTHROPIC_API_KEY=your-anthropic-api-key
# Azure OpenAI
AZURE_OPENAI_API_KEY=your-azure-openai-api-key
AZURE_OPENAI_ENDPOINT=your-azure-openai-endpoint
# Google
GOOGLE_API_KEY=your-google-api-key

# Optional: Override logging defaults
LOG_LEVEL=INFO
LOG_FORMAT=json
```

**Note:** Do NOT put `llm_provider` or `model` in `.env`. Configure these in `config/settings.py` directly.

### Supported LLM Providers and Models

**OpenAI:**
- gpt-4
- gpt-4-turbo
- gpt-4o
- gpt-3.5-turbo

**Anthropic:**
- claude-sonnet-4-6
- claude-3-opus
- claude-3-sonnet
- claude-3-haiku

**Azure OpenAI:**
- Any Azure OpenAI model

**Google:**
- gemini-pro
- gemini-pro-vision

## Project Structure

```
sharepoint-discovery-agent/
├── skills/              # Skill directories with SKILL.md files
│   ├── discovery/       # Discovery skills
│   ├── assessment/      # Assessment skills
│   ├── planning/        # Planning skills
│   ├── execution/       # Execution skills
│   └── reporting/       # Reporting skills
├── scripts/             # PowerShell scripts
│   ├── discovery/       # Discovery scripts
│   └── setup/           # Setup scripts
├── tools/               # LangChain tools
├── agents/              # Subagents and main agent
├── config/              # Configuration
├── main.py              # Entry point
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

## DeepAgents Usage

### Creating the Main Agent

```python
from deepagents import create_deep_agent
from agents.subagents import (
    intake_subagent,
    planning_subagent,
    installation_subagent,
    execution_subagent,
    reporting_subagent,
)

subagents = [
    intake_subagent,
    planning_subagent,
    installation_subagent,
    execution_subagent,
    reporting_subagent,
]

agent = create_deep_agent(
    subagents=subagents,
    interrupt_on={
        "execution-agent": True,
        "reporting-agent": True,
    },
)
```

### Subagent Configuration

Each subagent is configured with:
- `name`: Subagent identifier
- `description`: Subagent purpose
- `system_prompt`: System instructions
- `tools`: Available LangChain tools
- `skills`: Skill directories to use

## Security

- Never commit credentials to version control
- Use certificate-based authentication for production
- Rotate credentials regularly
- Limit permissions to minimum required
- Monitor audit logs for suspicious activity

## License

Proprietary - Dell Technologies

## Support

For issues or questions, contact the Dell support team.

