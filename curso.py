from abc import ABC
class Curso:
    def __init__(self):
        self.__titulo = None
        self.__descricao = None
        self.__valor = 0.0
        self.__sala = None

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, valor_titulo):
        if not valor_titulo or not valor_titulo.strip():
            raise ValueError("Campo obrigatório não preenchido!")
        self.__titulo = valor_titulo.strip()

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor_descricao):
        if not valor_descricao or not valor_descricao.strip():
            raise ValueError("Campo obrigatório não preenchido!")
        self.__descricao = valor_descricao.strip()

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, novo_valor):
        if novo_valor <= 0:
            raise ValueError("Valor inválido!")
        self.__valor = novo_valor

    @property
    def sala(self):
        return self.__sala

    @sala.setter
    def sala(self, nova_sala):
        if not nova_sala or not nova_sala.strip():
            raise ValueError("Campo obrigatório não preenchido!")
        self.__sala = nova_sala.strip()

    def cadastrarCurso(self):
        while True:
            try:
                self.titulo = input("\nTítulo do curso: ")
                print("Título cadastrado!")
                break
            except ValueError as erro:
                print(erro)

        while True:
            try:
                self.descricao = input("\nDescrição do curso: ")
                print("Descrição cadastrada!")
                break
            except ValueError as erro:
                print(erro)

        while True:
            try:
                preco = float(input("\nValor do curso: ").replace(",", "."))
                self.valor = preco
                print("Valor cadastrado!")
                break
            except ValueError as erro:
                if str(erro) == "Valor inválido!":
                    print(erro)
                else:
                    print("Digite um valor válido!")

        while True:
            try:
                self.sala = input("\nSala do curso: ")
                print("Sala cadastrada!")
                break
            except ValueError as erro:
                print(erro)

    def exibirCurso(self):
        print("\n--- DADOS DO CURSO ---")
        print(f"Título: {self.titulo}")
        print(f"Descrição: {self.descricao}")
        print(f"Valor: R$ {self.valor:.2f}")
        print(f"Sala: {self.sala}")


if __name__ == "__main__":
    lista_cursos = []

    while True:
        print("\n1 - Cadastrar Cursos")
        print("2 - Exibir Cursos")
        print("3 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            curso = Curso()
            curso.cadastrarCurso()
            lista_cursos.append(curso)

        elif opcao == "2":
            if len(lista_cursos) == 0:
                print("Nenhum curso cadastrado!")
            else:
                for curso in lista_cursos:
                    curso.exibirCurso()

        elif opcao == "3":
            break

        else:
            print("Opção inválida!")
