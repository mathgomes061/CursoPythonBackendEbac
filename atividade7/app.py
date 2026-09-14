from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Tarefa(BaseModel):
    nome: str
    descricao: str
    concluida: bool = False


tarefas: list[Tarefa] = []


@app.post("/adicionar")
def post_tarefa(tarefa: Tarefa):
    for tarefa_existente in tarefas:
        if tarefa_existente.nome == tarefa.nome:
            raise HTTPException(
                status_code=400,
                detail="Tarefa já existe na lista."
            )

    tarefas.append(tarefa)

    return {
        "mensagem": "Tarefa adicionada com sucesso!"
    }


@app.get("/tarefas")
def get_tarefas():
    if not tarefas:
        return {
            "mensagem": "Não há tarefas na lista."
        }

    return {
        "tarefas": tarefas
    }


@app.put("/atualizar/{nome}")
def put_tarefa(nome: str):
    for tarefa in tarefas:
        if tarefa.nome == nome:
            tarefa.concluida = True

            return {
                "mensagem": f"Tarefa '{tarefa.nome}' atualizada com sucesso!"
            }

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada."
    )


@app.delete("/deletar/{nome}")
def delete_tarefa(nome: str):
    for tarefa in tarefas:
        if tarefa.nome == nome:
            tarefas.remove(tarefa)

            return {
                "mensagem": f"Tarefa '{tarefa.nome}' deletada com sucesso!"
            }

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada na lista."
    )
