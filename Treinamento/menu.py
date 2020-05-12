## programa Menu

def menu():

    x = int(input("Digite uma opção: "))

    if (x == 1):
        print("Vc escolheu 1")
    if (x == 2):
        print("Vc escolheu 2")
    if (x == 3):
        print("Vc escolheu 3")
    if (x > 3):
        print("Escolha um numero ate 3")
    
## Inicio do programa
menu() ## chama aa função menu
