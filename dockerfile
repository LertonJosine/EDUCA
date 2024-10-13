FROM python:3.10-slim

WORKDIR /Educa

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

EXPOSE 8000

CMD ["sh", "-c", "RUN python manage.py collectstatic --noinput && python manage.py migrate && gunicorn --bind 0.0.0.0:8000 educa.wsgi:application"]
