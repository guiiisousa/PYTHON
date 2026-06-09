class Pessoa:

    def __init__(self, nome, idade):
        if isinstance(nome, str):
            self._nome = nome

        if isinstance(idade, int):
            self._idade = idade
            
    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


    def apresentar(self):
        print(f"{self._nome} tem {self._idade} anos")

class Aluno(Pessoa):

    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        if isinstance(matricula, str):
            self._matricula = matricula

    @property
    def matricula(self):
        return self._matricula

    def apresentar(self):
        base = super().apresentar()
        print(f"{base} e é um aluno com a matrícula {self._matricula}")

class Professor(Pessoa):

    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        if isinstance(disciplina, str):
            self._disciplina = disciplina

    def apresentar(self):
        print(f"{self._nome} tem {self._idade} anos e é um professor da disciplina {self._disciplina}")
