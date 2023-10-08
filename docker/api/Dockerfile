FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

ADD ./app/src/utils /code/src/utils
ADD ./app/src/sql_scripts /code/src/sql_scripts
ADD ./app/api /code/api

COPY ./docker/api /code/docker
RUN pip install -r docker/requirements.txt

RUN touch __init__.py

WORKDIR /code/api

ENV PYTHONPATH=$PYTHONPATH/code

CMD ["uvicorn", "router:app", "--reload",  "--host", "0.0.0.0"]
