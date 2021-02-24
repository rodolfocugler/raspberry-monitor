FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ .

CMD ["waitress-serve", "--port=80", "--call",  "raspberry_monitor:create_app"]