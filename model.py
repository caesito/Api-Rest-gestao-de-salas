from sqlalchemy import ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import DateTime
import datetime

USUARIO="root"
SENHA=""
HOST="localhost"
BANCO="Escola"
PORT="3306"

CONNECT=f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

engine=create_engine(CONNECT, echo=True)
Session=sessionmaker(bind=engine)
session=Session()
Base=declarative_base()

class Classroom(Base):
    __tablename__="Classroom"
    id=Column(Integer,primary_key=True)
    name=Column(String(50))
    describe=Column(String(100))

class Schedule(Base):
    __tablename__="Schedule"
    id=Column(Integer,primary_key=True)
    id_classroom=Column(Integer,ForeignKey('Classroom.id'))
    party=Column(String(50))
    date=Column(DateTime)
    time_start=Column(DateTime)
    time_end=Column(DateTime)


Base.metadata.create_all(engine)