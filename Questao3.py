Produtos = {}

def cadastrarProduto(Produtos,Produto,Valor):
  Produtos[Produto]= Valor
  
def exibirProdutos(lista):
  for i in lista:
    print("Seu produto é:" ,i, "Seu valor é:", Produtos[i])
    
def removerProduto(Produtos,Produto):
  del Produtos[Produto]
  print(Produtos)
  
def exibirBaratoProduto(Produtos):
  aux = False
  titulo = ""
  for i in Produtos:
    if aux == False:
      minimo = Produtos[i]
      titulo = i
      aux = True
    if Produtos[i] < minimo:
      minimo = Produtos[i]
      titulo = i
  return titulo

def exibirCaroProduto(Produtos):
  maximo = 0
  for i in Produtos:
    if Produtos[i] > maximo :
      maximo = Produtos[i]
      titulo = i
  return i

def menu():
  aux = 's'
  while(aux == 's'):
    opcao = int(input("O que você quer ?\n1 - Adicionar produto ?\n2 - Mostrar o produtos ?\n3 - Remover o produto ?\n4 - Mostrar o mais caro ?\n5 - Mostar o mais barato ?\n6 - Terminar.\n"))

    if(opcao == 1):
      Produto = str(input("Diga o nome do produto:"))
      Valor = float(input("Diga o valor do produto:"))
      cadastrarProduto(Produtos, Produto, Valor)
    elif(opcao == 2):
      cont = 's'
      lista = []
      while(cont == 's'):
        Pro = str(input("Diga o nome do produto:"))
        lista.append(Pro)
        aux = str(input("Adicionar mais produtos ?"))
      exibirProdutos(lista)
    elif(opcao == 3):
      Pro = str(input("Diga o nome do produto:"))
      removerProduto(Produtos,Produto)
    elif(opcao == 4):
      print(exibirCaroProduto(Produtos))
    elif(opcao == 5):
      print(exibirBaratoProduto(Produtos))
    elif(opcao == 6):
      aux = "nao"
      print("Obrigada")
    else:
        print("Opcao inválida, comece novamente")
menu()
