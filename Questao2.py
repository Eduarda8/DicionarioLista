Funcionarios = {}

def adicionarFuncionario (matricula, nome):
  Funcionarios[matricula] = nome

def exibirFuncionario ():
  print(Funcionarios)

continuar = 's'
while(continuar == 's'):
  nome = str(input("Digite o nome do seu funcionário:"))
  matricula = int(input("Digite a matrícula do funcinário :"))
  adicionarFuncionario(matricula, nome)
  continuar = str(input("Deseja adicionar mais Funcionarios ? (s/n)"))
  if (continuar == 's'):
    Funcionarios[matricula] = nome

exibirFuncionario ()

def buscarFuncionario (nome):
  for i in Funcionarios:
    if Funcionarios[i]== nome:
      return Funcionarios[i]
