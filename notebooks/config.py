"""Load configuration from .env."""
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    """The configuration class."""
    
    MODEL: str | None = None
    API_TOKEN: str | None = None
    
    def __init__(self):
        load_dotenv()
        super().__init__()


    # def __init__(self, MODEL, API_TOKEN):
    #     self.MODEL = MODEL
    #     self.API_TOKEN = API_TOKEN

        # load_dotenv()
        # super().__init__()
