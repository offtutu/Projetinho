# Aqui é os print que são utilizados no controller, para não poluir tanto o controller.

# Esse é um print para mostrar um produto especifico.
def Mostrar_produto(produto):
    print(produto)

# Esse é o print que mostra todos os produtos cadastrados e se não encontra nenhum produto, ele retorna que não tem produto.
def Mostrar_produtos(produtos):
    if not produtos:
        print('Nenhum produto encontrado.')
        return

    for produto in produtos:
        print(produto)

# Aqui é um modelo de print padrão para mensagens basicas, ex: "O Seu produto foi cadastrado com sucesso".
def Mostrar_mensagem(mensagem):
    print(mensagem)

# Aqui é um print para todas as mensagens de erros ou excessões.
def Mostrar_erro(erro):
    print(f'Motivo do Erro: {erro}')
