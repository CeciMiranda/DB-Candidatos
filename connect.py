from tinydb import TinyDB, Query
from model import Candidato
import pandas as pd


bd = TinyDB("Candidatos.json")
cdd = Query()

def inserir(model: Candidato):
    bd.insert({"Nome":model.nome, 
    "Numero": model.numero, 
    "Partido": model.partido,
    "Quantidade de votos": model.qtdVotos})

def mostrarTodos():
    todos = bd.all()
    return todos

def deletarCandidato(numero: int):
    print(numero)
    if bd.search(cdd.Numero == str(numero)):
        bd.remove(cdd.Numero == str(numero))
    else:
        print("Candidato não encontrado")

def atualizarCandidato(numero:int, model:Candidato):
    print(numero)
    if bd.search(cdd.Numero == str(numero)):
        bd.remove(cdd.Numero == str(numero))
        inserir(model)
    else:
        print("Este candidato não existe")

def mostrarTabelaTodos():
    todos = pd.DataFrame(bd) 
    return todos

def buscarPorNumero(numero):
    return bd.search(cdd.Numero == str(numero))