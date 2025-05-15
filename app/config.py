from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"
    ADMIN_USERNAME: str = "admin"
    ADMIN_PASSWORD: str = "secret"

    model_config = ConfigDict(extra="ignore")


settings = Settings()
