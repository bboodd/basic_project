from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_DATABASE: str
    MYSQL_ROOT_PASSWORD: str

    @property
    def SQLALCHEMY_DATABASE_URL(self) -> str:
        return 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
            self.MYSQL_USER,
            self.MYSQL_PASSWORD,
            self.MYSQL_HOST,
            self.MYSQL_PORT,
            self.MYSQL_DATABASE
        )

    class Config:
        env_file = '.env'
    
settings = Settings()