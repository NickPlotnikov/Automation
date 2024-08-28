from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from company import get_db
from empl_db import Employee, EmployeeCreate, EmployeeUpdate

app = FastAPI()

@app.get("/employee")
def read_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

@app.post("/employee")
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@app.get("/employee/{id}")
def read_employee(id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.patch("/employee/{id}")
def update_employee(id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.id == id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    for key, value in employee.dict(exclude_unset=True).items():
        setattr(db_employee, key, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee