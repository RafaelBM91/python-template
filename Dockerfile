FROM    python:3
WORKDIR /var/src
COPY    requirements.txt ./
RUN     pip install -r requirements.txt
