FROM ubuntu

MAINTAINER ujnamss "ujnamss@gmail.com"

RUN  apt-get update -y && \
     apt-get upgrade -y && \
     apt-get dist-upgrade -y && \
     apt-get -y autoremove && \
     apt-get clean

RUN apt-get install -y python3-pip python3-dev
RUN apt-get install -y locales && locale-gen en_US.UTF-8

ADD install/requirements.txt /app/requirements.txt

RUN python3 -m pip install -Ur /app/requirements.txt

ENV HOME_DIR /homedir
ENV PORT {{PORT}}
ENV PYTHONIOENCODING utf-8
ENV PYTHONUNBUFFERED TRUE
ENV SLACK_API_TOKEN {{slack_api_token}}

WORKDIR $HOME_DIR/{{service_name}}/src

CMD python3 -u app.py
