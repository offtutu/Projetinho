from src.view import cli_menu
from src.infra.database.connection_factory import Criar_tabelas

def main():
    Criar_tabelas()
    cli_menu.run()
    cli_menu.EscolherOpcao()

if __name__ == "__main__":
     main()