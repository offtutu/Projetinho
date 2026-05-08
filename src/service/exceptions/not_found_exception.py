# Aqui é uma classe que herda o Exception, onde a função dela é ir atrás de um produto pelo codigo e se não encontrar, retorna uma exceção, para o usuario entender melhor o porque do erro.
class ExceptionDeProdutoNaoEncontrado(Exception):
    def __init__(self, codigo):
        self.codigo = codigo
        super().__init__(f'Produto com código {codigo} não encontrado')
