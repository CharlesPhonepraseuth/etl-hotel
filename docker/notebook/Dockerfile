FROM python:3.9-slim

USER root

RUN apt-get update

ADD ./docker/notebook /home/docker

RUN pip install -r home/docker/requirements.txt

WORKDIR /home/app/notebooks

ENTRYPOINT ["jupyter", "notebook", "--allow-root", "--ip=0.0.0.0"]
