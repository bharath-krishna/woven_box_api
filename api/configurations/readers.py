import base64
import json
from api.configurations.base import config

_firebase_configs = {}


class ConfigReader():
    def __init__(self):
        firebase_configs = config.firebase
        if not firebase_configs:
            raise Exception(f'"API_FIREBASE_CONFIGS" environment varible not set')
        global _firebase_configs

        if not _firebase_configs:
            # if secret file not exist, raise exception and quit.
            _firebase_configs = json.loads(base64.b64decode(bytes(firebase_configs, 'utf-8')))

    def get(self, secret_key):
        global _firebase_configs
        return _firebase_configs.get(secret_key, None)


class SecretReader(ConfigReader):
    def __init__(self):
        super().__init__(env_name='FASTAPI_firebase_configs')
