# Woven Box
## Backend APIs

[![Build Status](https://travis-ci.com/bharath-krishna/woven-box_api.svg?branch=master)](https://travis-ci.com/github/bharath-krishna/woven-box_api)

This is a [FastAPI](https://fastapi.tiangolo.com/) project.

## Getting Started

First, run the development server:

```bash
> pipenv shell
> pipenv install
```

Open [http://localhost:8088/apidocs](http://localhost:8088/apidocs) with your browser to see the result.

API routes can be accessed as [http://localhost:8088/api/profile](http://localhost:3000/api/profile).


## Deploy using docker (Recommended)
Application runs with default configs you can modity below by passing environment variables.

Firebase service account details are base64 encoded from a secrets.json file to a token string (API_FIREBASE_CONFIGS). This needs to passed via env vars also.


```bash
> docker build -t fastapi_backend .
> docker run -d --name fastapi_backend -p 8088:8088 fastapi_backend
```

and access [http://localhost:8088/apidocs](http://localhost:8088/apidocs) for Swagger specs page.


## How to stop and remove

```bash
> docker stop fastapi_backend
> docker rm fastapi_backend
```

### END


