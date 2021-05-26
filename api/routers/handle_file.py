from api.modules.uploads import FileUploadModel
import aiofiles
import os

from pathlib import Path
from typing import Dict, List
import fastapi

from fastapi.datastructures import UploadFile
from fastapi.param_functions import File
from api.modules.profile import Profile
from api.models.auth import require_user
from api.models.profile import  UserModel
from fastapi import APIRouter, Depends, Request, HTTPException
router = APIRouter()


@router.get('/uploads',
            tags=['Profile'],
            summary='Get Profile',
            description='Get user profile',
            response_model=Dict[str, List[str]]
            )
async def get_uploads(request: Request):
    uploads = FileUploadModel()
    response = await uploads.get_uploads()
    return response


@router.post('/uploads',
            tags=['Profile'],
            summary='Get Profile',
            description='Get user profile',
            response_model=Dict[str, List[str]]
            )
async def upload_files(request: Request, uploaded_files: List[UploadFile] = File(...)):
    uploads = FileUploadModel()
    response = await uploads.upload_file(uploaded_files)
    return response


@router.delete('/uploads',
            tags=['Profile'],
            summary='Get Profile',
            description='Get user profile',
            response_model=Dict[str, str]
            )
async def delete_file(request: Request, filename: str):
    uploads = FileUploadModel()
    response = await uploads.delete_file(filename)
    return response
