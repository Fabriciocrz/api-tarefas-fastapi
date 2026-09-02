from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional


#Criação da API
app = FastAPI(title= "API de Tarefas")

#Modelo de dados:
class Tarefa(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    concluida: bool = False

#Banco em memoria:
db_tarefas = []

#Rota de listagem de tarefas:
@app.get('/tarefas', response_model=list[Tarefa])
async def listar_tarefas():
    return db_tarefas

#Rota de criação de tarefas:
@app.post('/tarefas', response_model=Tarefa, status_code=201) 

async def criar_tarefa(tarefa: Tarefa):
    tarefa.id = len(db_tarefas)+1
    db_tarefas.append(tarefa)
    return tarefa

#Rota de busca de tarefas por id:
@app.get("/tarefas/{tarefa_id}", response_model = Tarefa)
async def obter_tarefa(tarefa_id: int):
    for t in db_tarefas:
        if t.id == tarefa_id:
            return t
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

#Rota para alterar tarefa:
@app.put('/tarefas/{tarefa_id}', response_model = Tarefa)
async def atualizar_tarefa(tarefa_id: int, tarefa_atualizada: Tarefa):
    for index, t in enumerate(db_tarefas):
        if t.id == tarefa_id:
            tarefa_atualizada.id = tarefa_id

            db_tarefas[index] = tarefa_atualizada

            return tarefa_atualizada

    raise HTTPException(status_code=404, detail = "Tarefa não encontrada")

#Rota para deletar:
@app.delete('/tarefas/{tarefa_id}',status_code=204)
async def deletar_tarefa(tarefa_id: int):
    for t in db_tarefas:
        if t.id == tarefa_id:
            db_tarefas.remove(t)
            return 
    raise HTTPException(status_code=404, detail= "Tarefa não encontrada")