from sqlalchemy.orm.session import Session
from models import User,Employee,Role,Department
from utils.security import get_password_hash,verify_password
from fastapi import HTTPException
from typing import Optional
from config import settings
def userregister(email:str,
                 username:str,
                 password:str,
                 mobile:str,
                 first_name:str,
                 last_name:str,
                 db:Session):
    hash_password = get_password_hash(password)
    user = db.query(User).filter(User.email == email).first()
    if user is not None:
        raise HTTPException(status_code=403,detail=settings.MSG_DATA_EXISTS)
    user_info  = User(email = email,
                      username = username,
                      password = hash_password,
                      mobile = mobile,
                      firstname = first_name,
                      lastname = last_name)
    db.add(user_info)
    db.commit()
    db.refresh(user_info)
    return user_info


def authenticate_user(username:str,password:str,db:Session)->Optional[User]:

    user = db.query(User).filter(User.username == username).first()
    if not user:
        return None
    if not verify_password(password,user.password):
        return None
    return user

def create_emp(email,
               firstname,
               lastname,
               salary,
               contact,
               bonus,
               user,
               dept,
               role,
               db:Session):
    dept = db.query(Department).filter(Department.id == dept).first()
    if not dept:
        raise HTTPException(status_code=403,detail=settings.MSG_DATA_DEPT_EXISTS)
    role = db.query(Role).filter(Role.id == role).first()
    if not role:
         raise HTTPException(status_code=403,detail=settings.MSG_DATA_EXISTS)
    emp_info = Employee(email = email,
                        firstname = firstname,
                        lastname = lastname,
                        salary = salary,
                        contact = contact,
                        bonus = bonus,
                        user_id = user,
                        depts_id = dept.id,
                        role_id = role.id,
                        created_by = user
                        )
    db.add(emp_info)
    db.commit()
    db.refresh(emp_info)
    return emp_info

def get_all_emp(db:Session):
    get_emps = db.query(Employee).all()
    return get_emps
    
def get_employee_detail(emp_id,db:Session):
    emp_detail = db.query(Employee).filter(Employee.id == emp_id).first()
    if not emp_detail:
        raise HTTPException(status_code=403,detail="Employee for this id does not exist")
    return emp_detail

def update_employee(emp_id,data,db:Session):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    emp.email = data.email
    emp.firstname = data.firstname
    emp.lastname = data.lastname
    emp.salary = data.salary
    emp.contact = data.contact
    emp.bonus = data.bonus
    emp.depts_id = data.depts_id 
    emp.role_id = data.role_id    
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return (emp)
    
def emp_delete(emp_id,
               db:Session):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    db.delete(emp)
    db.commit()
    return []