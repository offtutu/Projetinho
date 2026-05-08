# Aqui é a parte da conexão do banco de dado.

# Essa parte é responsável por criar a conexão com o banco de dados.
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

# Aqui é onde o caminho do banco de dadoos, além do caminho, tem a criação da engine, da base e também das sessões.
db_path = os.path.join(os.path.dirname(__file__), 'dados.db')
engine = create_engine(f"sqlite:///{db_path}")
Base = declarative_base()
Sessao = sessionmaker(bind=engine)

# Aqui é função para criar as tabelas para o banco de dados, se for a primeira run do programa.
def Criar_tabelas():
    Base.metadata.create_all(engine)