from mult.py import mutiplicacao()
from divis.py import divisão()
def soma():
    n1 = int(input("me informe o primeiro valor"))
    n2 = int(input("me informe o segundo valor\n"))
    a = (n1 + n2)
    print(a)

def subtração():
    n1 = int(input("me informe o primeiro valor"))
    n2 = int(input("me informe o segundo valor\n"))
    b = (n1 - n2)
    print(b)


while True:
    print("bem-vindo á calculadora!")
    escolha = int(input("Escolha que função deseja utilizar: \n1- soma \n2- subtração \n3- multiplicação \n4- divisão \n"))
    if escolha == 1:
        soma()
    if escolha == 2:
        subtração()
    if escolha == 3:
        multiplicacao()
    if escolha == 4:
        divisão()