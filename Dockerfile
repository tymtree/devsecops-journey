FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .

RUN python -m pip install --no-cache-dir --upgrade pip setuptools msgpack

#RUN python -m pip install --upgrade pip setuptools

RUN python -m pip install --no-cache-dir -r requirements.txt

RUN python -m pip install --upgrade msgpack

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]