import os
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'

import unittest
from unittest.mock import MagicMock
from api.service.policy_service import PolicyService
from api.models.policy_models import Policy

class TestPolicyService(unittest.TestCase):
    def setUp(self):
        self.mock_repository = MagicMock()
        self.service = PolicyService.__new__(PolicyService)
        self.service.policies_repository = self.mock_repository

    def test_get_policy_by_policy_number(self):
        # Arrange
        mock_policy = self.get_mock_policy()
        self.mock_repository.get_policy_by_policy_number.return_value = mock_policy

        # Act
        result = self.service.get_policy_by_policy_number(123)

        # Assert
        self.mock_repository.get_policy_by_policy_number.assert_called_once_with(123)
        self.assertEqual(result, mock_policy)

    def get_mock_policy(self) -> Policy:
        return Policy(
            policy_number=123,
            policy_type="Home Insurance",
            policy_start_date="2023-01-01",
            policy_end_date="2024-01-01",
            status="active",
            premium_amount=250.00,
            currency="GBP",
            created_at="2023-01-01T00:00:00",
            updated_at="2023-01-01T00:00:00"
        )
