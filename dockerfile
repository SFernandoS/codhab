FROM python:3.11

RUN apt-get update

WORKDIR /codhab

COPY . /codhab

RUN chmod -R 666 /codhab

RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /codhab/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]