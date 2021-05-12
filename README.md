# FastAPI framework
## Boilerplate code

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

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

You can use below JWT tokens to authorize in Swagger specs.

```
JWT Tokens

Bharath

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkJoYXJhdGgiLCJpZCI6InNxTDFPSkRubmNxTkVGV1lTeEFaIiwiaWF0IjoxNjE5NTA1ODIxLCJleHAiOjE2MjA1MDU4MjF9.x49Wt89fod751sIahASYTu6XKPRlhJlqNl0i18t4qFU


Sanjay

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IlNhbmpheSIsImlkIjoialo5MkozaE5nQVNlMnVSRENCUW4iLCJpYXQiOjE2MTk1MDU4MjEsImV4cCI6MTYyMDUwNTgyMX0.oDimnvv40Ji7sWevG2ah-8OKF1Vn0kcODrbrqAL1ldI


Anitha

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFuaXRoYSIsImlkIjoidG9DR1hBUEFySHZuQzg1NzVqYzQiLCJpYXQiOjE2MTk1MDU4MjEsImV4cCI6MTYyMDUwNTgyMX0.7cHKuujHPm2_LevQBReGKfTcipEes8twZ4B4PR6kgkA

```
These tokens are valid till 9 May 05:30 GMT, you can regenerate token by modifying "exp" in payload for testing purposes.


## How to stop and remove

```bash
> docker stop fastapi_backend
> docker rm fastapi_backend
```

### END


