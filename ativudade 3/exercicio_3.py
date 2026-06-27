import main as m

'''
print ('Questão - 1')
class Figurinha:
    def __init__(self,numero,tema):
        
        self.numero = numero
        self.tema = tema

    def mostrar(self):
        return (f'figurinha - {self.numero},{self.tema}')



class Pacotinho:
    def __init__(self):
        self.Figurinha = []

    def adicionar(self,figurinha_escolhida):
        self.Figurinha.append(figurinha_escolhida)
    
    def listar(self):
        for i in range(len(self.Figurinha)):
            print(f'figurinha - {self.Figurinha[i].numero}, {self.Figurinha[i].tema}')



class Minhacolecao:

    def __init__(self):
        self.album = []
    
    def colar(self,pacote):
        while pacote.Figurinha:
            fig = pacote.Figurinha.pop()
            self.album.append(fig)
        

    def faltantes(self, total):
        qtd = len(self.album)
        return f'faltam {total - qtd} figurinhas'
    
    def mostrar_album(self):
        for fig in self.album:
            print(f'figurinha - {fig.numero}, {fig.tema}')
'''

'''
print ('Questão - 2')

class Aluno:
    def __init__(self,nome,nota):
        self.nome = nome
        self.nota = nota
        
    def aprovado(self):
        return self.nota >= 6




class Professores:
    def __init__(self,nome):
        self.nome = nome
        self.alunos = []
        

    def adicionar_aluno(self,aluno):
        self.alunos.append(aluno)
        
        
    def media_da_turma(self):
        if len(self.alunos) == 0:
            return 0

        soma = 0
        for aluno in self.alunos:
            soma += aluno.nota

        return soma/len(self.alunos)

    def aprovados(self):
        for aluno in self.alunos:
            if aluno.nota >= 6:
                print (aluno.nome)





class Escola:
    def __init__(self,nome):
        self.escola = []
        self.nome = nome

    def adicionar_professor(self,professor):
        self.escola.append(professor)

    def relatorio_geral(self):
        for prof in self.escola:
            
            print(f'Professor: {prof.nome}')
            print(f'Alunos: {len(prof.alunos)}')
            
            if len(prof.alunos) > 0:
                print(f'Média: {prof.media_da_turma():}')
            else:
                print('Média: 0')


'''