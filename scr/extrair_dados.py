import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

conexao = psycopg2.connect(
    host="localhost",
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    port=int(os.getenv("DB_PORT", 5433))
)

cursor = conexao.cursor()

#Extrair dados da tabela usuarios

cursor.execute("SELECT * FROM usuario")
usuarios = cursor.fetchall()

with open("lake/usuario.csv", "w") as arquivo:
    arquivo.write("id_usuario,nome,email,cpf,ano_nascimento, mes_nascimento, dia_nascimento,telefone,status\n")
    for usuario in usuarios:
        usuario =str(usuario).replace("(", "").replace(")", "").replace("datetime.date","").replace("'", "")
        arquivo.write(usuario + "\n")

#Extrair dados da tabela cursos

cursor.execute("SELECT * FROM curso")
cursos = cursor.fetchall()

with open("lake/curso.csv", "w") as arquivo:
    arquivo.write("id_curso,nome,descricao,valor,duracao\n")
    for curso in cursos:
        curso =str(curso).replace("(", "").replace(")", "").replace("Decimal","").replace("'", "")
        arquivo.write(curso + "\n")

cursor.execute("SELECT * FROM transacoes")
transacoes = cursor.fetchall()

# Extrair dados da tabela transacoes
with open("lake/transacoes.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write("id_transacao,id_curso,id_usuario,valor,metodo_pagamento,data\n")
    for transacao in transacoes:
        id_transacao, id_curso, id_usuario, valor, metodo_pagamento, data = transacao
        # Garantir que a data fique no formato YYYY-MM-DD HH:MM:SS.mmm
        if isinstance(data, datetime):
            data = data.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # corta para milissegundos
        
        linha = f"{id_transacao},{id_curso},{id_usuario},{valor},{metodo_pagamento},{data}\n"
        arquivo.write(linha)