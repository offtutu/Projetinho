# ====== POO + SQL + CLI ======

Projeto desenvolvido em Python utilizando o padrão MVC para construções das camadas.

## Objetivo

O sistema permite:

- Cadastro de produtos
- Listagem de produtos
- Atualização de produtos
- Remoção de produtos

O projeto foi desenvolvido com foco em:

- Programação Orientada a Objetos
- Arquitetura em camadas
- Separação de responsabilidades
- Persistência de dados com ORM
- Tratamento de exceções
- Pratica de menu do usuario

---

## Tecnologias Utilizadas

- Python 3
- SQLAlchemy
- SQLite

---

## Executar o projeto

```bash
python main.py
```
---

## Arquitetura do Sistema

O projeto segue uma arquitetura em camadas:

```text
View
↓
Controller
↓
Service
↓
Model
↓
Database
```

---

## Responsabilidades

| Camada | Responsabilidade |
|---|---|
| View | Interface CLI e entrada de dados |
| Controller | Comunicação entre View e Service |
| Service | Regras de negócio e validações |
| Model | Representação das entidades ORM e Operações de persistência no banco |
| Infra | Configuração de banco e infraestrutura |

---

## Estrutura do Projeto

```text
repo/
  README.md
  .gitignore
  /src
    /model
      product.py
      product_repository.py
    /service
      product_service.py
      /exceptions
        business_exception.py
        not_found_exception.py
        duplicate_code_exception.py
        validation_exception.py
    /controller
      product_controller.py
    /view
      cli_menu.py
      input_reader.py
      output_printer.py
    /infra
      /database
        connection_factory.py
    main.py
```
