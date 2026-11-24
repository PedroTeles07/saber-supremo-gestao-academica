from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome = "", rg = "", cpf = "", nascimento = None, sexo = ""):
        self.__nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.__nascimento = nascimento
        self.__sexo = sexo 

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,valor):
        if valor.strip() == "":
            raise ValueError("Campo obrigatorio vazio!")
        else:
            self.__nome = valor

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, valor):
        if valor.strip() == "" or len(valor) != 8 or not valor.isdigit():
            raise ValueError("Campo obrigatorio vazio ou incorreto!")
        else:
            self.__rg = valor

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, valor):
        if valor.strip() == "" or len(valor) != 11 or not valor.isdigit():
            raise ValueError("Campo obrigatorio não preenchido!")
        else:
            self.__cpf = valor

    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, valor):
        self.validar_nascimento(valor)
        self.__nascimento = valor

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, valor):
        if valor.strip() == "" or (valor != "M" and valor != "F"):
            raise ValueError("Campo obrigatorio vazio ou incorreto!")
        else:
            self.__sexo = valor

    def validar_nascimento(self,nascimento, idade_minima=18):
        hoje = date.today()

        if nascimento > hoje:
            raise ValueError("A data não pode estar no futuro!")

        idade = hoje.year - nascimento.year
        if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
            idade -= 1

        if idade < idade_minima:
            raise ValueError(f"Usuario deve ter pelo menos {idade_minima} anos!")
        
    @abstractmethod
    def cadastrar(self):
        while True:
            try:
                self.nome = input("\nNome: ").strip()
                break
            except ValueError as erro:
                print(erro)

        while True:
            try:
                self.rg = input("\nRg[8 digitos]: ").strip()
                break
            except ValueError as erro:
                print(erro)

        while True:
            try:
                self.cpf = input("\nCpf[11 digitos]: ").strip()
                break
            except ValueError as erro:
                print(erro)

        while True:
            ano = input("\nAno nascimento: ").strip()
            mes = input("Mês nascimento: ").strip()
            dia = input("Dia nascimento: ").strip()

            try:
                self.nascimento = date(int(ano), int(mes), int(dia))
                break
            except ValueError as erro:
                print(erro)

        while True:
            try:
                self.sexo = input("\nSexo[M/F]: ").strip().upper()
                break
            except ValueError as erro:
                print(erro)     
        

    @abstractmethod
    def exibir(self):
        print(f"\nNome: {self.nome}")
        print(f"RG: {self.rg}")
        print(f"CPF: {self.cpf}")
        print(f"Nascimento: {self.nascimento.strftime('%d/%m/%Y')}")
        print(f"Sexo: {self.sexo}")
    
    
class Aluno(Pessoa):
    def __init__(self, nome = "", rg = "", cpf = "", nascimento = None, sexo = "", codigo = None, interesse = False, curso = "", desconto = 0.0):
        super().__init__(nome, rg, cpf, nascimento, sexo)
        self.__codigo = codigo
        self.__interesse = interesse
        self.__curso = curso
        self.__desconto = desconto

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        if not isinstance(valor, int) or isinstance(valor, bool) or valor <= 0:
            raise ValueError("Código deve ser um número inteiro positivo!")
        self.__codigo = valor

    @property
    def interesse(self):
        return self.__interesse

    @interesse.setter
    def interesse(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("Campo obrigatorio vazio ou incorreto!")
        else:
            self.__interesse = valor

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, valor):
        if valor.strip() == "":
            raise ValueError("Campo obrigatorio vazio!")
        else:
            self.__curso = valor

    @property
    def desconto(self):
        return self.__desconto

    @desconto.setter
    def desconto(self, valor):
        if (valor > 100 or valor < 0):
            raise ValueError("Campo obrigatorio vazio ou incorreto!")
        else:
            self.__desconto = valor

    def cadastrar(self):
        super().cadastrar()

        while True:
            texto = input("\nCódigo: ").strip()

            if not texto.isdigit():
                print("Código deve conter apenas números!")
                continue

            try:
                self.codigo = int(texto)
                break
            except ValueError as erro:
                print(erro)
        while True:
            resposta = input("\nPossui interesse em algum curso? [S/N]: ").strip().upper()
            if resposta in ("S", "N"):
                self.interesse = (resposta == "S")
                break
            print("Digite S ou N!")

        if self.interesse:
            while True:
                try:
                    self.curso = input("\nCurso: ").strip()
                    break
                except ValueError as erro:
                    print(erro)

        while True:
            texto = input("\nDesconto [0 se não tiver]: ").strip()
            try:
                self.desconto = float(texto)
                break
            except ValueError as erro:
                if "could not convert" in str(erro):
                    print("Digite um número válido!")
                else:
                    print(erro)  
                
    def exibir(self):
        super().exibir()
        print(f"Código: {self.codigo}")
        if self.interesse:
            print("Possui interesse em cursos: Sim")
            print(f"Curso: {self.curso}")
        print(f"Desconto: {self.desconto}%")

        
if __name__ == "__main__":
    lista_alunos = []
    while True:
        print("\n1-Cadastrar aluno\n2-Sair")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            aluno = Aluno()
            aluno.cadastrar()
            lista_alunos.append(aluno)
        elif opcao == "2":
            break
        else:
            print("Opção inválida!")

    for aluno in lista_alunos:
        aluno.exibir()
        print("-" * 40)
