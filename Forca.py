from Palavra_Forca import palavra

letra_usuario = []
chances = 4
ganhou = False

while True:
    #criando a lógica
    
    for letra in palavra:
        if letra.lower() in letra_usuario:
            print(letra, end=' ')
        else:
            print("_", end=' ')
    print("")
    print(f"Você tem {chances} chances")
    
    tentativa = input("Escolha uma letra para advinhar: ")
    letra_usuario.append(tentativa.lower())
    
    if tentativa.lower() not in palavra.lower():
        chances -= 1    
    
    ganhou = True
    for letra in palavra:
        if letra.lower() not in letra_usuario:
            ganhou = False

    if chances == 0 or ganhou:
        break
    

if ganhou:
    print('=================================================')
    print(f"Parabéns, você ganhou!\nA palavra era {palavra} ")
else:
    print('======================================')
    print(f'Você perdeu!\nA palavra era {palavra}')