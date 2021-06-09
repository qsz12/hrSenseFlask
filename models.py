import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Boolean,Float

Base=declarative_base()

class Employee(Base):
    __tablename__='Employee'

    id=Column('id',Integer, primary_key=True)
    title = Column('title',String(50))
    department=Column('department',String(50))
    country=Column('country',String(20))
    state=Column('state',String(20))
    city=Column('city',String(20))
    remote=Column('remote',Boolean)
    description=Column('description',String(500))
    requirements=Column('requirements',String(500))
    benifits=Column('benifits',String(500))
    company_industry=Column('company_industry',String(100))
    job_function=Column('job_function',String(100))
    employment_type=Column('employment_type',String(100))
    experience=Column('experience',Float)
    education=Column('education',String(100))
    keywords=Column('keywords',String(200))
    salary_from=Column('salary_from',Integer)
    salary_to=Column('salary_to',Integer)
    currency=Column('currency',String(50))