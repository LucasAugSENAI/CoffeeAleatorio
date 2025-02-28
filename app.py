from flask import Flask, render_template, request, redirect,g
import requests # requisição para usarmos as APIs
import sqlite3
url = "https://coffee.alexflipnote.dev/random.json"


def ligar_banco():
    banco = g.database = sqlite3.connect('API-Cafe.db')
    return banco

app = Flask(__name__)


@app.route('/')
def home():
    solicitacao = requests.get(url)
    dados = solicitacao.json()
    imagem = dados["file"]
    return render_template('index.html', Titulo = 'API Imagens', imagem = imagem)

@app.route('/coffe')
def cadastro():
    solicitacao = requests.get(url)
    dados = solicitacao.json()
    imagem = dados["file"]
    return render_template('Coffee.html', Titulo = 'API Imagens - Café', imagem = imagem)

@app.route('/galeria')
def galeria():
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute('SELECT Descricao, Imagem FROM CoffeeAPI')
    imagens = cursor.fetchall()
    return render_template('galeria.html', Titulo = 'API Imagens - Galeria', imagensbd = imagens)

@app.route('/criar', methods=['POST'])
def criar():
    imagem = request.form['url']
    descricao = request.form['descricao']
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute('INSERT INTO CoffeeAPI(Descricao,Imagem)'
                   'VALUES(?,?);'
                   '',(descricao,imagem))
    banco.commit()
    return redirect('/coffe')

if __name__ == '__main__':
    app.run()
