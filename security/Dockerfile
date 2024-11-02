FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY security_container.py ./

CMD ["python", "security_container.py"]
