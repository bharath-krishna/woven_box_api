from api.exceptions.api import APIError
from fastapi.security.http import HTTPAuthorizationCredentials
from api.models.profile import UserModel
from fastapi import Depends, Request
from fastapi.security import HTTPBearer
from firebase_admin._auth_utils import InvalidIdTokenError

bearer_scheme = HTTPBearer()

def get_token_user(request: Request,
        auth_creds: HTTPAuthorizationCredentials = Depends(bearer_scheme)) -> UserModel:
    token = auth_creds.credentials

    try:
        user = request.app.auth.verify_id_token(token)
    except (InvalidIdTokenError):
        raise APIError('unauthorized')
    return user

async def require_user(user: UserModel = Depends(get_token_user)) -> UserModel:
    return user
