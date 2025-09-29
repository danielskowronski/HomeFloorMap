import yaml
from typing import Optional
from pydantic import BaseModel, ValidationError

class AppConfigSensorMergeRain(BaseModel):
  min15: str = ""
  hour: str = ""
  day: str = ""
class AppConfigSensorMerge(BaseModel):
  window: dict[str, list[str]] = {}
  rain: dict[str, AppConfigSensorMergeRain] = {}
class AppConfigSensorMap(BaseModel):
  sensor: dict[str, str] = {}
  binary_sensor: dict[str, str] = {}
  cover: dict[str, str] = {}
  climate: dict[str, str] = {}
class AppConfigProm(BaseModel):
  url: str = "http://localhost:9090"
  query: str = '{__name__=~"homeassistant_.*"}'
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
  prom: AppConfigProm = AppConfigProm()
  sensorMap: AppConfigSensorMap = AppConfigSensorMap()
  sensorMerge: AppConfigSensorMerge = AppConfigSensorMerge()

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
