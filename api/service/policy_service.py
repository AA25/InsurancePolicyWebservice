from sqlalchemy.orm import Session
from api.repository.policy_repository import PolicyRepository
from api.models.policy_models import Policy as PolicyModel, CreatePolicyRequest


# PolicyService class to handle business logic related to policies
class PolicyService:
    def __init__(self, session: Session):
        self.policies_repository = PolicyRepository(session)

    def get_policy_by_policy_number(self, policy_number: int) -> PolicyModel:
        return self.policies_repository.get_policy_by_policy_number(policy_number)

    def get_all_policies(self) -> list[PolicyModel]:
        return self.policies_repository.get_all_policies()

    def create_policy(self, policy_data: CreatePolicyRequest) -> PolicyModel:
        # Convert CreatePolicyRequest to PolicyModel
        policy = PolicyModel(
            policy_holder_id=policy_data.policy_holder_id,
            policy_number=policy_data.policy_number,
            policy_type=policy_data.policy_type,
            policy_start_date=policy_data.policy_start_date,
            policy_end_date=policy_data.policy_end_date,
            status=policy_data.status,
            premium_amount=policy_data.premium_amount,
            currency=policy_data.currency
        )
        return self.policies_repository.create_policy(policy)