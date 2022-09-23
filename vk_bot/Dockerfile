FROM python:3.7-slim

WORKDIR /app

COPY req.txt ./

RUN pip3 install -r req.txt --no-cache-dir

COPY ./ ./

CMD ["gunicorn", "vk_bot.wsgi:application", "--bind", "0:8000"]