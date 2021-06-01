# Woven Box
## Backend APIs

[![Build Status](https://travis-ci.com/bharath-krishna/woven-box_api.svg?branch=master)](https://travis-ci.com/github/bharath-krishna/woven-box_api)

This is a [FastAPI](https://fastapi.tiangolo.com/) project.

## Getting Started

First, run the development server:

```bash
> pipenv shell
> pipenv install
> ./scripts/run_uvicorn.sh
```

Open [http://localhost:8088/apidocs](http://localhost:8088/apidocs) with your browser to see the result.

API routes can be accessed as [http://localhost:8088/api/profile](http://localhost:3000/api/profile).


## Deploy using docker (Recommended)
Application runs with default configs you can modity below by passing environment variables.

Firebase service account details are base64 encoded from a secrets.json file to a token string (API_FIREBASE_CONFIGS). This needs to passed via env vars also.


```bash
> docker build -t woven_box_api .
> docker run -d --name woven_box_api -p 8088:8088 woven_box_api
```

and access [http://localhost:8088/apidocs](http://localhost:8088/apidocs) for Swagger specs page.

The app uses default configs but can be passed from docker run command. The default env vars are as below

Field | Value
--- | ---
API_PREFIX | /api
API_HOST | 0.0.0.0
API_PORT | 8088
API_LOG_LEVEL | debug
API_WORKERS | 4
API_RELOAD | True
API_ACCESS_LOG | True
API_DEBUG | True
API_FIREBASE_CONFIGS | None
API_SIGNATURE_TEXT | somesecret
API_STORAGE_PATH | ~/woven_box_storage


## How to stop and remove

```bash
> docker stop woven_box_api
> docker rm woven_box_api
```

### END


