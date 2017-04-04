diasSemana = {}

def adicionarDia (posicao, dia):
  diasSemana[posicao]= dia
  
def exibirDia ():
  print(diasSemana)	

continuar = ("s")
while (continuar == 's'):  
  nomeDia = str(input("Qual é o dia ?"))
  numeroDia = input("Qual é a posição desejada ?")
  adicionarDia(numeroDia, nomeDia)
  continuar = str(input("Deseja adicionar mais dias ?(s / n )"))
exibirDia ()
