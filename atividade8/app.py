from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Optional
import secrets

app = FastAPI()

MEU_USUARIO = "admin"
MINHA_SENHA = "admin"

security = HTTPBasic()


class Tarefa(BaseModel):
    nome: str
    descricao: str
    concluida: bool = False


def autenticar_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    is_username_correct = secrets.compare_digest(
        credentials.username, MEU_USUARIO
    )
    is_password_correct = secrets.compare_digest(
        credentials.password, MINHA_SENHA
    )

    if not (is_username_correct and is_password_correct):
        raise HTTPException(
            status_code=401,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Basic"}
        )


tarefas: list[Tarefa] = []


@app.post("/adicionar")
def post_tarefa(
    tarefa: Tarefa,
    credentials: HTTPBasicCredentials = Depends(autenticar_usuario)
):
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
def get_tarefas(
    page: int = 1,
    size: int = 10,
    credentials: HTTPBasicCredentials = Depends(autenticar_usuario),
    ordena: Optional[str] = None
):
    if page < 1 or size < 1:
        raise HTTPException(
            status_code=400,
            detail="Página ou limites não podem ser menores que 1"
        )

    if not tarefas:
        return {
            "mensagem": "Não há tarefas na lista."
        }

    if ordena:
        if ordena not in ["nome", "descricao", "concluida"]:
            raise HTTPException(
                status_code=400,
                detail=(
                    f"Não é possível ordenar pelo campo '{ordena}'. "
                    "Escolha entre: nome, descricao ou concluida."
                )
            )

        tarefas_ordenadas = sorted(tarefas, key=lambda x: getattr(x, ordena))

    else:
        tarefas_ordenadas = tarefas

    inicio = (page - 1) * size
    fim = inicio + size
    tarefas_da_pagina = tarefas_ordenadas[inicio:fim]

    tarefas_formatadas = [
        {
            "nome_tarefa": tarefa.nome,
            "descricao_tarefa": tarefa.descricao,
            "tarefa_concluida": tarefa.concluida
        }
        for tarefa in tarefas_da_pagina
    ]

    return {
        "page": page,
        "size": size,
        "total": len(tarefas),
        "tarefas": tarefas_formatadas
    }


@app.put("/atualizar/{nome}")
def put_tarefa(
    nome: str,
    credentials: HTTPBasicCredentials = Depends(autenticar_usuario)
):
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
def delete_tarefa(
    nome: str,
    credentials: HTTPBasicCredentials = Depends(autenticar_usuario)
):
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
