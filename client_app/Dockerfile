FROM python:3.11

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV TZ=Europe/Moscow

CMD [ "python", "-u", "./main.py" ]
