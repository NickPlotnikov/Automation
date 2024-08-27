from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from company import SessionLocal
from empl_db import Employee

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/employee")
def read_employees(db: Session = Depends(get_db)):
    return db.query(Employee).filter(Employee.is_active == True).all()

@app.post("/employee")
def create_employee(employee: Employee, db: Session = Depends(get_db)):
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

@app.get("/employee/{id}")
def read_employee(id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == id, Employee.is_active == True).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.patch("/employee/{id}")
def update_employee(id: int, employee: Employee, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.id == id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    for key, value in employee.dict().items():
        setattr(db_employee, key, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee