FROM python:3.8-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apk update && apk add curl
COPY . .

CMD [ "python", "./app.py" ] 