# Use the official Python image for version 3.9
FROM python:3.9-alpine

# Set the working directory in the container to /app
WORKDIR /app

# Copy all files from the current directory to /app in the container
COPY . .

# Install the required packages using pip
RUN pip install --no-cache-dir -r requirements.txt

# Run the python script every 15 minutes using cron
RUN echo "*/15 * * * * python3 /app/Scheduler_Function.py" >> /var/spool/cron/crontabs/root

# Run cron in the foreground
CMD ["crond", "-f"]
