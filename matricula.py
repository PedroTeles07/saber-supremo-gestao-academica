
class Matricula:
    def __init__(self):
        self.__mesM = None
        self.__anoM = None
        self.__id = None

    def Matricular(self, lista_matriculas):
        while True:
            try:
                codigo = int(input("\nCódigo do aluno: "))

                if codigo <= 0:
                    print("Código inválido!")
                    continue

                repetido = False

                for matricula in lista_matriculas:
                    if matricula.__id == codigo:
                        repetido = True
                        break

                if repetido:
                    print("Este aluno já possui matrícula!")
                    continue

                self.__id = codigo
                break

            except ValueError:
                print("Digite um código válido!")

        while True:
            try:
                mes = int(input("\nMês da matrícula: "))
                ano = int(input("Ano da matrícula: "))

                if mes < 1 or mes > 12:
                    print("Mês inválido!")
                    continue

                if ano < 1:
                    print("Ano inválido!")
                    continue

                self.__mesM = mes
                self.__anoM = ano

                print("Matrícula realizada com sucesso!")
                break

            except ValueError:
                print("Digite valores numéricos válidos!")

    def ExibirMatricula(self):
        print("\n--- DADOS DA MATRÍCULA ---")
        print(f"ID do aluno: {self.__id}")
        print(f"Mês da matrícula: {self.__mesM}")
        print(f"Ano da matrícula: {self.__anoM}")


if __name__ == "__main__":

    lista_matriculas = []

    while True:
        print("\n1 - Cadastrar matrículas")
        print("2 - Exibir matrículas")
        print("3 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            matricula = Matricula()
            matricula.Matricular(lista_matriculas)

            lista_matriculas.append(matricula)

        elif opcao == "2":

            if len(lista_matriculas) == 0:
                print("\nNenhuma matrícula cadastrada!")
            else:
                for matricula in lista_matriculas:
                    matricula.ExibirMatricula()

        elif opcao == "3":
            print("Encerrando programa...")
            break

        else:
            print("Opção inválida!")
