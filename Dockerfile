FROM python:3

WORKDIR /opt/tornado_skillup_proj

ADD . /opt/tornado_skillup_proj
RUN pip install --no-cache-dir -r requirements.txt
