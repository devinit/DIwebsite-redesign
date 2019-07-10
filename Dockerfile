
FROM alpine:3.10.0
LABEL maintainer="Napho <naphlin.akena@devinit.org>"

RUN apk add  --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/v3.4/main/ nodejs=6.7.0-r1

#WORKDIR /code/patterns
#Compile skelly libary
#COPY ./patterns ./
#RUN npm install
#RUN npm rebuild node-sass
#RUN npm run build

RUN apk add postgresql-client && \
    set -ex \
	&& apk add gcc \
		g++ \
		make \
		libc-dev \
		musl-dev \
		linux-headers \
		pcre-dev \
		postgresql-dev \
		git

RUN apk add python3-dev

RUN apk add --no-cache python3 && \
 if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
 if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi

#Require to compile pygcog2
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache postgresql-dev
RUN apk add --no-cache libmemcached-dev zlib-dev

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev


COPY ./requirements.txt /code/requirements.txt

RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install pip --upgrade \
    && pip install -r /code/requirements.txt \
    && apk del .build-deps

# Copy the current directory contents into the container at /code/
COPY . /code/
# Set the working directory to /code/
WORKDIR /code/

#Install nvm to be used by user wagail
EXPOSE 8090

# start uWSGI, using a wrapper script to allow us to easily add more commands to container startup:
ENTRYPOINT ["/code/docker-entrypoint.sh"]
CMD ["gunicorn","di_website.wsgi:application","--bind","0.0.0.0:8090","--workers","3"]
