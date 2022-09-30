FROM python:3.10-alpine

WORKDIR /app

COPY ./ /app

RUN apk add --no-cache gcc musl-dev linux-headers libffi-dev
RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]
