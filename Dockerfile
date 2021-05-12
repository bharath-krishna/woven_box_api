FROM tiangolo/uvicorn-gunicorn:python3.7

ARG USER=fastapi
ARG GROUP=fastapi

ARG HOME=/home/${USER}
ENV APP_DIR=${HOME}/app
ENV LOCAL_BIN=${HOME}/.local/bin
ENV PATH="${PATH}:${LOCAL_BIN}"
ENV HOST=0.0.0.0
ENV PORT=8080

RUN addgroup --gid 256000 --group ${GROUP}
RUN adduser --uid 22600 --ingroup ${GROUP} --disabled-password fastapi
RUN chown -R ${USER}:${GROUP} ${HOME}

COPY . ${APP_DIR}
RUN chown -R ${USER}:${GROUP} ${APP_DIR}

USER ${USER}
WORKDIR ${APP_DIR}

RUN pip install pipenv setuptools --user
RUN pipenv lock -r | tail -n +2 > requirements.txt
RUN pip install -r requirements.txt --user

RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]