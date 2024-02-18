"""Load configuration from .env."""
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    """The configuration class."""
    
    CACHE_SHARDS: str
    CACHE: str
    SALESFORCE: str
    
    def __init__(self):
        load_dotenv()
        super().__init__()
