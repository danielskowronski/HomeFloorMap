FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
    FLASK_ENV=production \
    FLASK_APP=app.py

RUN addgroup --system webgroup && adduser --system webuser --ingroup webgroup

WORKDIR /app
COPY ./app /app
RUN chown -R webuser:webgroup /app
RUN pip install --no-cache-dir -r requirements.txt
USER webuser

EXPOSE 9002

CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:9002", "app:app"]
