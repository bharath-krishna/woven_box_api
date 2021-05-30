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
        try:
            _, _, filenames = next(os.walk(uploads_path.__str__()))
        except StopIteration:
            return {'filenames': []}
        return {'filenames': filenames}

    async def upload_file(self, uploaded_files, user) -> Dict[str, List[str]]:
        uploads_path = self.get_uploads_path(user)
        
        for uploaded_file in uploaded_files:
            if Path(uploaded_file.filename).is_absolute():
                raise HTTPException(status_code=400, detail="Please provide relative path")

            name = uploads_path/uploaded_file.filename
            try:
                async with aiofiles.open(name.__str__(), 'wb') as saving_file:
                    while True:
                        content = await uploaded_file.read(1024)
                        if not content:
                            break
                        await saving_file.write(content)
            except FileNotFoundError:
                raise HTTPException(status_code=404, detail=f"File '{uploaded_file.filename}' Not Found")
        return {'uploaded_files': [uploaded_file.filename for uploaded_file in uploaded_files]}

    async def delete_file(self, filename, user) -> Dict[str, str]:
        uploads_path = self.get_uploads_path(user)
        try:
            os.remove(str(uploads_path) + '/' + filename)
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail=f"File {filename} Not Found in storage")
        return {'removed_file': filename}
