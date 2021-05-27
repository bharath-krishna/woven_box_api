from api.modules.profile import Profile
from api.models.auth import require_user
from api.models.profile import  UserModel
from fastapi import APIRouter, Depends, Request

router = APIRouter()


@router.get('/profile',
            tags=['Profile'],
            summary='Get Profile',
            description='Get user profile',
            response_model=UserModel
            )
async def get_profile(request: Request, user: UserModel = Depends(require_user)):
    profile_model = Profile(request)
    profile = await profile_model.get_profile(user)
    return profile
