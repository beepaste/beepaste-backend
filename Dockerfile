FROM python:3.6

# RUN git clone https://github.com/beepaste/beepaste-backend.git /beepaste
COPY beepaste /beepaste/beepaste
COPY config /beepaste/config
COPY requirements /beepaste/requirements
COPY run.py /beepaste/run.py

WORKDIR /beepaste

RUN pip install -r requirements/requirements-dev.txt

VOLUME ["/beepaste/config"]

CMD ["python", "./run.py"]
