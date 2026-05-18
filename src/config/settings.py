"""Configuration settings for DeepAgents framework."""

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    """Application settings using Pydantic-Settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="SP_AGENT_",
        extra="ignore",
    )

    # LLM Provider Configuration (configured here, not in .env)
    llm_provider: str = "openai"
    model: str = "gpt-4.1-mini"
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    azure_openai_api_key: Optional[str] = None
    azure_openai_endpoint: Optional[str] = None
    google_api_key: Optional[str] = None

    # Logging Configuration
    log_level: str = "INFO"
    log_format: str = "json"

    # Execution Configuration
    max_retries: int = 3
    max_iterations: int = 10

    # Human Approval Configuration
    require_human_approval: bool = True


settings = Settings()
