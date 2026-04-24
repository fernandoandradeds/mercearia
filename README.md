# Mercearia — Sistema de Gestão em Python

Sistema de gerenciamento para mercearias desenvolvido em Python puro, aplicando o padrão **MVC (Model-View-Controller)** com persistência em arquivos de texto.

## Funcionalidades

- **Categorias** — cadastro e remoção de categorias de produtos
- **Estoque** — controle de entrada e saída de produtos com quantidade
- **Vendas** — registro de vendas com desconto automático do estoque
- **Fornecedores** — cadastro de fornecedores por CNPJ
- **Clientes** — cadastro de clientes por CPF
- **Funcionários** — cadastro com vínculo CLT, cargo e salário

## Arquitetura

```
mercearia/
├── Models.py       # Entidades do domínio
├── DAO.py          # Camada de acesso a dados (arquivos .txt)
├── Controller.py   # Regras de negócio
└── View.py         # Interface de linha de comando (menu interativo)
```

O projeto segue o padrão MVC para separação de responsabilidades:

| Camada | Arquivo | Responsabilidade |
|--------|---------|-----------------|
| Model | `Models.py` | Definição das classes de domínio |
| DAO | `DAO.py` | Leitura e escrita nos arquivos de dados |
| Controller | `Controller.py` | Validações e regras de negócio |
| View | `View.py` | Interface interativa via terminal |

## Como executar

**Pré-requisitos:** Python 3.8+

```bash
git clone https://github.com/fernandoandradeds/mercearia.git
cd mercearia
python View.py
```

Nenhuma dependência externa — apenas biblioteca padrão do Python.

## Demonstração

```
==================================================
  MERCEARIA — SISTEMA DE GESTÃO
==================================================
1. Categorias
2. Estoque
3. Vendas
4. Fornecedores
5. Clientes
6. Funcionários
0. Sair
```

## Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

## Autor

**Fernando Andrade** — [GitHub](https://github.com/fernandoandradeds) · [LinkedIn](https://www.linkedin.com/in/fernandoandradeds/)
