FROM python:3.10-slim

RUN apt update -y && apt install awscli -y git

# Set the Git executable path for GitPython
ENV GIT_PYTHON_GIT_EXECUTABLE=/usr/bin/git

WORKDIR /app

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Activate the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

COPY . /app
RUN pip install -r requirements.txt

EXPOSE 8080

CMD python app.py