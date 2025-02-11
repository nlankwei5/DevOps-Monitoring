# 1. Use Ubuntu as the base image
FROM ubuntu:latest  

# Install cron
RUN apt-get update && apt-get install -y cron

# 2. Copy the Bash script into the container
COPY ../bash_scripts/monitor.sh /monitor.sh

# 3. Give the script execution permissions
RUN chmod +x /monitor.sh  

# Add crontab for root inside the Docker container
RUN echo "0 */4 * * * /workspace/Automated-System-Monitoring-/Monitor.sh 1>>/var/log/monitor.log 2>&1" | crontab -

# Start cron in the foreground
CMD cron -f
