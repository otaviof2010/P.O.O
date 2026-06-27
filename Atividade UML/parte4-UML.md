classDiagram

class Escola
class Turma
class Professor
class Aluno
class Avaliacao

Escola o-- "1..*" Turma : possui

Turma --> "1" Professor : responsavel

Turma o-- "0..*" Aluno : matricula

Turma *-- "0..*" Avaliacao : cria