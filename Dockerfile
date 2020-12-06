
# Use the python 3.8 alpine image container image
FROM python:3.8-alpine3.11

# Set the working directory to /app
WORKDIR /th3pl4gu3

# Copy the current directory contents into the container at /app
ADD . /th3pl4gu3

# Dependencies for uWSGI
RUN apk add python3-dev build-base linux-headers pcre-dev

# Install the dependencies from requirements
RUN pip install -r requirements.txt

# In case bash is needed
#RUN apk add --no-cache bash

# tell the port number the container should expose
EXPOSE 8082

# Run the command
ENTRYPOINT ["uwsgi", "app.ini"]