from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.config.database import get_db
from api.models.policy_models import PolicyResponse
from api.service.policy_service import PolicyService
from api.models.policy_models import Policy as PolicyModel, CreatePolicyRequest

# Policy router to handle policy-related endpoints

router = APIRouter(
    prefix="/policies",
    tags=["policies"]
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/{policy_number}", status_code=200, response_model=PolicyResponse)
def get_policy_by_number(policy_number: int, db: db_dependency):
    policy: PolicyModel = PolicyService(db).get_policy_by_policy_number(policy_number)

    policy_response = policy.__dict__.copy()

    # Convert date fields to ISO strings - Preferably we'd do elsewhere e.g. in a Factory
    if "policy_start_date" in policy_response and policy_response["policy_start_date"]:
        policy_response["policy_start_date"] = policy_response["policy_start_date"].isoformat()
    if "policy_end_date" in policy_response and policy_response["policy_end_date"]:
        policy_response["policy_end_date"] = policy_response["policy_end_date"].isoformat()

    return PolicyResponse(**policy_response)

@router.get("/", status_code=200, response_model=list[PolicyResponse])
def get_all_policies(db: db_dependency):
    policies: List[PolicyModel] = PolicyService(db).get_all_policies()

    # Convert each policy's date fields to ISO strings and create PolicyResponse objects
    policies_response: List[Policy] = []
    for policy in policies:
        data = policy.__dict__.copy()
        if "policy_start_date" in data and data["policy_start_date"]:
            data["policy_start_date"] = data["policy_start_date"].isoformat()
        if "policy_end_date" in data and data["policy_end_date"]:
            data["policy_end_date"] = data["policy_end_date"].isoformat()
        policies_response.append(PolicyResponse(**data))

    return policies_response

@router.post("/", status_code=201, response_model=PolicyResponse)
def post_policy(policy_request: CreatePolicyRequest, db: db_dependency):
    return PolicyService(db).create_policy(policy_request)
