# serverless-fastapi
A tiny sample FastAPI app that can be deployed to AWS Lambda. Makes use of Cognito to authenticate requests.

## Prereqs
This demo requires an API Gateway set up w/ a Cognito User Pool.
After deploying this function, add a Resource to your gateway and proxy requests to this function using `/{proxy+}`.

## Getting started
1. Install serverless, Docker, and AWS CLI
2. `nox`
3. `export AWS_ACCESS_KEY_ID=`
4. `export AWS_SECRET_ACCESS_KEY=`
5. `serverless deploy --stage development --region us-east-2`
