from api.exceptions.api import APIError
from api.modules import BaseModule
from typing import Dict, List
import aiofiles
import os
from api.configurations.base import config

from pathlib import Path
from fastapi import HTTPException


class FileUploadModel(BaseModule):
    def get_uploads_path(self, user) -> str:
        storage_path = config.storage_path
        uploads_path = Path(storage_path)/f'{str(user.uid)}/uploads'
        if not os.path.exists(uploads_path.__str__()):
            try:
                os.makedirs(uploads_path.__str__())
            except:
                raise APIError('not_found_general', value='Personal space')
        return uploads_path

    async def get_file_exists(self, user, filename):
        uploads_path = self.get_uploads_path(user)
        filepath = uploads_path/filename
        if not os.path.exists(filepath.__str__()):
            raise APIError('not_found_general', value=f'File {filename}')
        return filepath

    async def get_uploads(self, user) -> Dict[str, List[str]]:
        uploads_path = self.get_uploads_path(user)
        filenames = await self.client.get_dir_files(uploads_path)
        return {'filenames': filenames}

    async def upload_file(self, uploaded_files, user) -> Dict[str, List[str]]:
        uploads_path = self.get_uploads_path(user)
        uploaded_file_result = await self.client.upload_file(uploaded_files, uploads_path)
        return {'uploaded_files': uploaded_file_result}

    async def delete_file(self, filename, user) -> Dict[str, str]:
        uploads_path = self.get_uploads_path(user)
        deleted_file = await self.client.delete_file(filename, uploads_path)
        return {'removed_file': deleted_file}
