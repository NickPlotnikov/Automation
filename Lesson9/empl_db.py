from sqlalchemy import Column, Integer, Boolean, String, Timestamp
from company import Base

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    is_active = Column(Boolean, default=True)
    create_timestamp = Column(Timestamp, server_default='now()')
    change_timestamp = Column(Timestamp, server_default='now()', onupdate='now()')
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    middle_name = Column(String(20))
    phone = Column(String(15))
    email = Column(String(256))
    avatar_url = Column(String(1024))
    company_id = Column(Integer, nullable=False)