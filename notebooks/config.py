"""Load configuration from .env."""
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    """The configuration class."""
    
    SHARDS: str
    SALESFORCE: str
    ## PYDEVD_DISABLE_FILE_VALIDATION: int ## = 1
    
    def __init__(self):
        load_dotenv()
        super().__init__()
