FROM python:3.10.1-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY web_scraping.py .

CMD [ "python", "web_scraping.py" ]