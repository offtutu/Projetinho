# Aqui são os imports do banco de dados para criar a tabela em cima do modelo do produto
from src.infra.database.connection_factory import Base
from sqlalchemy import Column, Integer, String

# Aqui é a classe do produto, onde tem os atributos da tabela
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(Integer, unique=True, nullable=False)
    nome = Column(String(80), nullable= False)
    marca = Column(String(80), nullable= False)
    classificacao = Column(String(50), nullable= False)

    # Aqui é uma função para printar os dados do produto de uma forma bem mais organizada e não printar ela como um objeto.
    def __str__(self):
        return f"""Código: {self.codigo}
Nome: {self.nome}
Marca: {self.marca}
Classificação: {self.classificacao}"""