# Serverless GitHub IP Grab

This example app which runs on Amazon Lambda gets all GitHub ips and stores them with a timestamp in a JSON document on Amazon S3.

The Lambda job is configured to run every 1 hour to update the JSON document.

Tools used: Serverless Framework + Localstack (for local tests).

## Extra Info

AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY need to be defined as env variables. For tests on localstack these can be random values.