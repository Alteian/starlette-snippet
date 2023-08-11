#!/bin/bash

exec $(which gunicorn) -c /code/config/gunicorn/dev.py src.app:app
