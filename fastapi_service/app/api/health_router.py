from fastapi import APIRouter, status
from app.schemas.responses import Response

health_router = APIRouter()


@health_router.get(
    path="/",
    response_model=Response,
    status_code=status.HTTP_200_OK,
)
def health():
    return Response(message="Server is running", status_code=status.HTTP_200_OK)
