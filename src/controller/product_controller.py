# Aqui é o import onde ele puxa as funções do service para serem usadas no controller e o controller é que passa informação para o view.
from src.service.product_service import ProdutoService
# Aqui são dois imports para deixar o controller menos poluido, aqui são inputs e printers que vem da camada view.
from src.view import input_reader
from src.view import output_printer

# Aqui é parte do controller onde ele passa as informações para o service e o service faz a parte tecnica, enquanto o controller é a parte faz comunicação para o view.
produto_service = ProdutoService()

# Aqui é a função que leva a informação para a primeira opção do menu no view, ela serve para criar um produto.
def Criar_produto():
    codigo = input_reader.Entrada_codigo()
    nome = input_reader.Entrada_nome()
    marca = input_reader.Entrada_marca()
    classificacao = input_reader.Entrada_classificacao()

    produto = produto_service.Criar(codigo, nome, marca, classificacao)

    output_printer.Mostrar_mensagem('O Produto criado com sucesso!')
    output_printer.Mostrar_produto(produto)
    return produto

# Aqui é a função que leva a segunda opção do menu, ela serve para listar os produtos que foram criados com a função acima.
def Listar_produtos():
    produtos = produto_service.Listar()
    output_printer.Mostrar_produtos(produtos)

# Aqui é a função que leva a terceira opção do menu, ela serve para atualizar um produto, onde ela pede o codigo do produto que você deseja atualizar e passa os novos valores.
def Atualizar_produto():
    produto_service.Atualizar(
        codigo = input_reader.Entrada_codigo(),
        nome = input_reader.Entrada_nome(),
        marca = input_reader.Entrada_marca(),
        classificacao = input_reader.Entrada_classificacao()
    )
    output_printer.Mostrar_mensagem('O Produto atualizado com sucesso!')
    output_printer.Mostrar_produtos(produto_service.Listar())

# Aqui é a função que leva a quarta opção do menu, ela serve para deletar um produto, onde ela pede o codigo do produto que você deseja excluir.
def Deletar_produto():
    codigo = input_reader.Entrada_codigo()
    produto = produto_service.Deletar(codigo)

    output_printer.Mostrar_mensagem('O Produto foi deletado com sucesso!')
    output_printer.Mostrar_produto(produto)
