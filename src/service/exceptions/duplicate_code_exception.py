# Aqui é uma classe que herda do Exception, onde a função dela é de código duplicado, ou seja, quando o usuário tentar cadastrar um produto com um código que já existe, ele retorna uma exceção, para o usuário entender melhor o porque do erro.
class ExceptionDeCodigoDuplicado(Exception):
    def __init__(self, codigo):
        self.codigo = codigo
        super().__init__(f'Já existe um produto com o código {codigo} cadastrado')
