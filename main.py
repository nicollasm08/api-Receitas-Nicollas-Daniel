from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Livro de Receitas")

class Receita(BaseModel):
    id: int
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str

receitas: List[Receita] = []

@app.get("/")
def hello():
    return {"titulo": "Livro de Receitas"}

@app.get("/receitas")
def get_todas_receitas():
    return receitas

@app.get("/receitas/{nome}")
def get_receita(nome: str):
    for r in receitas:
        if r.nome.lower() == nome.lower():
            return r
    raise HTTPException(status_code=404, detail="Receita não encontrada")

@app.get("/receitas/id/{id}")
def get_receita(id: int):
    for r in receitas:
        if r.id == id:
            return r
    raise HTTPException(status_code=404, detail="Receita não encontrada")

@app.post("/receita")
def create_receita(dados: Receita):
    nova_receita = dados

    receitas.append(nova_receita)

    return nova_receita

@app.put("/receitas/{id}")
def update_receita(id: int, dados: Receita):
    for i in range(len(receitas)):
        if receitas[i].id == id:
            receita_atualizada = Receita(
                id=id,
                nome=dados.nome,
                ingredientes=dados.ingredientes,
                modo_de_preparo=dados.modo_de_preparo,
            )
            receitas[i] = receita_atualizada
            return receita_atualizada

    return {"mensagem": "Receita não encontrada"}


@app.delete("/receitas/{id}")
def deletar_receita(id: int):
    for i in range(len(receitas)):
        if receitas[i].id == id:
            receitas.pop(i)
            return {"Mensagem": "Receita deletada"}
    return {"Mensagem": " Receita não encontrada"}
