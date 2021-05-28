from pydantic import BaseModel
from api.configurations.base import config


class InfoModel(BaseModel):
    Name: str
    Version: str
