import logging

from fastapi import APIRouter, status

from app.schemas.greeting import GreetingRequest, GreetingResponse

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/cherries", tags=["greeting"])


@router.put(
    "/greeting",
    response_model=GreetingResponse,
    status_code=status.HTTP_200_OK,
    summary="Submit a greeting message",
)
def put_greeting(payload: GreetingRequest) -> GreetingResponse:
    logger.info(f"Received greeting message {payload.message=}")
    return GreetingResponse(status="ok", echoed=payload.message)
