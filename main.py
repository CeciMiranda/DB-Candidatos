from model import Candidato
from connect import *
from flask import Flask, render_template, redirect
from flask.globals import request


app = Flask (__name__)
@app.route('/')
def index():
    result = mostrarTodos()
    return render_template("index.html", 
    result = result)

@app.route("/cadastrar", methods=["POST","GET"])
def cadastrar():
    nome = request.form["nome"]
    numero = request.form["numero"]
    partido = request.form["partido"]
    candidato = Candidato(nome, numero, partido)
    inserir(candidato)
    return redirect ("/")

@app.route('/atualizar/<int:numero>',methods=["POST","GET"])
def atualizar(numero):    
    if request.method =='POST':
        nome = request.form["nome"]
        numero = request.form["numero"]
        partido = request.form["partido"]
        candidato = Candidato(nome, numero, partido)
        try:
            atualizarCandidato(numero, candidato)
            return redirect('/')
        except:
            return 'Erro ao atualizar candidato'
    else:
        candidato = buscarPorNumero(numero)
        return render_template('update.html', candidato = candidato)

@app.route('/deletar/<int:numero>')
def deletar(numero):
    try:
        deletarCandidato(numero)
        return redirect("/")
    except:
        return "Erro ao deletar candidato"


if __name__ == "__main__":
    app.run(debug=True)
 



