FROM python:3.9-slim

WORKDIR /code

ADD ./app/src/utils /code/src/utils
ADD ./app/src/sql_scripts /code/src/sql_scripts
ADD ./app/dashboard /code/dashboard

ADD ./docker/dashboard /code/docker
RUN pip install -r docker/requirements.txt

RUN touch __init__.py

ENV PYTHONPATH=$PYTHONPATH/code

ENTRYPOINT ["python"]
CMD ["dashboard/index.py"]
