FROM python:3.6

LABEL maintainer="thePrince"

######################
# Install Dependencies
######################
COPY requirements.txt /req/
RUN cd /req; pip install -r requirements.txt

######################
# Install Application
######################
COPY app/ /app

#######################################
# Set Application Environment Variables
#######################################
ENV PYTHONPATH=/app

###############
# Run Container
###############
CMD [ "sh", "/app/run.sh" ]