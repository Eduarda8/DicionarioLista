Turmas = {}

def consulta():
    opcao = int(input("1- Turmas\n2- Alunos\n3- Aluno"))
    if(opcao == 1):
        print(turmas)
    elif(opcao == 2):
        Nota_Turma = str(input("Qual o nome da turma :"))
        print(turmas[Nota_Turma])
    elif(opçao == 3):
        Nota_Turma = str(input("Qual o nome da turma :"))
        mat = str(input("Qual a matricula do aluno :"))
        print(turmas[Nota_Turma][mat])
def adicionarAlunoNotas():
    Nota_Turma = str(input("Qual a matricula do aluno :"))
    alunos = {}
    mat = str(input("Diga a matricula"))
    NTS = []
    cont = 'sim'
    while (cont == 'sim'):
        nota = float(input("Digite a nota do aluno :"))
        nota.append(nota)
        cont = str(input("Adicionar mais notas ?"))
    turmas[Nome_turma][mat] = notas

def adicionarTurma():
    name = str(input("Qual o nome da turma ?"))
    alunos = {}
    turmas[name]= alunos
def calcularMedia(notas):
    soma = 0
    for i in notas :
        soma +=i
    return soma/len(notas)

def mediaTurma():
    soma = 0
    Con = 0
    Nome_turma = str(input("Qual o nome da turma"))
    for i in turmas[Nome_Turma]:
        soma += calcularMedia(turmas[Nota_Turma][i])
        con +=1
    return soma/con
    
def menu():
    aux = 'sim'
    While aux == 'sim':
        opcao = int(input("O que você deseja ?\n1- Adicionar a turma :\n2- Adicionar o aluno e as notas :\n3- Calcular média de um aluno :\n4- Calcular média de uma turma :\n5- Sair\n"))
        if(opcao == 1) :
            AdicionarTurma()
        elif(opcao == 2):
            AdicionarAlunosNotas()
        elif(opcao == 3):
            turma = str(input("Digite o nome da turma;"))
            mat = str(input("Digite a matricula"))
            print(calcularMedia(turmas[turma][mat]))
        elif(opcao == 4):
            print(mediaTurma())
        elif(opcao == 5):
            print(mediaTurma())
        elif(opcao == 6):
            Continuar = 'nao'

menu()
