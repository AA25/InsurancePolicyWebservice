from pydantic import BaseModel, Field, ConfigDict

# This file contains Pydantic models for policy-related requests and responses

class PolicyResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
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
    )

    policy_number: int = Field(..., description="Policy number associated with the policy")
    policy_type: str = Field(..., description="Type of the insurance policy")
    policy_start_date: str = Field(..., description="Start date of the policy in YYYY-MM-DD format")
    policy_end_date: str = Field(..., description="End date of the policy in YYYY-MM-DD format")
    status: str = Field(..., description="Current status of the policy (e.g., active, expired)")
    premium_amount: float = Field(..., description="Premium amount for the policy")
    currency: str = Field(..., description="Currency of the premium amount, e.g., GBP, USD, EUR")

class CreatePolicyRequest(BaseModel):
    policy_holder_id: int = Field(ge=1, le=3, description="ID of the policy holder")
    policy_number: int = Field(ge=100000, le=199999, description="Policy number associated with the policy")
    policy_type: str = Field(..., description="Type of the insurance policy")
    policy_start_date: str = Field(..., description="Start date of the policy in YYYY-MM-DD format")
    policy_end_date: str = Field(..., description="End date of the policy in YYYY-MM-DD format")
    status: str = Field(..., description="Current status of the policy (e.g., active, expired)")
    premium_amount: float = Field(..., description="Premium amount for the policy")
    currency: str = Field(..., description="Currency of the premium amount, e.g., GBP, USD, EUR")


class Policy(BaseModel):
    policy_number: int = Field(..., description="Policy number associated with the policy")
    policy_type: str = Field(..., description="Type of the insurance policy")
    policy_start_date: str = Field(..., description="Start date of the policy in YYYY-MM-DD format")
    policy_end_date: str = Field(..., description="End date of the policy in YYYY-MM-DD format")
    status: str = Field(..., description="Current status of the policy (e.g., active, expired)")
    premium_amount: float = Field(..., description="Premium amount for the policy")
    currency: str = Field(..., description="Currency of the premium amount, e.g., GBP, USD, EUR")
    created_at: str = Field(..., description="Creation date of the policy in ISO format")
    updated_at: str = Field(..., description="Last update date of the policy in ISO format")