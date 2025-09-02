from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="API dos negros")

# Modelo base com id opcional (não fornecido pelo usuário)
class Receita(BaseModel):
    id: Optional[int] = None  # ID gerado automaticamente
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str

# Lista para armazenar receitas
receitas: List[Receita] = []

@app.get("/")
def hello():
    return {"titulo": "Livro de Receitas"}

@app.get("/receitas/{nome}")
def get_receita(nome: str):
    for r in receitas:
        if r.nome.lower() == nome.lower():
            return r
    raise HTTPException(status_code=404, detail="Receita não encontrada")

@app.get("/receitas")
def get_todas_receitas():
    return receitas

@app.post("/receitas", response_model=Receita, status_code=201)
def criar_receita(dados: Receita):
    # Verifica se já existe receita com o mesmo nome (ignorar maiúsc/minúsc)
    for r in receitas:
        if r.nome.lower() == dados.nome.lower():
            raise HTTPException(status_code=400, detail="Já existe uma receita com esse nome.")

    # Gerar novo id incremental
    novo_id = len(receitas) + 1

    # Criar a nova receita com id gerado automaticamente
    nova_receita = Receita(
        id=novo_id,
        nome=dados.nome,
        ingredientes=dados.ingredientes,
        modo_de_preparo=dados.modo_de_preparo
    )

    receitas.append(nova_receita)

    return nova_receitas