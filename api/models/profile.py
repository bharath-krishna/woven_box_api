from typing import Dict, List, Optional
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
    email: Optional[str]
    email_verified: Optional[bool]
    firebase: FirebaseModel
    uid: str

