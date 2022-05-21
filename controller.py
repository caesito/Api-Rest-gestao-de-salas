from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Classroom, Schedule, CONNECT

def db_connect():
    engine=create_engine(CONNECT, echo=True)
    Session=sessionmaker(bind= engine)
    return Session()

class ControllerClassroom:

    @classmethod
    def add_classroom(cls,name: str,describe:str):
        if cls.verify_exist_classroom(name):
            try:
                session=db_connect()
                session.add(Classroom(name=name, describe=describe))
                session.commit()  
                return {'status code': 200, 'message': f'sala {name} adicionada com sucesso'}
            except Exception as error:
                print('Ocorreu um erro: ', error)
        else:
            return {'warning': f'sala {name} ja existe, não foi possivel adicionar!'}

    @classmethod       
    def verify_exist_classroom(cls,name: str):
        try:
            session=db_connect()
            query=session.query(Classroom).filter(Classroom.name==name).all()
            if len(query) == 0:
                return True
            else:
                return False
        except Exception as error:
            return {'message error': error}

    @classmethod
    def list_of_classroom(cls):
        list_classroom=list()
        try:
            session=db_connect()
            query=session.query(Classroom).all()

            for classroom in query:
                dict_classroom={
                    'id': classroom.id,
                    'name': classroom.name,
                    'describe': classroom.describe
                }
                list_classroom.append(dict_classroom)
                print(list_classroom)
            return list_classroom

        except Exception as error:
            return {'message error': error}

    @classmethod
    def search_classroom(csl, name: str):

        try:
            list_classroom=list()
            session=db_connect()
            query=session.query(Classroom).filter(Classroom.name==name).all()

            for classroom in query:
                dict_classroom={
                    'id': classroom.id,
                    'name': classroom.name,
                    'describe': classroom.describe
                }
                list_classroom.append(dict_classroom)
            return list_classroom

        except Exception as error:
            return {'message error': error}
    
class ControllerSchedule:

    @classmethod
    def add_schedule(cls, name: str, date_start: datetime, date_end: datetime, party: str):
        try:
            if cls.verify_schedule_time(name,date_start,date_end):
                session=db_connect()
                query_classroom=session.query(Classroom).filter(Classroom.name==name)
                id_classroom=query_classroom[0].id
                session.add(Schedule(id_classroom=id_classroom,party=party,date=date_start.date(),time_start=date_start.time(),time_end=date_end.time()))
                session.commit()
                return {'status code': 200, 'message': f'data {date_start.date()} {date_start.time()} - {date_end.time()} ,  adicionada com sucesso'}
            else:
                return {'warning': f'data {date_start.date()} {date_start.time()} - {date_end.time()} , para a sala {name} não esta disponivel '}

        except Exception as error:
            return {'message error': error}

    @classmethod
    def verify_schedule_time(cls,name: str, date_start: datetime, date_end: datetime):
        try:
            session=db_connect()
            query_classroom=session.query(Classroom).filter(Classroom.name==name)
            id_classroom=query_classroom[0].id
            query=session.query(Schedule).filter(Schedule.id_classroom==id_classroom).filter(Schedule.date==date_start.date()).all()
            if len(query)==0:
                return True
            else:
                for item in query:
                    if date_start.time() < item.time_end or date_end.time() > item.time_start:
                        return False
                    else:
                        return True 

        except Exception as error:
            return {'message error': error}

    @classmethod
    def search_open_Schedule(cls, date_start: datetime, date_end: datetime):
        try:
            session=db_connect()
            query=session.query(Schedule).filter(Schedule.date==date_start.date()).all()
            if len(query)==0:
                query_classroom=session.query(Classroom).all()
                list_open_classroom=list()
                for classroom in query_classroom:
                    dict_open_classroom={
                        'id':classroom.id,
                        'name':classroom.name,
                        'describe':classroom.describe,
                        'available':True
                    }
                    list_open_classroom.append(dict_open_classroom)
                return list_open_classroom
            else:
                list_open_classroom=list()
                for classroom in query:

                    if date_start.time() < classroom.time_end or date_end.time() > classroom.time_start:
                        return False
                    else:
                        query_open_class=session.query(Classroom).filter(Classroom.id==classroom.id_classroom)
                        dict_open_classroom={
                            'id':query_open_class.id,
                            'name':query_open_class.name,
                            'describe':query_open_class.describe,
                            'available':True
                        }
                        list_open_classroom.append(dict_open_classroom)
                return list_open_classroom

        except Exception as error:
            return {'message error': error}
                    
