# Use an official Python runtime as a parent image
FROM python:3.9.19-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright and its dependencies
RUN pip install playwright \
    && playwright install --with-deps

# Run test script on container launch
CMD ["pytest", "-v"]
