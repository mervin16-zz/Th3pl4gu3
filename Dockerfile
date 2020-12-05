
# Use the python 3.8 alpine image container image
FROM python:3.8-alpine

# Set the working directory to /app
WORKDIR /th3pl4gu3

# Copy the current directory contents into the container at /app
ADD . /th3pl4gu3

# Install the dependencies
RUN pip install -r requirements.txt

# tell the port number the container should expose
EXPOSE 8082

#Later change to WSGI
# run the command
ENTRYPOINT ["python", "run.py"]