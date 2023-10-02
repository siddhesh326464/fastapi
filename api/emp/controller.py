from fastapi import APIRouter,Depends,HTTPException
from db.deps import get_db,get_current_user_id
from sqlalchemy.orm.session import Session
from api.emp.schema import User_registration,User,Login as login_schema ,Employee,EmployeeDetails,UpdateEmployee
from typing import Any
from api.emp.service import userregister,authenticate_user,create_emp,get_all_emp,get_employee_detail,update_employee,emp_delete
from fastapi_jwt_auth import AuthJWT
router = APIRouter()

@router.post("/register",response_model=User)
def Register(db: Session = Depends(get_db),user_data: User_registration = Depends())->Any:
    """
    Get information for user registration
    """
    user = userregister(email=user_data.email,
                        username=user_data.username,
                        password = user_data.password,
                        mobile = user_data.mobile,
                        first_name = user_data.firstname,
                        last_name = user_data.lastname,
                        db=db)
    return user

@router.post("/login")
def Login(login_data : login_schema,db: Session = Depends(get_db),Authorize: AuthJWT = Depends())->Any:
    """
    This is for authenticate user
    """
    auth_user = authenticate_user(username=login_data.username,
                                  password=login_data.password,
                                  db=db)
    if not auth_user:
        raise  HTTPException(status_code=401,detail="creadentials not found")
    access_token = Authorize.create_access_token(subject=auth_user.username)
    refresh_token = Authorize.create_refresh_token(subject=auth_user.username)
    Authorize.set_access_cookies(access_token)
    Authorize.set_refresh_cookies(refresh_token)
    return {
        "access_token":access_token,
        "refresh_token":refresh_token
    }

@router.post("/emp/create/",response_model= EmployeeDetails)
def CreateEmployee( emp_data:Employee,db:Session = Depends(get_db) ,Authorize: AuthJWT = Depends() ):
    """
    This function is for creating employee
    """
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    current_user_id = get_current_user_id(current_user,db=db)
    emp = create_emp(email = emp_data.email,
                     firstname = emp_data.firstname,
                     lastname = emp_data.lastname,
                     salary = emp_data.salary,
                     contact = emp_data.contact,
                     bonus = emp_data.bonus,
                     user = current_user_id.id,
                     dept = emp_data.depts_id,
                     role = emp_data.role_id,
                     db = db
                     )
    return emp
    

@router.get("/emp/emplist/",response_model=list[EmployeeDetails])
def GetEmployeeList(db:Session = Depends(get_db) ,Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    emp_list = get_all_emp(db=db)
    return emp_list


@router.get("/emp/detail/{emp_id}/",response_model=EmployeeDetails)
def GetEmployeeDetail(emp_id : int ,db:Session =  Depends(get_db) ,Authorize: AuthJWT = Depends()):
    """
    This is to geting information of Employee
    """
    Authorize.jwt_required()
    emp_detail = get_employee_detail(emp_id,
                                     db=db)
    return emp_detail    

@router.put("/emp/update/{emp_id}/",response_model=UpdateEmployee)
def UpdateEmployeeDetail(emp_id : int ,request_data: UpdateEmployee, db:Session =  Depends(get_db) ,Authorize: AuthJWT = Depends()):
    """
    This is to update Employee details 
    """
    Authorize.jwt_required()
    updated_emp = update_employee(emp_id,
                                  request_data,
                                  db=db)
    return updated_emp

@router.delete("/emp/delete/{emp_id}/")
def DeleteEmployee(emp_id : int , db:Session =  Depends(get_db) ,Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    delete_emp = emp_delete(emp_id,
                            db)
    return delete_emp