from fastapi import Request


class BaseModule():
    def __init__(self, request: Request) -> None:
        self.request = request
