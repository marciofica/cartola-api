FROM python:3
ENV PYTHONUNBUFFERED 1
RUN echo "America/Sao_Paulo" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata
RUN mkdir /code
WORKDIR /code
ADD /config/requirements.pip /code/
RUN pip install -r requirements.pip
ADD . /code/