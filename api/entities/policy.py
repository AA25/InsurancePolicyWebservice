# Database entity for insurance policies

from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, ForeignKey, Date
from api.config.database import Base

class Policy(Base):
    __tablename__ = "policies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    policy_holder_id = Column(Integer, ForeignKey('policy_holders.id'), nullable=False)
    policy_number = Column(Integer, nullable=False)
    policy_type = Column(String(50),  nullable=False) # Update to "class"
    policy_start_date = Column(Date, nullable=False)
    policy_end_date = Column(Date, nullable=False)
    status = Column(String(20), nullable=False)
    premium_amount = Column(DECIMAL(10,2), nullable=False)
    currency = Column(String(3), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))