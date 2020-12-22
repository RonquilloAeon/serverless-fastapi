from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from mangum import Mangum
from starlette.requests import Request

app = FastAPI()


@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


@app.middleware("http")
async def get_claims(request: Request, call_next):
    try:
        ctx = request.scope["aws.event"].get("requestContext")
        request.state.claims = ctx["authorizer"]["claims"]
    except KeyError:
        return JSONResponse(
            status_code=422,
            content={"message": "Missing authorization claims"},
        )
    else:
        return await call_next(request)


@app.get("/health")
def root() -> dict:
    return {"status": "ok"}


@app.get("/me")
def get_me(request: Request) -> dict:
    claims = request.state.claims

    return {
        "id": claims["cognito:username"],
        "name": claims["name"],
        "email": claims["email"],
        "phone_number": claims["phone_number"],
    }


handler = Mangum(app)
