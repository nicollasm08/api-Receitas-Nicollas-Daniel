from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title = "API dos negros")

class Receita(BaseModel):
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str

receitas: List[Receita] = []



'''receitas = [
    {
        'nome': 'Abacatada',
    
        'ingredientes': [
        '1 abacate bem grande',
        '1 litro de leite',
        '2 colheres de açúcar (ou a gosto)'
        ],

        'utensílios': [
        'Copo',
        'Liquidificador',
        'Faca',
        'Tábua de corte'
        ],

        'modo de preparo': '1. Descasque o abacate e retire o caroço. '
                       '2. Coloque o abacate, o leite e o açúcar no liquidificador. '
                       '3. Bata até obter uma mistura homogênea. '
                       '4. Sirva gelado em copos.'
    },

    {
        'nome': 'Bolo de Chocolate',
        'ingredientes': ['3 ovos', '2 xícaras (chá) de farinha de trigo', 
                         '1/2 xícara (chá) de óleo', '1 pitada de sal',
                         '1 e 1/2 xícara (chá) de açúcar', '1 xícara (chá) de chocolate em pó ou achocolatado',
                         '1 colher (sopa) de fermento em pó', '1 xícara (chá) de água quente', 
                         '4 colheres (sopa) de leite', '1 colher (sopa) de manteiga', 
                         '1/2 xícara (chá) de chocolate em pó', '1 xícara (chá) de açúcar'],

        'utensílios': ['Liquidificador', 'Panela',
                       'Forma de bolo','Bowl'],

        'modo de preparo': '1. Em um liquidificador, bata os ovos, o açúcar, o óleo, o achocolatado e a farinha de trigo. 2. Despeje a massa em uma tigela e adicione a água quente e o fermento, misturando bem. 3. Despeje a massa em uma forma untada e asse em forno médio-alto (200° C), preaquecido, por 40 minutos. 4. Desenforme ainda quente. 5. Em uma panela, leve todos os ingredientes ao fogo até levantar fervura. 6. Despeje ainda quente em cima do bolo.'
    },

    {
        'nome': 'Cocada',
        
        'ingredientes': [
        '400g de coco fresco ralado',
        '1 e 1/2 xícara (chá) de água',
        '2 e 1/2 xícaras (chá) de açúcar',
        '1/4 xícara (chá) de leite condensado',
        'Óleo (quanto baste para untar)'
        ],

        'utensílios': [
        'Panela',
        'Colher de madeira',
        'Forma (ou assadeira)',
        'Espátula'
        ],

        'modo de preparo': '1. Unte uma assadeira grande com óleo e reserve. '
                       '2. Em uma panela, coloque a água e o açúcar e leve ao fogo alto. '
                       '3. Cozinhe até atingir o ponto de fio médio. '
                       '4. Acrescente o coco ralado e mexa bem. '
                       '5. Adicione o leite condensado e continue mexendo até a mistura começar a desgrudar do fundo da panela. '
                       '6. Retire do fogo e, com a ajuda de uma colher, faça porções sobre a assadeira untada. '
                       '7. Deixe endurecer um pouco e retire com uma espátula. '
                       '8. Para armazenar, espere esfriar completamente e guarde em um recipiente com tampa.'
    },

    {
        'nome': 'Lasanha Mista',
        

        'ingredientes': [
        # Massa
        '1 pacote de massa para lasanha',

        # Recheio
        '150g de presunto', '150g de queijo', '100g de carne moída',

        # Molho bolonhesa
        '1 cebola picadinha', '1 colher de sopa de manteiga', '1 caldo de carne',
        '1 caixinha de polpa de tomate', '4 tomates cortados em cubos', 
        '1/2 caixinha de creme de leite', 'Sal e açúcar a gosto',

        # Molho branco
        '1 colher de sopa de margarina', '1 colher de sopa de farinha de trigo',
        '100ml de leite', '1 pacote de queijo ralado', '1/2 caixinha de creme de leite'
    ],

        'utensílios': ['Panela', 'Colher', 'Liquidificador', 'Travessa', 'Faca', 'Fogão'],

        'modo de preparo': '1. Cozinhe a massa da lasanha em água com sal e óleo. Reserve.\n'
                       '2. Para o molho bolonhesa, refogue a cebola picada em 1 colher de sopa de manteiga. '
                       'Adicione a carne moída, alho, sal e o caldo de carne picado. '
                       'Misture bem, adicione a polpa de tomate e continue refogando. '
                       'Bata os tomates com o restante da polpa no liquidificador e despeje na panela. '
                       'Tempere com sal e açúcar, deixe ferver, desligue o fogo e adicione 1/2 caixinha de creme de leite.\n'
                       '3. Para o molho branco, em outra panela, derreta 1 colher de sopa de margarina e refogue a cebola. '
                       'Acrescente a farinha de trigo e misture até dourar levemente. '
                       'Adicione o leite aos poucos, dissolvendo bem até formar um mingau. '
                       'Acrescente o queijo ralado e 1/2 caixinha de creme de leite. Misture bem e reserve.\n'
                       '4. Para montar a lasanha, alterne camadas de molho bolonhesa, presunto, massa, molho branco e queijo. '
                       'Finalize com uma camada de queijo por cima. Leve ao forno até gratinar e sirva quente.'

    },

    {
        'nome': 'Pizza Mista',
        
        'ingredientes': [
        # Massa
        '500g de farinha de trigo', '250ml de água', '1 colher de açúcar',
        '1 gema', '2 colheres (chá) de azeite', '10g de fermento biológico seco instantâneo',
        '1 colher de sal',

        # Molho
        '1 caixinha de molho de tomate', '125ml de mostarda', '3 colheres de óleo',
        '1 alho amassado', '125ml de catchup', '1/2 pacote de orégano', '1/2 cebola picada',

        # Cobertura
        '400g de mussarela', '300g de presunto', '1 calabresa defumada cortada em rodelas',
        '1 colher de orégano', '1 tomate cortado em rodelas', 'Azeitonas sem caroço'
    ],
        'utensílios': ['Tigela grande', 'Forma para pizza', 'Liquidificador', 'Panela', 'Colher', 'Forno'],

        'modo de preparo': '1. Misture todos os ingredientes da massa até formar uma bola homogênea. Cubra com plástico sem abafar e deixe fermentar por 45 minutos. '
                      '2. Abra a massa bem fina e distribua nas formas próprias. '
                      '3. Leve ao forno preaquecido por 20 minutos ou até dourar por cima (cuidado para não queimar embaixo). '
                      '4. Para o molho, bata no liquidificador o molho de tomate, orégano, catchup e mostarda. Reserve. '
                      '5. Em uma panela, refogue o alho e a cebola no óleo, depois adicione o molho batido e deixe ferver por 5 minutos. '
                      '6. Retire o molho do fogo e deixe esfriar. '
                      '7. Com a massa já pré-assada, passe o molho sobre ela. '
                      '8. Cubra com presunto, depois mussarela, depois calabresa, rodelas de tomate e azeitonas. Salpique orégano. '
                      '9. Leve ao forno novamente por 10 minutos ou até o queijo derreter. Sirva em seguida.'
    },

    {
        'nome': 'Pudim',
        
        'ingredientes': [
        # Pudim
        '1 lata de leite condensado',
        '1 lata de leite (medida da lata de leite condensado)',
        '3 ovos',

        # Calda
        '1 xícara (chá) de açúcar',
        '1/2 xícara de água'
        ],

        'utensílios': [
        'Liquidificador',
        'Panela',
        'Forma de pudim',
        'Prato de sobremesa',
        'Espátula'
        ],

        'modo de preparo': '1. No liquidificador, bata bem os ovos. Adicione o leite condensado e o leite, e bata novamente. Reserve.\n'
                       '2. Para a calda, derreta o açúcar em uma panela até atingir um tom dourado. Adicione a água com cuidado e mexa até engrossar.\n'
                       '3. Despeje a calda na forma de pudim, espalhando bem no fundo.\n'
                       '4. Coloque a mistura do pudim por cima da calda na forma.\n'
                       '5. Leve ao forno médio preaquecido por 45 minutos, em banho-maria (forma de pudim dentro de uma forma maior com água).\n'
                       '6. Espete um garfo para verificar se está assado. Retire do forno, deixe esfriar e desenforme em um prato de sobremesa.'
    },
]'''

@app.get("/")
def hello():
    return{"titulo":"Livro de Receitas"}

@app.get("/receitas/{receita}")
def get_receita(receita: str):
    for r in receitas:
        if r["nome"].lower() == receita.lower():
            return r
    return {"erro": "Receita não encontrada"}

@app.get("receitas")
def get_todas_receits():
    return receitas

@app.post("/receitas", response_model=Receita, status_code=status=201) 
def criar_receita(dados: Receita):

    nova_receitas = dados
    receitas.append(nova_receita)

    return nova_receita