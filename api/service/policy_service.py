from sqlalchemy.orm import Session
from api.repository.policy_repository import PolicyRepository
from api.models.policy_models import Policy as PolicyModel

# PolicyService class to handle business logic related to policies
class PolicyService:
    def __init__(self, session: Session):
        self.policies_repository = PolicyRepository(session)

    def get_policy_by_policy_number(self, policy_number: int) -> PolicyModel:
        return self.policies_repository.get_policy_by_policy_number(policy_number)

    def get_all_policies(self) -> list[PolicyModel]:
        return self.policies_repository.get_all_policies()