## programa teste

def media():
    aluno = input("Digite o nome do Aluno: ")
    nota = 0

    for i in range(1,5):
        nota += float(input("Digite nota " + str(i) + ": " ))

    media = nota/4 ## calcula media
    
    if( media >= 7 ): ## verifica se a media e maior que 7
        print( aluno,"sua media é:", media, "Vc foi aprovado" )
    else:
        print( aluno,"sua media é:", media, "Vc foi reprovado" )      

## Inicio do programa
media() ## chama a função media