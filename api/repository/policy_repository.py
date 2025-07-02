from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session
from api.models.policy_models import PolicyByPolicyNumberResponse, PolicyResponse
from api.entities.policy import Policy

# PolicyRepository class to handle database operations related to policies
class PolicyRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_policy_by_policy_number(self, policy_number: int) -> PolicyByPolicyNumberResponse:
        policy = self.db.query(Policy).filter(Policy.policy_number == policy_number).first()
        if not policy:
            raise HTTPException(status_code=404, detail="Policy not found")

        data = policy.__dict__.copy()

        # Convert date fields to ISO strings - Preferably we'd do elsewhere e.g. in a Factory
        if "policy_start_date" in data and data["policy_start_date"]:
            data["policy_start_date"] = data["policy_start_date"].isoformat()
        if "policy_end_date" in data and data["policy_end_date"]:
            data["policy_end_date"] = data["policy_end_date"].isoformat()

        return PolicyByPolicyNumberResponse(**data)

    def get_all_policies(self) -> List[PolicyResponse]:
        policies = self.db.query(Policy).all()
        if not policies:
            raise HTTPException(status_code=404, detail="No policies found")

        # Convert each policy's date fields to ISO strings and create PolicyResponse objects
        result: List[PolicyResponse] = []
        for policy in policies:
            data = policy.__dict__.copy()
            if "policy_start_date" in data and data["policy_start_date"]:
                data["policy_start_date"] = data["policy_start_date"].isoformat()
            if "policy_end_date" in data and data["policy_end_date"]:
                data["policy_end_date"] = data["policy_end_date"].isoformat()
            result.append(PolicyResponse(**data))
        return result