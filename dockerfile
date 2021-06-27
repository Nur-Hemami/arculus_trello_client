# set base image (host OS)
FROM python:3.8.2

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY example.csv .
COPY parameters.json .
COPY arculus_client.py .
COPY trello.py .

# command to run on container start
CMD [ "python3", "./arculus_client.py", "docker" ]