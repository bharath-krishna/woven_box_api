from api.routers import profile
from api.configurations.base import config
from fastapi import FastAPI


class Application(FastAPI):
    def __init__(self, **kwargs):
        config.logger.info("Application starting")
        super().__init__(**kwargs)

app = Application(docs_url='/apidocs',
                  swagger_ui_oauth2_redirect_url='/callback',
                  title=config.title,
                  description="Code for logging, authentication with JWT token, e2e tests are added",
                  version="0.0.1")

app.include_router(profile.router, prefix=config.prefix)
