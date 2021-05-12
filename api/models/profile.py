from pydantic import BaseModel


class UserModel(BaseModel):
    id: str
    name: str
    exp: int
    sub: str
    iat: int
