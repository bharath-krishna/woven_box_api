import os
from pathlib import Path
import aiofiles

from fastapi.exceptions import HTTPException
from api.configurations.base import config


class FileStorageClient():
    async def get_dir_files(self, dir_path):
        try:
            _, _, filenames = next(os.walk(dir_path.__str__()))
        except StopIteration:
            return []
        return filenames

    async def upload_file(self, uploaded_files, uploads_path):
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
        return [uploaded_file.filename for uploaded_file in uploaded_files]

    async def delete_file(self, filename, uploads_path):
        try:
            os.remove(str(uploads_path) + '/' + filename)
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail=f"File {filename} Not Found in storage")
        return filename
