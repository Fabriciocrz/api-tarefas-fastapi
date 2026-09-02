# API de Tarefas (CRUD com FastAPI)

Mini projeto de backend desenvolvido em Python utilizando o framework FastAPI. O objetivo desta aplicação é criar uma API REST completa (CRUD) para gerenciamento de uma lista de tarefas (To-Do List).

## Tecnologias Utilizadas
* Python 3
* FastAPI
* Uvicorn (Servidor)
* Pydantic (Validação de dados)

## Funcionalidades
* `GET /tarefas`: Lista todas as tarefas cadastradas.
* `POST /tarefas`: Cria uma nova tarefa.
* `GET /tarefas/{id}`: Busca uma tarefa específica pelo ID.
* `PUT /tarefas/{id}`: Atualiza os dados de uma tarefa existente.
* `DELETE /tarefas/{id}`: Remove uma tarefa da lista.

## Como rodar o projeto localmente
1. Clone este repositório.
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install fastapi uvicorn
   ```
4. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```
5. Acesse no endereço: http://127.0.0.1:8000/docs