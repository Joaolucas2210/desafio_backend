FROM python:3.11.6-alpine3.18

COPY . .
RUN pip install --upgrade pip

RUN pip install  --no-cache-dir -r requirements.txt

CMD ["python","-u", "main.py"]