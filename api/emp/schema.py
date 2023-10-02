from pydantic import BaseModel
 

class User_registration(BaseModel):
    email : str
    username:str
    password:str
    mobile : str
    firstname:str
    lastname : str

    class Config:
        orm_mode = True

class User(BaseModel):
    id : int
    email : str
    username : str
    mobile : str
    firstname : str
    lastname : str

    class Config:
        orm_mode = True

class Login(BaseModel):
    username :str
    password : str

class Employee(BaseModel):
    email : str
    firstname : str
    lastname : str
    salary : str
    contact : str
    bonus : str
    depts_id : int
    role_id : int

    class Config:
        orm_mode = True

class DepartmentDetail(BaseModel):
    id : int
    dept : str
    class Config:
        orm_mode = True

class RoleDetail(BaseModel):
    id : int
    role : str
    class Config:
        orm_mode = True

class EmployeeDetails(BaseModel):
    id : int
    email : str
    firstname : str
    lastname : str
    salary : str
    contact : str
    bonus : str
    depts : DepartmentDetail
    roles : RoleDetail
    class Config:
        orm_mode = True


class UpdateEmployee(BaseModel):
    email : str
    firstname : str
    lastname : str
    salary : str
    contact : str
    bonus : str
    depts_id : int
    role_id : int

    class Config:
        orm_mode = True