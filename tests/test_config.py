import pytest
import os
import sys
from pathlib import Path

# Add src to pythonpath for testing
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

from config.settings import Settings

def test_settings_default_values():
    """Test that default settings load correctly."""
    settings = Settings()
    assert settings.llm_provider == "openai"
    assert settings.model == "gpt-4.1-mini"
    assert settings.log_level == "INFO"
    assert settings.max_retries == 3
