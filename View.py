import os
from Controller import (
    ControllerCategoria, ControllerEstoque, ControllerVenda,
    ControllerFornecedor, ControllerCliente, ControllerFuncionario
)

ctrl_cat = ControllerCategoria()
ctrl_est = ControllerEstoque()
ctrl_venda = ControllerVenda()
ctrl_forn = ControllerFornecedor()
ctrl_cli = ControllerCliente()
ctrl_func = ControllerFuncionario()

FILES = ['categoria.txt', 'estoque.txt', 'venda.txt', 'fornecedores.txt', 'clientes.txt', 'funcionarios.txt']


def init_files():
    for f in FILES:
        if not os.path.exists(f):
            open(f, 'w').close()


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def cabecalho(titulo):
    limpar()
    print("=" * 50)
    print(f"  MERCEARIA — {titulo}")
    print("=" * 50)


# ── CATEGORIAS ─────────────────────────────────────

def menu_categorias():
    while True:
        cabecalho("CATEGORIAS")
        print("1. Cadastrar categoria")
        print("2. Remover categoria")
        print("3. Listar categorias")
        print("0. Voltar")
        op = input("\nOpção: ").strip()

        if op == "1":
            nome = input("Nome da categoria: ").strip()
            if nome:
                ctrl_cat.cadastrarCategoria(nome)
            input("\nEnter para continuar...")

        elif op == "2":
            cats = ctrl_cat.listarCategorias()
            if not cats:
                print("Nenhuma categoria cadastrada.")
            else:
                for i, c in enumerate(cats, 1):
                    print(f"  {i}. {c.categoria}")
            nome = input("Nome da categoria a remover: ").strip()
            if nome:
                ctrl_cat.removerCategoria(nome)
            input("\nEnter para continuar...")

        elif op == "3":
            cats = ctrl_cat.listarCategorias()
            cabecalho("CATEGORIAS CADASTRADAS")
            if not cats:
                print("Nenhuma categoria cadastrada.")
            else:
                for i, c in enumerate(cats, 1):
                    print(f"  {i}. {c.categoria}")
            input("\nEnter para continuar...")

        elif op == "0":
            break


# ── ESTOQUE ────────────────────────────────────────

def menu_estoque():
    while True:
        cabecalho("ESTOQUE")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar estoque")
        print("0. Voltar")
        op = input("\nOpção: ").strip()

        if op == "1":
            nome = input("Nome do produto: ").strip()
            preco = input("Preço (ex: 5.99): ").strip()
            categoria = input("Categoria: ").strip()
            quantidade = input("Quantidade: ").strip()
            if nome and preco and categoria and quantidade:
                ctrl_est.adicionarProduto(nome, preco, categoria, quantidade)
            input("\nEnter para continuar...")

        elif op == "2":
            nome = input("Nome do produto a remover: ").strip()
            if nome:
                ctrl_est.removerProduto(nome)
            input("\nEnter para continuar...")

        elif op == "3":
            itens = ctrl_est.listarEstoque()
            cabecalho("ESTOQUE ATUAL")
            if not itens:
                print("Estoque vazio.")
            else:
                print(f"{'PRODUTO':<25} {'PREÇO':>8} {'CATEGORIA':<20} {'QTD':>5}")
                print("-" * 62)
                for i in itens:
                    print(f"  {i.produto.nome:<23} R${float(i.produto.preco):>7.2f}  {i.produto.categoria:<20} {i.quantidade:>5}")
            input("\nEnter para continuar...")

        elif op == "0":
            break


# ── VENDAS ─────────────────────────────────────────

def menu_vendas():
    while True:
        cabecalho("VENDAS")
        print("1. Registrar venda")
        print("2. Histórico de vendas")
        print("0. Voltar")
        op = input("\nOpção: ").strip()

        if op == "1":
            itens = ctrl_est.listarEstoque()
            if not itens:
                print("Estoque vazio! Adicione produtos antes de vender.")
                input("\nEnter para continuar...")
                continue
            print("\nProdutos disponíveis:")
            for i in itens:
                print(f"  - {i.produto.nome} | R$ {float(i.produto.preco):.2f} | Qtd: {i.quantidade}")
            produto = input("\nProduto: ").strip()
            vendedor = input("Vendedor (nome): ").strip()
            comprador = input("Comprador (nome): ").strip()
            quantidade = input("Quantidade: ").strip()
            if produto and vendedor and comprador and quantidade:
                ctrl_venda.realizarVenda(produto, vendedor, comprador, quantidade)
            input("\nEnter para continuar...")

        elif op == "2":
            vendas = ctrl_venda.listarVendas()
            cabecalho("HISTÓRICO DE VENDAS")
            if not vendas:
                print("Nenhuma venda registrada.")
            else:
                print(f"{'PRODUTO':<20} {'VENDEDOR':<15} {'COMPRADOR':<15} {'QTD':>4} {'DATA'}")
                print("-" * 70)
                for v in vendas:
                    print(f"  {v.itensVendidos.nome:<18} {v.vendedor:<15} {v.comprador:<15} {v.quantidadeVendida:>4}  {v.data}")
            input("\nEnter para continuar...")

        elif op == "0":
            break


