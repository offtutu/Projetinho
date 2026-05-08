# Aqui é uma classe que herda do Exception, onde a função dela é de regra de negócio, ou seja, quando o usuário tentar fazer algo que não é permitido pelas regras do sistema, ele retorna uma exceção, para o usuário entender melhor o porque do erro.
class ExceptionDeRegraDeNegocio(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
        super().__init__(mensagem)
