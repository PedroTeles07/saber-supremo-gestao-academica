
class Curso:
    def __init__(self):
        self.__titulo = None
        self.__descricao = None
        self.__valor = 0.0
        self.sala = None

    def cadastrarCurso(self):

        while True:
            self.__titulo = input("\nTítulo do curso: ").strip()

            if self.__titulo == "":
                print("Campo obrigatório não preenchido!")
            else:
                print("Título cadastrado!")
                break

        while True:
            self.__descricao = input("\nDescrição do curso: ").strip()

            if self.__descricao == "":
                print("Campo obrigatório não preenchido!")
            else:
                print("Descrição cadastrada!")
                break

        while True:
            try:
                self.__valor = float(input("\nValor do curso: ").replace(",", "."))

                if self.__valor <= 0:
                    print("Valor inválido!")
                else:
                    print("Valor cadastrado!")
                    break

            except ValueError:
                print("Digite um valor válido!")

        while True:
            self.sala = input("\nSala do curso: ").strip()

            if self.sala == "":
                print("Campo obrigatório não preenchido!")
            else:
                print("Sala cadastrada!")
                break

    def exibirCurso(self):
        print("\n--- DADOS DO CURSO ---")
        print(f"Título: {self.__titulo}")
        print(f"Descrição: {self.__descricao}")
        print(f"Valor: R$ {self.__valor:.2f}")
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
