# 📊 Modelagem de Banco de Dados + Mini Data Lake

![img](/img/modelo_fisico.png)

Este projeto tem como objetivo **modelar um banco de dados relacional no PostgreSQL** e demonstrar um fluxo simples de **extração de dados para um mini data lake**.  
A ideia é simular um pipeline de dados em pequena escala: criar o modelo, popular com dados de exemplo e extrair os dados para armazenamento em formato CSV.

---

## 📂 Estrutura do Projeto

```
.
├── lake/ # Mini data lake
│ ├── curso.csv
│ ├── transacoes.csv
│ └── usuario.csv
│
├── scr/ # Scripts Python para ETL
│ ├── extrair_dados.py # Extrai dados do PostgreSQL e exporta para CSV
│ └── popular_tabelas.py # Popula as tabelas com dados de exemplo
│
├── sql/ # Scripts SQL
│ └── 01.curso.sql
│ └── 02.usuario.sql
│ └── 03.transacoes.sql
│
├── .env # Variáveis de ambiente (credenciais do PostgreSQL)
├── docker-compose.yml # Configuração do PostgreSQL em container Docker
├── requirements.txt # Dependências Python
└── README.md # Documentação do projeto
```

---

## 🗄️ Modelagem de Dados

O banco segue o modelo **relacional** com as entidades principais:

- **Usuário** (`usuario`) → informações cadastrais
- **Curso** (`curso`) → catálogo de cursos disponíveis
- **Transação** (`transacoes`) → registros de compras realizadas

As relações foram definidas com **chaves estrangeiras**, garantindo integridade referencial.

---

## 🚀 Tecnologias Utilizadas

- **PostgreSQL** (via Docker)
- **Python 3.12**
  - [psycopg2](https://pypi.org/project/psycopg2/) → conexão e consultas SQL
  - [python-dotenv](https://pypi.org/project/python-dotenv/) → variáveis de ambiente
- **Docker Compose** → orquestração do banco de dados

---

## ⚙️ Passo a Passo para Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Santiago956/modelagem-banco-de-dados.git
cd modelagem-banco-de-dados
```

### 2. Criar ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

```
POSTGRES_DB=seu_banco
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
DB_PORT=5433
```

### 5. Subir o banco no Docker

```bash
docker-compose up -d
```

### 6. Popular tabelas com dados de exemplo

```bash
python scr/popular_tabelas.py
```

### 7. Extrair dados para o mini data lake

```bash
python scr/extrair_dados.py
```
---

## Aviso / Disclaimer

Este projeto foi inicialmente desenvolvido como parte do curso da [DataEngineer.Help](DataEngineer.Help).
Embora o projeto tenha sido feito com o acompanhamento das aulas, algumas adaptações e implementações adicionais foram feitas individualmente para fins de aprendizado e aprimoramento pessoal.

