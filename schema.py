class Receita(BaseModel):
    id: int
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str

class Create_Receita(BaseModel):
    nome: str
    ingredientes: List[str]  # lista normal
    modo_de_preparo: str