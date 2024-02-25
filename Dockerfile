FROM python:3.11


# Copy the application code
COPY . /app

# Set the working directory
WORKDIR /app

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Install Python dependencies
RUN /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install -r requirements.txt

# Set executable permissions for entrypoint script
RUN chmod +x entrypoint.sh

# Set the default command to run the entrypoint script
CMD ["/app/entrypoint.sh"]