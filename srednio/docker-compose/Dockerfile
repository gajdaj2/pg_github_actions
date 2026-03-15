FROM python:3.12-slim

WORKDIR /app

COPY srednio/kontenery/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY srednio/kontenery/app.py ./app.py
COPY srednio/kontenery/tests ./tests

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

