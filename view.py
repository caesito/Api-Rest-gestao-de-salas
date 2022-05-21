from urllib import response
from fastapi import FastAPI
from controller import ControllerClassroom, ControllerSchedule
from datetime import datetime
 
app=FastAPI()


@app.get('/lista')
def lista():
    response=ControllerClassroom.list_of_classroom()
    return response

@app.get('/filtro_nome')
def filtro_nome(name: str):
    response=ControllerClassroom.search_classroom(name=name)
    return response
    
@app.get('/filtro_disponibilidade')
def filtro_disponibilidade(date_start: datetime, date_end: datetime):
    response=ControllerSchedule.search_open_Schedule(date_start=date_start,date_end=date_end)
    return response

@app.post('/cadastro')
def cadastro(name: str, describe: str):
    response=ControllerClassroom.add_classroom(name=name, describe= describe)
    return response

@app.post('/agendamento')
def agendamento(name: str, date_start: datetime, date_end: datetime, party: str):
    response=ControllerSchedule.add_schedule(name=name,date_start=date_start, date_end=date_end, party=party)
    return response


