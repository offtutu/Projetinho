# Aqui é uma classe que herda do Exception, onde a função dela é de validação dos campos, como se fosse um tratamento de erros, onde ela trás o campo e o motivo do erro, para que o usuário possa entender melhor o que aconteceu de errado.
class ExceptionDeValidacao(Exception):
    def __init__(self, campo, motivo):
        self.campo = campo
        self.motivo = motivo
        super().__init__(f'{campo}: {motivo}')
