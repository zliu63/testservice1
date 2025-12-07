import logging

from fastapi import APIRouter, HTTPException, status

from app.schemas.greeting import GreetingRequest, GreetingResponse
from chelsydb import insert_data

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
    try:
        new_id = insert_data(payload.message)
        logger.info("Inserted greeting into testtbl1", extra={"id": new_id})
    except Exception as exc:  # pragma: no cover - integration error path
        logger.exception("Failed to insert greeting into testtbl1")
        raise HTTPException(status_code=500, detail="Failed to persist greeting") from exc

    return GreetingResponse(status="ok", echoed=payload.message)
