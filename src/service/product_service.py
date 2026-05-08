# Aqui são os imports que serão nescessario para esse model do codigo.
from src.model.product import Produto
# Aqui é a importação do repositorio de produtos, onde ele linka o service com o banco de dados.
from src.model.product_repository import RepositorioDeProdutos

from src.service.exceptions.duplicate_code_exception import ExceptionDeCodigoDuplicado
from src.service.exceptions.not_found_exception import ExceptionDeProdutoNaoEncontrado
from src.service.exceptions.validation_exception import ExceptionDeValidacao

# Aqui é a classe do serviço do produto principal, onde tem tanto as regras de negocios quanto as validações.
class ProdutoService:
    def __init__(self):
        self.repositorio = RepositorioDeProdutos()

    # Aqui é a função de criar produto, ontem tem as validações e a exceção a codigo duplicado.
    def Criar(self, codigo, nome, marca, classificacao):
        self._ValidarCodigo(codigo)
        self._Validartexto("Nome", nome)
        self._Validartexto("Marca", marca)
        self._Validartexto("Classificação", classificacao)
        nome = nome.strip()
        marca = marca.strip()
        classificacao = classificacao.strip()

        if self._BuscarPorCodigo(codigo) is not None:
            raise ExceptionDeCodigoDuplicado(codigo)

        produto = Produto(codigo=codigo, nome=nome, marca=marca, classificacao=classificacao)
        self.repositorio.Salvar(produto)    
        return produto

    # Aqui é a função de listar os produtos cadastrados, ela também sua exceção, que seria a de produto não encontrado.
    def Listar(self):
        return self.repositorio.Listar()

    # Aqui é a função para atualizar algum produto cadastrado, onde tem as validações e a exceção de produto não encontrado.    
    def Atualizar(self, codigo, nome, marca, classificacao):
        self._ValidarCodigo(codigo)
        self._Validartexto('Nome', nome)
        self._Validartexto('Marca', marca)
        self._Validartexto('Classificação', classificacao)
        nome = nome.strip()
        marca = marca.strip()
        classificacao = classificacao.strip()

        produto = self._BuscarPorCodigo(codigo)

        if produto is None:
            raise ExceptionDeProdutoNaoEncontrado(codigo)

        produto.nome = nome
        produto.marca = marca
        produto.classificacao = classificacao

        self.repositorio.Atualizar(produto)
        return produto

    # Aqui é a função de deletar, onde ela tem a suas validações e a exceção de produto não encontrado.
    def Deletar(self, codigo):
        self._ValidarCodigo(codigo)

        produto = self._BuscarPorCodigo(codigo)

        if produto is None:
            raise ExceptionDeProdutoNaoEncontrado(codigo)

        self.repositorio.Deletar(produto)
        return produto

    # Aqui é a função de buscar um produto pelo codigo, onde ela retorna um produto pelo codigo e tem sua exceção de prduto não encontrado também.
    def _BuscarPorCodigo(self, codigo):
        return self.repositorio.BuscarPorCodigo(codigo)

    # Aqui é a função de validação, ela é extremamente importante, porque ela é o tratamento de erros, onde o trabalho dela é validar todos os campos de codigo, a excesão da mesma é a de validação, onde ela trás o campo e o motivo do erro.
    def _ValidarCodigo(self, codigo):
        if not isinstance(codigo, int):
            raise ExceptionDeValidacao('Codigo', 'Numero invalido, digite um numero inteiro, fazendo favor.')

        if codigo <= 0:
            raise ExceptionDeValidacao('Codigo', 'Numero invalido, o codigo tem que ser maior que zero')

    # Aqui é basicmamente a mesma coisa da funçãa acima, só que agora ela é para os campos de texto.
    def _Validartexto(self, campo, valor):
        if not isinstance(valor, str):
            raise ExceptionDeValidacao(campo, 'Esse campo precisa ser um texto.')

        if valor.strip() == '':
            raise ExceptionDeValidacao(campo,'Esse campo não pode ficar vazio, favor preencher o campo.')
