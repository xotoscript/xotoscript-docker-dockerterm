# multi-stage docker build for tests

################################
# stage 1: build the dockerterm_dockerterm image (if not already available)
################################

FROM dockerterm_dockerterm as base

# no need to do anything here, as the image is already built in the previous step
# this stage will only run if the `dockerterm_dockerterm` image is not available locally

################################
# stage 2: build the test container
################################

FROM base

# copy the test files to the container
COPY . /app

# install dependencies (including pytest)
RUN pip install pytest pytest-docker-tools pytest-testinfra

# set the working directory
WORKDIR /app

# set the permissions to full access for the /app folder
RUN sudo chown -R 1000:1000 /app

# switch to a non-root user
USER 1000

CMD ["sh", "-c", "python3 -m pytest ./tests/*"]
