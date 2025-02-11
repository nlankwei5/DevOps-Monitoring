# 1. Use Ubuntu as the base image
FROM ubuntu:latest  

# Install cron
RUN apt-get update && apt-get install -y cron

# 2. Copy the Bash script into the container
COPY ../bash_scripts/monitor.sh /monitor.sh

# 3. Give the script execution permissions
RUN chmod +x /monitor.sh  

# 4. Run the script when the container starts
CMD ["/monitor.sh"]  

