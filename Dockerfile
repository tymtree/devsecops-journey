FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip setuptools

RUN python -m pip install --no-cache-dir -r requirements.txt

RUN python -m pip install --upgrade msgpack

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]