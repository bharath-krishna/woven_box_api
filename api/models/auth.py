from api.exceptions.api import APIError
from fastapi.security.http import HTTPAuthorizationCredentials
from api.models.profile import UserModel
from fastapi import Depends, Request
from fastapi.security import HTTPBearer
from firebase_admin._auth_utils import InvalidIdTokenError

bearer_scheme = HTTPBearer()


class User():
    def __init__(self, auth, access_token=''):
        self.auth = auth
        self.access_token = access_token

    @classmethod
    def log_user_in(cls, request: Request, token: str) -> UserModel:
        user = cls(request.app.auth, token)
        return user.get_token_user()

    def get_token_user(self) -> UserModel:
        try:
            user = UserModel(**self.auth.verify_id_token(self.access_token))
        except (InvalidIdTokenError):
            raise APIError('unauthorized')
        return user


async def require_user(request: Request,
        auth_creds: HTTPAuthorizationCredentials = Depends(bearer_scheme)) -> UserModel:
    token = auth_creds.credentials
    user: User = User.log_user_in(request, token)
    return user
