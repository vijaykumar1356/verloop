FROM python:3.10-slim
WORKDIR /code
COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src ./src
COPY ./.env ./
# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"] to run without docker-compose as an indepedent service