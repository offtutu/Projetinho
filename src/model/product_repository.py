# Aqui é a parte dos imports do banco de dados e do model produto.
from src.infra.database.connection_factory import Sessao
from src.model import product

# Aqui é a classe do repositorio dos comandos que são utilizados no service.
class RepositorioDeProdutos:
    def __init__(self):
        self.sessao = Sessao()

    # Aqui é a função para salvar o produto.
    def Salvar(self, produto: product.Produto):
        self.sessao.add(produto)
        self.sessao.commit()
    
    # Essa aqui é para listar.
    def Listar(self):
        return self.sessao.query(product.Produto).all()
    
    # Essa é para buscar um produto pelo código.
    def BuscarPorCodigo(self, codigo: int):
        return self.sessao.query(product.Produto).filter_by(codigo=codigo).first()
    
    # Aqui é para atualizar um produto.
    def Atualizar(self, produto: product.Produto):
        self.sessao.merge(produto)
        self.sessao.commit()

    # Aqui é para deletar um produto.
    def Deletar(self, produto: product.Produto):
        self.sessao.delete(produto)
        self.sessao.commit()

        return produto