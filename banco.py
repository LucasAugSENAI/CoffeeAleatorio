import sqlite3
conexao = sqlite3.connect('API-Cafe.db')
cursor = conexao.cursor() # executar comando SQL
cursor.execute('CREATE TABLE IF NOT EXISTS CoffeeAPI'
               '(ID INTEGER PRIMARY KEY,'
               'Descricao TEXT,'
               'Imagem TEXT)')