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

@app.get("/receitas/{id}")
def get_receita(id: int):
    for r in receitas:
        if r.id == id:
            return r
    raise HTTPException(status_code=404, detail="Receita não encontrada")


