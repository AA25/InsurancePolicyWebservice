# Database entity for insurance policyholders

from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, Date
from api.config.database import Base

class PolicyHolder(Base):
    __tablename__ = "policy_holders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(50),  nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=True)
    email = Column(String(50), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=False)
    address1 = Column(String(50), nullable=False)
    address2 = Column(String(50), nullable=False)
    city = Column(String(100), nullable=False)
    postal_code = Column(String(20), nullable=False)
    country = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))