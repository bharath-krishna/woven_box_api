from typing import Dict, List
from pydantic import BaseModel


class FirebaseModel(BaseModel):
    identities: Dict[str, List[str]]
    sign_in_provider: str


class UserModel(BaseModel):
    iss: str
    aud: str
    auth_time: int
    user_id: str
    sub: str
    iat: int
    exp: int
    email: str
    email_verified: bool
    firebase: FirebaseModel
    uid: str

