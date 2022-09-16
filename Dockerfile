FROM python:3.9

ENV FLASK_PORT 80

RUN apt-get update -y && \
    apt-get -y install  sudo \
                        bmon

RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo

WORKDIR /usr/src/app
ENV BASE_PATH /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ .

ENTRYPOINT waitress-serve --port=$FLASK_PORT --call raspberry_monitor:create_app