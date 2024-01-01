FROM python:3.11

# Install unzip
RUN apt-get update && apt-get install -y unzip

WORKDIR /app

COPY Pipfile Pipfile.lock app.py calibrated_classifier.zip /app/

RUN unzip calibrated_classifier.zip

# Install project dependencies
RUN pip install pipenv
RUN pipenv install

## Expose the port that the Flask app runs on
EXPOSE 8080

## Run the Flask app
CMD ["pipenv", "run", "python", "app.py"]