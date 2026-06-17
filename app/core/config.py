from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    DATABASE_URL: str = Field(..., description = "Database URL")
    APP_NAME: str = Field(..., description = "Application Name")
    DEBUG_MODE: bool = Field(..., description = "Debug Mode")
    PORT: int = Field(..., description = "Port Number")

    #allow pydantic to read from .env file
    model_config = SettingsConfigDict(
    env_file = ".env",
    env_file_encoding = "utf-8",
    extra = "ignore"
    ) 

#singleton instance of settings
settings = Settings()
