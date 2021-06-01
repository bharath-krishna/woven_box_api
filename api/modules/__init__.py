from api.modules.file_storage_client.uploads import FileStorageClient
from fastapi import Request


class BaseModule():
    def __init__(self, request: Request) -> None:
        self.request = request
        self.db = request.app.db
        self.auth = request.app.auth
        file_storage_client = FileStorageClient()
        self.client = file_storage_client
