from sqlalchemy import create_engine,Column,String,Integer,Float,desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('mysql+pymysql://root:anuj@localhost/anujdb')
DBSession = sessionmaker(bind=engine)

session = DBSession()
class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer,primary_key = True)
    fname = Column(String)
    department = Column(String)
    basic_salary = Column(Float)
    da = Column(Float)
    hra = Column(Float)

'''for i in session.query(Employee).filter(Employee.department=='computer science').all():
    print(i.id,i.fname,i.department)

for i in session.query(Employee).filter(Employee.fname.in_(['anuj','anurag'])).all():
    print(i.id, i.fname, i.department)'''

for i in session.query(Employee).order_by(desc(Employee.hra)).all():
    print(i.id, i.fname, i.department,i.basic_salary,i.da,i.hra)