from fastapi import FastAPI
from mangum import Mangum
from starlette.requests import Request

app = FastAPI()


@app.get("/health")
def root() -> dict:
    return {"status": "ok"}


@app.get("/me")
def get_me(request: Request) -> dict:
    event = request.scope["aws.event"]
    authorizer = event["requestContext"]["authorizer"]["claims"]

    return {
        "name": authorizer["name"],
        "email": authorizer["email"],
        "phone_number": authorizer["phone_number"],
    }


handler = Mangum(app)
