FROM python:3.11-slim

RUN pip install --upgrade pip setuptools wheel --progress-bar off \
    && pip install --no-cache-dir requests --progress-bar off

WORKDIR /app
COPY test_authentication.py test_authorization.py test_content.py ./

CMD ["python3", "test_authentication.py"]
