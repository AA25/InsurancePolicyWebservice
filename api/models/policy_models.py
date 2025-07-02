from pydantic import BaseModel, Field

# This file contains Pydantic models for policy-related requests and responses

class PolicyByPolicyNumberRequest(BaseModel):
    policy_number: int = Field(min_length=1, max_length=10, description="Policy number must be between 1 and 10 digits long")

class PolicyByPolicyNumberResponse(BaseModel):
    policy_number: int = Field(..., description="Policy number associated with the policy")
    policy_type: str = Field(..., description="Type of the insurance policy")
    policy_start_date: str = Field(..., description="Start date of the policy in YYYY-MM-DD format")
    policy_end_date: str = Field(..., description="End date of the policy in YYYY-MM-DD format")
    status: str = Field(..., description="Current status of the policy (e.g., active, expired)")
    premium_amount: float = Field(..., description="Premium amount for the policy")
    currency: str = Field(..., description="Currency of the premium amount, e.g., GBP, USD, EUR")

    # special inner class used by Pydantic to configure the behavior of the PolicyByPolicyNumberResponse model
    class Config:
        # it tells Pydantic that it should be able to create an instance of PoliciesResponse
        # directly from an ORM model instance (e.g., an instance of your SQLAlchemy Policies class).
        orm_mode = True
        # for swagger
        schema_extra = {
            "example": {
                "id": 1,
                "policy_holder_id": 101,
                "policy_number": 1234567890,
                "policy_type": "Home Insurance",
                "policy_start_date": "2023-01-01",
                "policy_end_date": "2024-01-01",
                "status": "active",
                "premium_amount": 250.00,
                "currency": "GBP"
            }
        }

class PolicyResponse(BaseModel):
    policy_number: int = Field(..., description="Policy number associated with the policy")
    policy_type: str = Field(..., description="Type of the insurance policy")
    policy_start_date: str = Field(..., description="Start date of the policy in YYYY-MM-DD format")
    policy_end_date: str = Field(..., description="End date of the policy in YYYY-MM-DD format")
    status: str = Field(..., description="Current status of the policy (e.g., active, expired)")
    premium_amount: float = Field(..., description="Premium amount for the policy")
    currency: str = Field(..., description="Currency of the premium amount, e.g., GBP, USD, EUR")

    class Config:
        # it tells Pydantic that it should be able to create an instance of PoliciesResponse
        # directly from an ORM model instance (e.g., an instance of your SQLAlchemy Policies class).
        orm_mode = True
        # for swagger
        schema_extra = {
            "example": {
                "id": 1,
                "policy_holder_id": 101,
                "policy_number": 1234567890,
                "policy_type": "Home Insurance",
                "policy_start_date": "2023-01-01",
                "policy_end_date": "2024-01-01",
                "status": "active",
                "premium_amount": 250.00,
                "currency": "GBP"
            }
        }