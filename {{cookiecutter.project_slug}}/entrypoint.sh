#!/bin/sh
gunicorn smp_core.wsgi -b :$PORT -w $WORKERS
