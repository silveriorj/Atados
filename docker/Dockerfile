FROM python:3.8-slim

RUN python -V  && \
	pip install flake8 pytest pylint pytest-cov

RUN npm install -g serverless

WORKDIR /usr/src/app

# RUN serverless plugin install -n serverless-python-requirements.txt

