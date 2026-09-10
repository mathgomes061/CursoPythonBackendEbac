from fastapi import FastAPI, HTTPException

app = FastAPI()

tarefas: list[dict] = []


@app.post("/adicionar")
def post_tarefa(nome: str, descricao: str):
    if any(tarefa["nome"] == nome for tarefa in tarefas):
        raise HTTPException(
            status_code=400, detail="Tarefa já existe na lista."
        )

    tarefas.append({"nome": nome, "descrição": descricao, "concluída": False})
    return {"mensagem": "Tarefa adicionada com sucesso!"}


@app.get("/tarefas")
def get_tarefas():
    if not tarefas:
        return {"mensagem": "Não há tarefas na lista."}

    return {"tarefas": tarefas}


@app.put("/atualizar/{nome}")
def put_tarefa(nome: str):
    for tarefa in tarefas:
        if tarefa["nome"] == nome:
            tarefa["concluída"] = True
            return {"mensagem": f"Tarefa '{nome}' atualizada com sucesso!"}

    raise HTTPException(
        status_code=404, detail="Tarefa não encontrada."
    )


@app.delete("/deletar/{nome}")
def delete_tarefa(nome: str):
    for tarefa in tarefas[:]:
        if tarefa["nome"] == nome:
            tarefas.remove(tarefa)
            return {"mensagem": f"Tarefa '{nome}' deletada com sucesso!"}

    raise HTTPException(
        status_code=404, detail="Tarefa não encontrada na lista."
    )
