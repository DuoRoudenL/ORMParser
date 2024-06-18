FROM python:3.12-bullseye

WORKDIR /main

COPY requirements.txt /main/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /main

ENTRYPOINT ["python", "main.py"]