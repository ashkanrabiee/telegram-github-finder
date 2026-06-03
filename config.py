"""Configuration and environment variables."""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Central configuration class."""

    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

    # GitHub API settings
    GITHUB_SEARCH_PER_PAGE = 30  # Max results per search
    GITHUB_API_BASE_URL = "https://api.github.com"

    # OpenAI settings
    OPENAI_MODEL = "gpt-4o-mini"  # Cost-effective model
    OPENAI_TEMPERATURE = 0.3

    @classmethod
    def validate(cls) -> None:
        """Validate that all required environment variables are set."""
        if not cls.TELEGRAM_BOT_TOKEN:
            raise ValueError("TELEGRAM_BOT_TOKEN is not set in environment variables")
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is not set in environment variables")
        if not cls.GITHUB_TOKEN:
            raise ValueError("GITHUB_TOKEN is not set in environment variables")


# Validate on import
Config.validate()