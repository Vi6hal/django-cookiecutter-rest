from python:3.11-bullseye

# Section 2- Python Interpreter Flags
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


ARG DEF_DB_URL
ENV DATABASE_URL $DEF_DB_URL
ENV WORKERS 4
ENV PORT 8000


COPY . /opt/data
RUN ls
COPY requirements.txt /tmp/requirements.txt
WORKDIR /opt/data/app
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
RUN \
    python manage.py makemigrations && \
    python manage.py migrate --no-input && \
    python manage.py collectstatic --no-input
RUN chmod +x ../entrypoint.sh
EXPOSE $PORT
CMD ["../entrypoint.sh"]
