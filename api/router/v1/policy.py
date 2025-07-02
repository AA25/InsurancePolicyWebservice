from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.config.database import get_db
from api.models.policy_models import PolicyByPolicyNumberResponse, PolicyResponse
from api.service.policy_service import PolicyService

# Policy router to handle policy-related endpoints

router = APIRouter(
    prefix="/policy",
    tags=["policy"]
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/{policy_number}", status_code=200, response_model=PolicyByPolicyNumberResponse)
def get_policy_by_number(policy_number: int, db: db_dependency):
    return PolicyService(db).get_policy_by_policy_number(policy_number)

@router.get("/", status_code=200, response_model=list[PolicyResponse])
def get_all_policies(db: db_dependency):
    return PolicyService(db).get_all_policies()