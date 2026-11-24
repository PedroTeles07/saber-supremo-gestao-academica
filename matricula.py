from abc import ABC
class Matricula:
    def __init__(self):
        self.__id = None
        self.__mesM = None
        self.__anoM = None
        
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, codigo):
        if codigo <= 0:
            raise ValueError("Código inválido!")
        self.__id = codigo

   
    @property
    def mesM(self):
        return self.__mesM

    @mesM.setter
    def mesM(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido!")
        self.__mesM = mes

    
    @property
    def anoM(self):
        return self.__anoM

    @anoM.setter
    def anoM(self, ano):
        if ano < 1:
            raise ValueError("Ano inválido!")
        self.__anoM = ano

    def Matricular(self):

        while True:
            try:
                codigo = int(input("\nCódigo do aluno: "))
                self.id = codigo
                break

            except ValueError as erro:
                print(erro)
                print("Digite um código válido!")

        while True:
            try:
                mes = int(input("\nMês da matrícula: "))
                self.mesM = mes
                break

            except ValueError as erro:
                print(erro)

        while True:
            try:
                ano = int(input("\nAno da matrícula: "))
                self.anoM = ano
                break

            except ValueError as erro:
                print(erro)

        print("Matrícula realizada com sucesso!")

    def ExibirMatricula(self):
        print("\n--- DADOS DA MATRÍCULA ---")
        print(f"ID do aluno: {self.id}")
        print(f"Mês da matrícula: {self.mesM}")
        print(f"Ano da matrícula: {self.anoM}")
