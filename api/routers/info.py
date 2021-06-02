from api.models.info import InfoModel
from fastapi import APIRouter
from api.configurations.base import config


router = APIRouter()

@router.get('/info',
            tags=['Info'],
            summary='Get Application information',
            response_model=InfoModel
            )
async def get_uploads():
    response = InfoModel(
        Name = config.title,
        Version = config.version,
    )
    return response
