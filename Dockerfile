FROM python:3.8-slim

# Install the required libraries and cron
RUN apt-get update && apt-get install -y cron
RUN pip install requests

# Set the working directory to the app directory
WORKDIR /app

# Copy the application code to the container
COPY main.py /app/main.py

# copy the crontab configuration and make it executable
COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab

# run crond as main process of container
CMD ["cron", "-f"]
