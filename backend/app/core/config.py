from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str
    database_url: str
    redis_url: str
    jwt_secret: str
    access_token_minutes: int = 15
    refresh_token_days: int = 7
    model_config=SettingsConfigDict(env_file="../.env")

settings=Settings()