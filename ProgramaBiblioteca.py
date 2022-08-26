# Registro de nome, tia e os livros
# Nome:Humberto Rodrigues neto
# Prog. Biblioff
# 20/08/2018 10:05


nome = str(input("Digite nome do aluno: "))
tia = int(input("Digite o tia do aluno: "))
livro = int(input("Digite o exemplar do livro: "))    
print("menu: ")
print("(1)tem mais livros")
print("(2)não tem mais livros")
op = input("escolha uma opção: ")
if op == "1" or op == "2":
   opcao_valida = False 
     
if op == "1":
  livro2 = int(input("Digite o exemplar do livro2: "))
elif   op == "2":
  print("ok bom estudo")
  print("Nome:",(nome),"tia:",(tia),"livro1:",(livro))


print("menu: ")
print("(1)tem mais livros")
print("(2)não tem mais livros")
op = input("escolha uma opção: ")
if op == "1" or op == "2":
   opcao_valida = False

if op == "1":
  livro3 = int(input("Digite o exemplar do livro3: "))
elif op == "2":
  print("ok bom estudo")
  print("Nome:",(nome),"tia:",(tia),"livro1:",(livro), "livro2:",(livro2), "livro3",(livro3)) 
  
  # print ("Nome:",(nome),"tia:",(tia),"livro1:"
 # livro3 = int(input("Digite o exemplar do livro3: "))
#livro4 = int(input("Digite o exemplar do livro4: "))
#livro5 = int(input("Digite o exemplar do livro5: "))
#livro6 = int(input("Digite o exemplar do livro6: "))
#print ("Nome:",(nome),"tia:",(tia),"livro1:",(livro), "livro2:",(livro2),"livro3:",(livro3),"livro4:",(livro4), "livro5:",(livro5),"livro6:",(livro6))
