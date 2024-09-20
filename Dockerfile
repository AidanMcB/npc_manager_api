# Use a base Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install system dependencies required for psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt --verbose

# Copy the rest of the application code
COPY . /app

# Expose port 5000
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=npc_manager
ENV FLASK_ENV=development

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
