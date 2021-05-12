from api.exceptions.api import APIError
from fastapi.security.http import HTTPAuthorizationCredentials
from api.models.profile import UserModel
import jwt
from fastapi import Depends, Request
from fastapi.security import HTTPBearer
from jwt import DecodeError, ExpiredSignatureError
from api.configurations.base import config


bearer_scheme = HTTPBearer()

def get_token_user(request: Request, auth_creds: HTTPAuthorizationCredentials = Depends(bearer_scheme)) -> UserModel:
    token = auth_creds.credentials

    try:
        user = jwt.decode(token, key=config.signature_text, algorithms=["HS256"])
    except (ExpiredSignatureError, DecodeError):
        raise APIError("unauthorized")
    return user

async def require_user(user: UserModel = Depends(get_token_user)) -> UserModel:
    return user
