FROM python:3.10.1-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY data_chunking.py .

CMD [ "python", "data_chunking.py" ]