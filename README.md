# Api-Rest-gestao-de-salas/V2


## Sobre o projeto:
Teste realizado para o programa processo seletivo.

## Tecnologias utilizadas: 

- Python;
- SGBD Mysql;
- ORM SQLAlchemy;
- Framework FastAPI

## Para executar o projeto:

- clone o repositorio;
- é necessario ter instalado o SGBD Mysql instalado;
- crie um banco de dados com o nome 'escola', ou o de sua preferencia;
- crie uma virtualenv para não ter problemas com outras versões de ferramentas;
- rode o comando `pip install -r requirements.txt` ,  arquivo que contem as dependencias; 
- altere as informações de conexão com o SGBD Mysql no arquivo model.py, se necessario:
  - USUARIO='root' ou 'nome de usuario do SGBD';
  - SENHA='senha definida para o SGBD';
  - HOST='localhost', caso seja local;
  - BANCO='Escola' ou o nome do banco criado;
  - PORT='3306' porta padrão do Mysql, verifique em qual porta esta rodando;
- no terminal do repositorio local rode o comando:
` uvicorn view:app --reload`
- acesse a url ` localhost:8000`  ou `localhost:8000/docs` para acessar a documentação e verificar os rotas/endpoint 
  - verifique no terminal se realmente o servidor foi inicializado na porta padrão 8000 
## Sobre o modelo no banco de dados:
![imagem_2022-05-22_191551389](https://user-images.githubusercontent.com/71521248/169718295-6ab3b30e-efc4-4c41-a2c8-214d9952fd3e.png)

## Documentação:
para a documentação foi utilizado Swagger UI atravez do framework FastAPI, e apos rodar o projeto pode ser acessada diretamente pela API em:
`localhost:8000/docs`

![imagem_2022-05-22_192725248](https://user-images.githubusercontent.com/71521248/169718623-38eba13d-9557-41b1-8a6a-13d4f6b8f1ec.png)

