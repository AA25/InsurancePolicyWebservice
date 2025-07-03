from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session
from api.models.policy_models import PolicyResponse
from api.entities.policy import Policy
from api.models.policy_models import Policy as PolicyModel

# PolicyRepository class to handle database operations related to policies
class PolicyRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_policy_by_policy_number(self, policy_number: int) -> PolicyModel:
        policy = self.db.query(Policy).filter(Policy.policy_number == policy_number).first()
        if not policy:
            raise HTTPException(status_code=404, detail="Policy not found")

        return policy

    def get_all_policies(self) -> List[PolicyModel]:
        policies = self.db.query(Policy).all()
        if not policies:
            raise HTTPException(status_code=404, detail="No policies found")

        return policies