from dotenv import load_dotenv
from faker import Faker
from faker.providers import person, address, internet, date_time
import psycopg2
import os

# Adicionando o provedor brasileiro
load_dotenv()


fake = Faker('pt_BR')
fake.add_provider(person)
fake.add_provider(address)
fake.add_provider(internet)
fake.add_provider(date_time)
fake.unique.clear()

conexao = psycopg2.connect(
    host="localhost",
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    port=int(os.getenv("DB_PORT", 5433))
)

cur = conexao.cursor()


#Populando a tabela usuários
for _ in range(100*100):
    nome = fake.name()
    email = fake.unique.email()  # garante que não repita
    cpf = fake.unique.cpf()
    data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=100)
    telefone = fake.phone_number()
    status = fake.random_element(elements=('aluno', 'instrutor'))

    cur.execute(
        f"INSERT INTO usuario (nome, email, cpf, data_nascimento, telefone, status) VALUES ('{nome}', '{email}', '{cpf}', '{data_nascimento}', '{telefone}', '{status}')"
        )
    
# Populando a tabela cursos
for _ in range(20*100):
    nome = fake.bs().title()
    descricao = fake.text(max_nb_chars=100)
    valor = fake.random_int(min=0, max=500)
    duracao = fake.random_int(min=4, max=200)
    cur.execute(
        f"INSERT INTO curso (nome, descricao, valor, duracao) VALUES ('{nome}', '{descricao}', {valor}, {duracao})"
    )

# Populando a tabela transacoes

for _ in range(100*100):
    id_curso = fake.random_int(min=1, max=20)
    id_usuario = fake.random_int(min=1, max=100)
    valor = fake.random_int(min=0, max=500)
    metodo_pagamento = fake.random_element(elements=('credito', 'debito', 'boleto', 'pix'))
    data = fake.date_time_this_year()
    cur.execute(
        f"INSERT INTO transacoes (id_curso, id_usuario, valor, metodo_pagamento, data) VALUES ({id_curso}, {id_usuario}, {valor}, '{metodo_pagamento}', '{data}')"
    )

#Confirmando transações
conexao.commit()

#Fechar a conexão
cur.close()
conexao.close()