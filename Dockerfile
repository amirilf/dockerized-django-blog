FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ARG USER_ID=1000
ARG GROUP_ID=1000
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code