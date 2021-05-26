from api.routers import handle_file, profile
from api.configurations.base import config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


class Application(FastAPI):
    def __init__(self, **kwargs):
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

app.include_router(profile.router, prefix=config.prefix)
app.include_router(handle_file.router, prefix=config.prefix)
