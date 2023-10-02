from sqlalchemy import Boolean, Column, Integer, String,DateTime,Date,ForeignKey
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), index=True, nullable=False)
    username = Column(String(50), index=True, nullable=False)
    password = Column(String(512), nullable=False)
    mobile = Column(String(15), nullable=True)
    firstname = Column(String(50), nullable=True)
    lastname = Column(String(50), nullable=True)
    employees = relationship("Employee", back_populates="user")
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
    created_on = Column(DateTime, default=datetime.utcnow)
    updated_on = Column(DateTime, default=datetime.utcnow)

class Department(Base):
    __tablename__ = "depts"

    id = Column(Integer, primary_key=True, index=True)
    dept = Column(String(50),nullable=True)
    employees = relationship("Employee", back_populates="depts")
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
    created_on = Column(DateTime, default=datetime.utcnow)
    updated_on = Column(DateTime, default=datetime.utcnow)


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    role =  Column(String(50),nullable=True) 
    employees = relationship("Employee", back_populates="roles")
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
    created_on = Column(DateTime, default=datetime.utcnow)
    updated_on = Column(DateTime, default=datetime.utcnow)

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), index=True, nullable=False)
    firstname = Column(String(50), nullable=True)
    lastname = Column(String(50), nullable=True)
    salary = Column(String(50), nullable=True)
    contact = Column(String(15), nullable=True)
    bonus = Column(String(50), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User",back_populates="employees")
    depts_id = Column(Integer, ForeignKey("depts.id"))
    depts = relationship("Department",back_populates="employees")
    role_id = Column(Integer, ForeignKey("roles.id"))
    roles = relationship("Role",back_populates=("employees"))
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
    created_on = Column(DateTime, default=datetime.utcnow)
    updated_on = Column(DateTime, default=datetime.utcnow)


