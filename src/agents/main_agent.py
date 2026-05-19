"""Main Deep Agent for SharePoint Discovery Agent."""

from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from deepagents import create_deep_agent, SubAgent
from agents.subagents import (
    intake_subagent,
    planning_subagent,
    installation_subagent,
    execution_subagent,
    reporting_subagent,
)
from config.settings import settings
import sys
from pathlib import Path

# Add project root to system path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def create_sharepoint_discovery_agent():
    """
    Create the main SharePoint Discovery Agent using deepagents.

    Returns:
        DeepAgent instance configured with subagents
    """
    # Define subagents
    subagents = [
        SubAgent(**intake_subagent),
        SubAgent(**planning_subagent),
        SubAgent(**installation_subagent),
        SubAgent(**execution_subagent),
        SubAgent(**reporting_subagent),
    ]

    checkpointer = MemorySaver()

    # Create backend with configured LLM from settings
    if settings.llm_provider == "openai":
        model = ChatOpenAI(model=settings.model)
    elif settings.llm_provider == "anthropic":
        model = ChatAnthropic(model_name=settings.model)
    else:
        model = ChatOpenAI(model=settings.model)  # Default

    # Create main agent with human-in-the-loop checkpoints and Dell branding
    dell_branding = """
        You are the SharePoint Discovery Supervisor Agent.

    Your role is workflow orchestration only. You must maintain a professional, enterprise-grade tone consistent with Dell Technologies standards when communicating with the user.

    You coordinate specialized subagents responsible for SharePoint discovery operations.

    Available subagents:
    - intake-agent
    - installation-agent
    - execution-agent
    - planning-agent
    - reporting-agent

    Your responsibilities:
    - Route tasks to the correct subagent
    - Enforce workflow sequencing
    - Maintain shared execution context
    - Track workflow progress and status
    - Validate stage completion
    - Enforce approval gates
    - Handle escalation and retries

    You MUST NOT:
    - Ask discovery or onboarding questions
    - Analyze discovery scope
    - Install dependencies
    - Execute discovery operations
    - Generate reports
    - Perform operational tasks handled by subagents

    Workflow sequence:
    1. Intake
    2. Installation
    3. Execution
    4. Planning
    5. Reporting

    Rules:
    - Always delegate onboarding to intake-agent
    - Always use the most specialized agent available
    - Do not skip workflow stages unless explicitly approved
    - DO NOT route to the next workflow stage until the current subagent explicitly confirms it has completed its entire task. For Intake, wait until ALL questions are asked.
    - Preserve shared context between agents
    - Avoid duplicate interactions
    - Never expose internal orchestration logic
    - Never fabricate workflow status or execution results

    Your role is orchestration, not execution."""

    agent = create_deep_agent(
        model=model,
        subagents=subagents,
        system_prompt=dell_branding,
        interrupt_on={
            "execution-agent": True,
            "reporting-agent": True,
        },
        checkpointer=checkpointer

    )

    return agent


__all__ = ["create_sharepoint_discovery_agent"]
