from fastapi import APIRouter, Response, status


health_router = APIRouter()


@health_router.get(
    path="/",
    response_model=Response,
    status_code=status.HTTP_200_OK,
)
def health():
    return Response(content="Server is running", status_code=status.HTTP_200_OK)
