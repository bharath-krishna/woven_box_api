import mimetypes
from starlette.responses import FileResponse
from api.modules.uploads import FileUploadModel
from typing import Dict, List
from fastapi.datastructures import UploadFile
from fastapi.param_functions import File
from api.models.auth import require_user
from api.models.profile import  UserModel
from fastapi import APIRouter, Depends, Request, HTTPException


router = APIRouter()

@router.get('/uploads',
            tags=['Uploads'],
            summary='Get all uploaded files',
            response_model=Dict[str, List[str]]
            )
async def get_uploads(request: Request, user: UserModel = Depends(require_user)):
    uploads = FileUploadModel(request)
    response = await uploads.get_uploads(user)
    return response


@router.get('/uploads/{filename}',
            tags=['Uploads'],
            summary='Retreive a file',
            )
async def get_uploads(request: Request, filename: str, user: UserModel = Depends(require_user)):
    uploads = FileUploadModel(request)
    filepath = await uploads.get_file_exists(user, filename)
    filetype, _ = mimetypes.guess_type(filepath)
    return FileResponse(filepath, media_type=filetype)


@router.post('/uploads',
            tags=['Uploads'],
            summary='Upload a file',
            response_model=Dict[str, List[str]]
            )
async def upload_files(request: Request, uploaded_files: List[UploadFile] = File(...),
        user: UserModel = Depends(require_user)):
    uploads = FileUploadModel(request)
    response = await uploads.upload_file(uploaded_files, user)
    return response


@router.delete('/uploads/{filename}',
            tags=['Uploads'],
            summary='Delete an uploaded file',
            response_model=Dict[str, str]
            )
async def delete_file(request: Request, filename: str, user: UserModel = Depends(require_user)):
    uploads = FileUploadModel(request)
    response = await uploads.delete_file(filename, user)
    return response
