from fastapi import APIRouter
from api.router.v1 import policy

# Base API router for version 1
router = APIRouter(
    prefix="/api/v1"
)

router.include_router(policy.router)