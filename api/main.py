from api.routers import handle_file
from api.configurations.base import config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.configurations.readers import ConfigReader
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth


cred = credentials.Certificate({
  "type": ConfigReader().get('type'),
  "project_id": ConfigReader().get('project_id'),
  "private_key_id": ConfigReader().get('private_key_id'),
  "private_key": ConfigReader().get('private_key'),
  "client_email": ConfigReader().get('client_email'),
  "client_id": ConfigReader().get('client_id'),
  "auth_uri": ConfigReader().get('auth_uri'),
  "token_uri": ConfigReader().get('token_uri'),
  "auth_provider_x509_cert_url": ConfigReader().get('auth_provider_x509_cert_url'),
  "client_x509_cert_url": ConfigReader().get('client_x509_cert_url')
}
)
firebase_admin.initialize_app(cred)
db = firestore.client()


class Application(FastAPI):
    def __init__(self, **kwargs):
        self.db = db
        self.auth = auth
        config.logger.info("Application starting")
        super().__init__(**kwargs)

app = Application(docs_url='/apidocs',
                  swagger_ui_oauth2_redirect_url='/callback',
                  title=config.title,
                  description="Code for logging, authentication with JWT token, e2e tests are added",
                  version="0.0.1")


origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(handle_file.router, prefix=config.prefix)
