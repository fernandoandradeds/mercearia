from Models import Categoria, Estoque, Produtos, Fornecedor, Pessoa, Funcionario, Venda
from DAO import DaoCategoria, DaoEstoque, DaoFornecedor, DaoPessoa, DaoFuncionario, DaoVenda
from datetime import datetime

class ControllerCategoria:

    def cadastrarCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
                
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print("Categoria cadastrada com sucesso!")
        else:
            print("Categoria já existe!")

    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))
        if len(cat) <= 0:         
            print("Categoria não existe!")
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print("Categoria removida com sucesso!")

            with open('categoria.txt', 'w') as file:
                for i in x:
                    file.writelines(i.categoria)
                    file.writelines('\n')
