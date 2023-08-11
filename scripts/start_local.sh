#!/bin/bash

exec $(which gunicorn) -c /code/config/gunicorn/local.py src.app:app
