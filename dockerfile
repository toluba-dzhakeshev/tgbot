FROM python:3.10.14
ENV TOKEN='7097714679:AAE3zeahk7rbiKZJobMJmkM3tLvoa4ZD1Gs'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "bot.py"]
