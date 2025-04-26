#Classe Aluno
class Aluno:
    #atributos encapsulados
    __matricula = 123
    __nome = "Maria"
    __cr = 8.5

    #construtor
    def __init__(self,matricula,nome,cr):
        self.__matricula = matricula
        self.__nome = nome
        self.__cr = cr

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, value):
        self.__matricula=value

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def cr(self):
        return self.__cr

    @cr.setter
    def cr(self, value):
        self.__cr = value

    def obterdados(self):
        return "Matrícula: " + str(self.__matricula) + "\tNome: " + self.__nome + "\tCR: " + str(self.__cr)