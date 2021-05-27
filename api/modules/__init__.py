from fastapi import Request


class BaseModule():
    def __init__(self, request: Request) -> None:
        self.request = request
        self.db = request.app.db
        self.auth = request.app.auth
