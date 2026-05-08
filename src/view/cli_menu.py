# Aqui são todos os imports que estão sendo utilizados no menu
from src.controller import product_controller
from src.infra.database.connection_factory import Criar_tabelas
from src.service.exceptions.duplicate_code_exception import ExceptionDeCodigoDuplicado
from src.service.exceptions.not_found_exception import ExceptionDeProdutoNaoEncontrado
from src.service.exceptions.validation_exception import ExceptionDeValidacao
from src.view import output_printer

# Aqui é uma função para poder criar a tabela do banco de dados, onde ela é chamada no run para criar a tabela antes de começar o menu.
def run():
    Criar_tabelas()

# Aqui é a função que puxa o menu de seleção para o usuario
def MostrarMenu():
    print('----------MENU DO PRODUTO---------')
    print('1 - Adicionar Produto')
    print('2 - Listar Produtos')
    print('3 - Editar Produto')
    print('4 - Remover Produto')
    print('5 - Sair')
    print('-' * 36)

# Aqui é a função para escolher as opções do menu
def EscolherOpcao():
    while True:
        MostrarMenu()
        opcao = input('Digite a opção que você deseja (1 a 5): ')

        # Aqui é a parte da funcionalidade das opções, onde você escolhe uma das opções, puxa um comando de função do controller, se a execução do comando passar pelo tratamento de excessões, o comando será feita com sucesso
        try:
            match opcao:
                case '1':
                    product_controller.Criar_produto()
                case '2':
                    product_controller.Listar_produtos()
                case '3':
                    product_controller.Atualizar_produto()
                case '4':
                    product_controller.Deletar_produto()
                case '5':
                    print('Encerrando sistema...')
                    break
                case _:
                    print('Escolha uma opção válida, por favor.')
        # Aqui é um tratamento de erro para o usuario digitir somento numeros.
        except ValueError:
            output_printer.Mostrar_erro('Digite apenas número válido.')
        # Aqui é o tratamento de excessões, onde importa os valores das classses herdadas lá da pasta exceptions da camada de service.
        except (
            ExceptionDeCodigoDuplicado,
            ExceptionDeProdutoNaoEncontrado,
            ExceptionDeValidacao,
        ) as erro:
            # Aqui retorna basicamento o erro ou alguma excessão que não foi aceita.
            output_printer.Mostrar_erro(erro)
