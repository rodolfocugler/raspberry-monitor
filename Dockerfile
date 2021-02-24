FROM python:3.9

ENV FLASK_PORT 80

RUN apt-get update -y && \
    apt-get install bmon

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ .

CMD ["waitress-serve", "--port=$FLASK_PORT", "--call",  "raspberry_monitor:create_app"]