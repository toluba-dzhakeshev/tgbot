FROM python:3.10.14
ENV TOKEN='your_token'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "bot.py"]
