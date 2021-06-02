from api.modules.file_storage_client.uploads import FileStorageClient
from typing import Callable
from api.modules.uploads import FileUploadModel
import pytest
from pathlib import Path


@pytest.fixture
def file_upload_module(monkeypatch) -> Callable[[dict], FileUploadModel]:
    def mock_file_upload_module(mocked_return_data) -> FileUploadModel:
        def mock__init__(self, *args, **kwargs):
            return

        monkeypatch.setattr(FileUploadModel, '__init__', mock__init__)

        def mock_get_uploads_path(self, *args, **kwargs):
            return mocked_return_data

        monkeypatch.setattr(FileUploadModel, 'get_uploads_path', mock_get_uploads_path)
        return FileUploadModel()

    return mock_file_upload_module


@pytest.fixture
def file_storage_clinet(monkeypatch) -> Callable[[dict], FileStorageClient]:
    def mock_mock_file_storage_client(mocked_return_data) -> FileStorageClient:
        # def mock__init__(self, *args, **kwargs):
        #     return

        # monkeypatch.setattr(FileStorageClient, '__init__', mock__init__)

        async def mock_get_dir_files(self, *args):
            return mocked_return_data['get_dir_files']

        async def mock_upload_file(self, *args, **kwargs):
            return mocked_return_data['upload_file']

        async def mock_delete_file(self, *args, **kwargs):
            return mocked_return_data['delete_file']

        monkeypatch.setattr(FileStorageClient, 'get_dir_files', mock_get_dir_files)
        monkeypatch.setattr(FileStorageClient, 'upload_file', mock_upload_file)
        monkeypatch.setattr(FileStorageClient, 'delete_file', mock_delete_file)
        return FileStorageClient()

    return mock_mock_file_storage_client
