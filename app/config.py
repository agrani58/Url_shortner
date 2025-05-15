from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"
    ADMIN_USERNAME: str
    ADMIN_PASSWORD: str

    model_config = ConfigDict(extra="ignore")


settings = Settings()
