FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt update
RUN apt install -y libmagic-dev
RUN groupadd -r deepuser && useradd -r -g deepuser deepuser
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8009
RUN chmod +x entry.sh
ENTRYPOINT ["/app/entry.sh"]
