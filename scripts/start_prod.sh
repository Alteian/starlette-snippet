#!/bin/bash

exec $(which gunicorn) -c /code/config/gunicorn/prod.py src.app:app
