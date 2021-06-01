ARG BASE_IMAGE
FROM ${BASE_IMAGE}

WORKDIR /app

RUN apt-get update
RUN apt-get install vim -y
RUN apt-get install gcc python3-dev -y
COPY requirements.txt src/
RUN apt-get install python3-pip -y
RUN pip3 install --upgrade setuptools
RUN pip3 install -r src/requirements.txt

COPY src /app/src
COPY tests /app/tests
COPY src/entrypoint.sh /app


ENV PYTHONPATH /app/src


RUN ["chmod", "+x", "/app/entrypoint.sh"]
ENTRYPOINT ["bash", "/app/entrypoint.sh"]
