from sqlalchemy import create_engine, Column, Integer, Boolean, String, Timestamp
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, index=True)
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

Base.metadata.create_all(bind=engine)