# ── FORNECEDORES ───────────────────────────────────

def menu_fornecedores():
    while True:
        cabecalho("FORNECEDORES")
        print("1. Cadastrar fornecedor")
        print("2. Listar fornecedores")
        print("0. Voltar")
        op = input("\nOpção: ").strip()

        if op == "1":
            nome = input("Nome: ").strip()
            cnpj = input("CNPJ: ").strip()
            telefone = input("Telefone: ").strip()
            categoria = input("Categoria de produtos: ").strip()
            if nome and cnpj and telefone and categoria:
                ctrl_forn.cadastrarFornecedor(nome, cnpj, telefone, categoria)
            input("\nEnter para continuar...")

        elif op == "2":
            forns = ctrl_forn.listarFornecedores()
            cabecalho("FORNECEDORES CADASTRADOS")
            if not forns:
                print("Nenhum fornecedor cadastrado.")
            else:
                for f in forns:
                    print(f"  {f.nome} | CNPJ: {f.cnpj} | Tel: {f.telefone} | Cat: {f.categoria}")
            input("\nEnter para continuar...")

        elif op == "0":
            break


# ── CLIENTES ───────────────────────────────────────

def menu_clientes():
    while True:
        cabecalho("CLIENTES")
        print("1. Cadastrar cliente")
        print("2. Listar clientes")
        print("0. Voltar")
        op = input("\nOpção: ").strip()

        if op == "1":
            nome = input("Nome: ").strip()
            telefone = input("Telefone: ").strip()
            cpf = input("CPF: ").strip()
            email = input("E-mail: ").strip()
            endereco = input("Endereço: ").strip()
            if nome and telefone and cpf and email and endereco:
                ctrl_cli.cadastrarCliente(nome, telefone, cpf, email, endereco)
            input("\nEnter para continuar...")

        elif op == "2":
            clis = ctrl_cli.listarClientes()
            cabecalho("CLIENTES CADASTRADOS")
            if not clis:
                print("Nenhum cliente cadastrado.")
            else:
                for c in clis:
                    print(f"  {c.nome} | Tel: {c.telefone} | CPF: {c.cpf}")
            input("\nEnter para continuar...")

        elif op == "0":
            break


# ── FUNCIONÁRIOS ───────────────────────────────────

def menu_funcionarios():
    while True:
        cabecalho("FUNCIONÁRIOS")
        print("1. Cadastrar funcionário")
        print("2. Listar funcionários")
        print("0. Voltar")
        op = input("\nOpção: ").strip()

        if op == "1":
            clt = input("Registro CLT: ").strip()
            nome = input("Nome: ").strip()
            telefone = input("Telefone: ").strip()
            cpf = input("CPF: ").strip()
            email = input("E-mail: ").strip()
            endereco = input("Endereço: ").strip()
            salario = input("Salário (ex: 1800.00): ").strip()
            cargo = input("Cargo: ").strip()
            if all([clt, nome, telefone, cpf, email, endereco, salario, cargo]):
                ctrl_func.cadastrarFuncionario(clt, nome, telefone, cpf, email, endereco, salario, cargo)
            input("\nEnter para continuar...")

        elif op == "2":
            funcs = ctrl_func.listarFuncionarios()
            cabecalho("FUNCIONÁRIOS CADASTRADOS")
            if not funcs:
                print("Nenhum funcionário cadastrado.")
            else:
                for f in funcs:
                    print(f"  {f.nome} | Cargo: {f.cargo} | Salário: R$ {float(f.salario):.2f} | CLT: {f.clt}")
            input("\nEnter para continuar...")

        elif op == "0":
            break


# ── MENU PRINCIPAL ─────────────────────────────────

def main():
    init_files()
    while True:
        cabecalho("SISTEMA DE GESTÃO")
        print("1. Categorias")
        print("2. Estoque")
        print("3. Vendas")
        print("4. Fornecedores")
        print("5. Clientes")
        print("6. Funcionários")
        print("0. Sair")
        op = input("\nOpção: ").strip()

        if op == "1":
            menu_categorias()
        elif op == "2":
            menu_estoque()
        elif op == "3":
            menu_vendas()
        elif op == "4":
            menu_fornecedores()
        elif op == "5":
            menu_clientes()
        elif op == "6":
            menu_funcionarios()
        elif op == "0":
            limpar()
            print("Até logo!")
            break
        else:
            print("Opção inválida!")
            input("Enter para continuar...")


if __name__ == "__main__":
    main()
