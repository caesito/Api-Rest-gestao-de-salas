from fastapi import FastAPI, Response, status
from controller import ControllerClassroom, ControllerSchedule
from datetime import datetime
 

description="""
    API REST para gestão de salas:
    
     Cadastro de Salas de Aula;
     Listagem das Salas;
     Busca filtrada por nome ou salas disponíveis;
     Agendamento de sala de aula.
"""

app=FastAPI(
    title='GestãodesalasApi',
    description=description
)

@app.get('/')
def root():
    return {"message" :" Bem vindo a GestãodesalasApi, para consultar nossos andpoints/rotas acesse a url em:  /docs"}
    
@app.get('/lista', tags=['Listagem de salas cadastradas'])
def lista():
    response=ControllerClassroom.list_of_classroom()
    return response

@app.get('/filtro_nome', tags=['Filtrar por nome'])
def filtro_nome(name: str):
    response=ControllerClassroom.search_classroom(name=name)
    return response

@app.get('/filtro_disponibilidade', tags=['Filtrar por salas disponiveis'], description= 'necessario informar o horario. Exemplo: ano: 2022, dia: 18, hora: 17')
def filtro_disponibilidade( ano: int, mes: int, dia: int, hora_inicio: int, hora_fim: int):
    date_start=datetime(ano,mes,dia,hora_inicio)
    date_end=datetime(ano,mes,dia,hora_fim)
    response=ControllerSchedule.search_open_Schedule(date_start=date_start,date_end=date_end)
    return response

@app.post('/cadastro', tags=['Cadastro de sala'],status_code= 200)
def cadastro(name: str, describe: str, resp: Response):
    response=ControllerClassroom.add_classroom(name=name, describe= describe)
    if response is False:
        resp.status_code=status.HTTP_406_NOT_ACCEPTABLE
        return {'warning': f'sala {name} ja existe, não foi possivel adicionar!'}
    else:
        return response

@app.post('/agendamento', tags=['Agendar horario'], description= 'Exemplo: ano: 2022, dia: 18, hora: 17',status_code= 200)
def agendamento(nome: str, ano: int, mes: int, dia: int, hora_inicio: int, hora_fim: int, turma: str, resp: Response):
    date_start=datetime(ano,mes,dia,hora_inicio)
    date_end=datetime(ano,mes,dia,hora_fim)
    response=ControllerSchedule.add_schedule(name=nome,date_start=date_start, date_end=date_end, party=turma)
    if response is False:
        resp.status_code=status.HTTP_406_NOT_ACCEPTABLE
        return {'warning': f'data {date_start.date()} {date_start.time()} - {date_end.time()} , para a sala {nome} não esta disponivel '}
    else:
        return response


