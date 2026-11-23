from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):
    def __init__(self):
        self._nome = ""
        self._rg = ""
        self._cpf = ""
        self._nascimento = None
        self._sexo = ""
    @abstractmethod
    def Cadastrar(self):
        pass
    @abstractmethod
    def Exibir(self):
        pass
    
    
class Aluno(Pessoa):
    def __init__(self):
        super().__init__()
        self.__codigo = None
        self.__interesse = False
        self.__curso = None
        self.__desconto = 0.0
        
    def Cadastrar(self):
        while True:
            self._nome = input("\nNome: ")
            if self._nome.strip() == "":
                print("Campo obrigatorio não preenchido!")
            else:
                print("Nome cadastrado!")
                break
        
        while True:
            self._rg = input("\nRG: ")
            if self._rg.strip() == "" or len(self._rg) != 8 or not self._rg.isdigit():
                print("Dado invalido ou vazio!")
            else:
                print("RG cadastrado!")
                break
            
        while True:
            self._cpf = input("\nCPF: ")
            if self._cpf.strip() == "" or len(self._cpf) != 11 or not self._cpf.isdigit():
                print("Dado invalido ou vazio!")
            else:
                print("Cpf cadastrado!")
                break
        
        while True:
            try:
                ano = input("\nAno nascimento: ").strip()
                mes = input("Mês nascimento: ").strip()
                dia = input("Dia nascimento: ").strip()
                
                if (ano == "") or (mes == "") or (dia ==""):
                    print("Campos obrigatorios não preenchido!")
                    continue
                else:
                    ano = int(ano)
                    mes = int(mes)
                    dia = int(dia)
                    
                nascimento = date(ano, mes, dia)
                
                hoje = date.today()
                idade = hoje.year - ano
                
                if (hoje.month, hoje.day) < (mes, dia):
                    idade -= 1
                
                if idade < 18:
                    print("Aluno deve ter pelo menos 18 anos!")
                    continue
                
                self._nascimento = nascimento
                print("Data de nascimento cadastrada!")
                break
                
            except ValueError:
                print("Data inválida! Verifique os valores informados.")
            
        while True:
            self._sexo = input("\nSexo[M/F]:").upper().strip()
            
            if self._sexo == "" or (self._sexo != "M" and self._sexo != "F"):
                print("Dado invalido ou vazio!")
            else:
                print("Sexo cadastrado!")
                break
        
        while True:
            try:
                self.__codigo = input("\nCodigo aluno: ").strip()
                if self.__codigo == "":
                    print("Campo obrigatorio não preenchido!")
                    continue
                
                self.__codigo = int(self.__codigo)
                
                if self.__codigo <= 0:
                    print("Dado invalido!")
                else:
                    print("Codigo aluno cadastrado!")
                    break
            except ValueError:
                print("Codigo invalido! Use apenas numeros inteiros nao nulos")
                
        while True:
            interesse = input("\nPossui interesse em algum curso?[S/N]: ").upper().strip()
            
            if interesse == "":
                print("Campo obrigatorio não preenchido!")
                continue
            
            if interesse == "S":
                self.__interesse = True
                
                while True:
                    #para quem fizer a parte de curso, precisa adicionar a funcao de exibir aqui.
                    #isso é importante para que o usuario saiba quais cursos estão disponíveis e possa escolher um.
                    self.__curso = input("\nNome do curso: ").strip()
                    
                    if self.__curso == "":
                        print("Campo obrigatorio não preenchido!")
                    else:
                        print("Curso cadastrado!")
                        break
                break
            elif interesse == "N":
                self.__interesse = False
                self.__curso = None
        
                print("Aluno cadastrado sem interesse em cursos!")
                break
        
            else:
                print("Resposta inválida! Digite S ou N.")
                
        while True:
            try:
                desconto = input("\nDesconto[0 caso nao tenha]: ").strip()
                
                if desconto == "":
                    print("Campo obrigatorio nao preenchido!")
                    continue
                else:
                    self.__desconto = float(desconto.replace(",","."))
                    
                    if self.__desconto < 0 or self.__desconto >= 100:
                        print("Desconto invalido!")
                    else:
                        print("Desconto cadastrado!")
                        break
            except ValueError:
                print("Valor invalido! Use apenas numeros inteiros/decimais.")
                
    def Exibir(self):
        print(f"\n\nAluno(a): {self._nome}")
        print(f"RG: {self._rg}")
        print(f"Cpf: {self._cpf}")
        print(f"Data de nascimento: {self._nascimento}")
        print(f"Sexo: {self._sexo}")
        print(f"Codigo: {self.__codigo}")
        
        if self.__interesse:
            print("Possui interesse em cursos: Sim")
            print(f"Curso: {self.__curso}")
            
        print(f"Desconto: {self.__desconto}%")


class Coordenador(Professor):
    BONIFICACAO = 0.15

    def __init__(self) -> None:
        super().__init__()
        self.__area = ""
        self.__plusSalario = 0.0

    def cadastrarCoordenadorProf(self) -> None:
        super().Cadastrar()

        while True:
            self.__area = input("\nArea de coordenacao: ").strip()
            if self.__area == "":
                print("Campo obrigatorio não preenchido!")
            else:
                print("Area cadastrada!")
                break

        self.calcularPlusSalario()

    def exibirCoordenadorProf(self) -> None:
        super().Exibir()
        print(f"Area de coordenacao: {self.__area}")
        print(f"Bonificacao (15%): R$ {self.__plusSalario:.2f}")

    def calcularPlusSalario(self) -> float:
        self.__plusSalario = round(self.getSalarioBruto() * Coordenador.BONIFICACAO, 2)
        return self.__plusSalario

    def Cadastrar(self) -> None:
        self.cadastrarCoordenadorProf()

    def Exibir(self) -> None:
        self.exibirCoordenadorProf()


class CoordenadorAdm(Funcionario):
    BONIFICACAO = 0.135

    def __init__(self) -> None:
        super().__init__()
        self.__area = ""
        self.__plusSalario = 0.0

    def cadastrarCoordenadorAdm(self) -> None:
        super().Cadastrar()

        while True:
            self.__area = input("\nArea de coordenacao: ").strip()
            if self.__area == "":
                print("Campo obrigatorio não preenchido!")
            else:
                print("Area cadastrada!")
                break

        self.calcularPlusSalario()

    def exibirCoordenadorAdm(self) -> None:
        super().Exibir()
        print(f"Area de coordenacao: {self.__area}")
        print(f"Bonificacao (13,5%): R$ {self.__plusSalario:.2f}")

    def calcularPlusSalario(self) -> float:
        self.__plusSalario = round(self.getSalarioBruto() * CoordenadorAdm.BONIFICACAO, 2)
        return self.__plusSalario

    def Cadastrar(self) -> None:
        self.cadastrarCoordenadorAdm()

    def Exibir(self) -> None:
        self.exibirCoordenadorAdm()

        
if __name__ == "__main__":
    # programa principal provisorio para testes
    lista_alunos = []
    while True:
        print("1-Cadastrar aluno;\n2-Sair;")
        opcao = int(input("Opcao: "))
        if opcao == 1:
            aluno = Aluno()
            aluno.Cadastrar()
            lista_alunos.append(aluno)
            
        elif opcao == 2:
            break
    for aluno in lista_alunos:
        aluno.Exibir()
        print("-" * 40)

