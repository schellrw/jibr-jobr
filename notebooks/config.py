"""Load configuration from .env."""
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    """The configuration class."""
    
    SHARDS: str | None = None
    SALESFORCE: str | None = None
    CACHE: str | None = None
    # HF_HOME: str | None = None
    # HF_DATASETS_CACHE: str | None = None
    # TRANSFORMERS_CACHE: str | None = None
    
    def __init__(self):
        load_dotenv()
        super().__init__()
