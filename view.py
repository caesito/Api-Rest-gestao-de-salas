from urllib import response
from fastapi import FastAPI
from controller import ControllerClassroom, ControllerSchedule
 
app=FastAPI()


@app.post('/cadastro')
def cadastro(name: str, describe: str):
    response=ControllerClassroom.add_classroom(name=name, describe= describe)
    return response

@app.get('/lista')
def lista():
    response=ControllerClassroom.list_of_classroom()
    return response