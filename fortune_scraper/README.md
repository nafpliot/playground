# Fortune of the Day Scraper

The system fetches a random quote from a JSON url every 10 seconds and displays it in a HTML page.

It consists of two dockerized apps. The scraper, which is a Flask app with a 10 second scheduled job fetching the quotes, and the server, which is a Nginx reverse proxy pointing to the scraper in order to server the data as HTML.

The environment can be easily deployed with docker compose `docker-compose up -d`

# Extra Info

The scraper misses some error handling. ¯\\_(ツ)_/¯

The system can run on Amazon ECS or any other cloud platform. A typical case could be to deploy the Nginx reverse proxy container in front of the application container. In case of multiple copies of the stack we can also have a load balancer at the very front (probably sticky sessions make sense in out case).

Provisioning could be done on ECS using a CloudFormation template (ToDo) or some other tool like Terraform. For monitoring we have again many options from Amazon CloudWatch to other services like Promitheus.

There are alternative ways for this system to be developed and deployed, one of them could be:
- Run the scraper job on AWS Lambda (if the job didn't need to run every 10 seconds - because Lambda's minimum rate is 1 minute), then the result could be written, for example, in S3 or DynamoDB (free tier in this case). The server could read the values from DynamoDB. This however changes the concept and implies that the quote will be the same to all our visitors.