from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from company import Base
from pydantic import BaseModel
from datetime import datetime

class Employee(Base):
    __tablename__ = 'employee'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    is_active = Column(Boolean, default=True)
    create_timestamp = Column(TIMESTAMP, server_default='now()')
    change_timestamp = Column(TIMESTAMP, server_default='now()', onupdate='now()')
    first_name = Column(String(20))
    last_name = Column(String(20))
    middle_name = Column(String(20))
    phone = Column(String(15))
    email = Column(String(256))
    avatar_url = Column(String(1024))
    company_id = Column(Integer, ForeignKey('company.id'))

    company = relationship("Company")

class EmployeeCreate(BaseModel):
    is_active: bool
    first_name: str
    last_name: str
    middle_name: str
    phone: str
    email: str
    avatar_url: str
    company_id: int

class EmployeeUpdate(BaseModel):
    is_active: bool = None
    first_name: str = None
    last_name: str = None
    middle_name: str = None
    phone: str = None
    email: str = None
    avatar_url: str = None
    company_id: int = None