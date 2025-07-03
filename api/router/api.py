from fastapi import APIRouter
from api.router.v1 import policy_controller

# Base API router for version 1
router = APIRouter(
    prefix="/api/v1"
)

router.include_router(policy_controller.router)