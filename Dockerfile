FROM python:3-onbuild

RUN apt-get update && apt-get install -y \
    rsyslog

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR scripts
ENTRYPOINT ["python", "main.py"]