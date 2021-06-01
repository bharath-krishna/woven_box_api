from pathlib import Path
from fastapi.datastructures import UploadFile
import pytest
import io


pytestmark = pytest.mark.uploads


def test_get_uploads(user_client, file_storage_clinet):
    filenames = [Path(__file__).name]
    storage_mock_data = {'get_dir_files': filenames}
    file_storage_clinet(mocked_return_data=storage_mock_data)

    response = user_client.get('/api/uploads')
    json_response = response.json()
    assert response.status_code == 200
    assert 'filenames' in json_response
    for filename in filenames:
        assert filename in json_response['filenames']


def test_post_uploads(user_client, file_upload_module, file_storage_clinet):
    storage_mock_data = {'upload_file': [Path(__file__).name]}
    file_storage_clinet(mocked_return_data=storage_mock_data)

    uploaded_files = ("banner.jpg", open(Path(__file__).__str__(), "rb"), "plain/text")
    data = {'uploaded_files': uploaded_files}
    response = user_client.post('/api/uploads', files=data)
    json_response = response.json()
    assert response.status_code == 200
    assert 'uploaded_files' in json_response
    assert Path(__file__).name in json_response['uploaded_files']



def test_delete_file(user_client, file_storage_clinet):
    filename = Path(__file__).name
    storage_mock_data = {'delete_file': filename}
    file_storage_clinet(mocked_return_data=storage_mock_data)
    
    response = user_client.delete(f'/api/uploads/{filename}')
    json_response = response.json()
    assert response.status_code == 200
    assert 'removed_file' in json_response
    assert filename == json_response['removed_file']


