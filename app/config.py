import yaml
from typing import Optional
from pydantic import BaseModel, ValidationError

class AppConfigServer(BaseModel):
  host: str = "0.0.0.0"
  port: int = 9002
  debug: bool = False
class AppConfigHA(BaseModel):
  url: str = "http://localhost:8123"
  token: str = ""
class AppConfig(BaseModel):
  server: AppConfigServer = AppConfigServer()
  ha: AppConfigHA = AppConfigHA()

cfg = None | AppConfig

def load_config(config_path: str) -> AppConfig:
    """Load configuration from a YAML file."""
    try:
        with open(config_path, 'r') as file:
            config_data = yaml.safe_load(file)
        return AppConfig(**config_data)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    except ValidationError as e:
        raise ValueError(f"Invalid configuration: {e}") from e
