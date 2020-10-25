# Write your code here
import random

lista = ['python', 'java', 'kotlin', 'javascript']
letras = "abcdefghijklmnopqrstuvwxyz"
letras = list(letras)

random.seed()
choice1 = random.randint(0, 3)
print('H A N G M A N')
comp_palavra = len(lista[choice1])
palavra = lista[choice1]
adivinhar = []

while True:
    choice2 = input('Type "play" to play the game, "exit" to quit: ')
    while choice2 != 'play' and choice2 != 'exit':
        choice2 = input('Type "play" to play the game, "exit" to quit: ')
        #if choice2 != 'exit' or choice2 != 'play':
        #    break


    # print(palavra)
    # print(comp_palavra)
    if choice2 == 'play':
        for i in range(comp_palavra):
            adivinhar += "-"
    # print(adivinhar)
        flag = False
        lista_tentativas = ''
        while '-' in adivinhar or flag:

            i = 0
            while i < 8:
                #print(  'i: ',i)

        #for i in range(8):
                adivinhar = "".join(adivinhar)
                print()
                print(adivinhar)
                choice = input('Input a letter: ')

                if choice == '':
                    print("No such letter in the word")

                elif len(choice) != 1:
                    print("You should input a single letter")

                elif not choice.isalpha():
                    print("It is not an ASCII lowercase letter")

                elif choice not in letras:
                    print("It is not an ASCII lowercase letter")
                elif choice in lista_tentativas:
                    print("You already typed this letter")

                elif choice in palavra:

                    #   contador = palavra.count(choice)

                    encontradas = []
                    for j in range(len(palavra)):
                        if palavra[j] == choice:
                            encontradas.append(j)

                    adivinhar = list(adivinhar)
                    for j in encontradas:
                        adivinhar[j] = choice
             #           print(list(palavra))
             #           print(adivinhar)

                    if list(palavra) == adivinhar:
                        break

                    lista_tentativas += choice
                    print()

                else:
                    print("No such letter in the word")
                    lista_tentativas += choice
                    i += 1




         #   print('''Thanks for playing!\nWe'll see how well you did in the next stage''')
            break
        # if '-' not in adivinhar:
        #print("Thanks for playing!\nWe'll see how well you did in the next stage")


        if list(palavra) == adivinhar:
            print("You guessed the word %s!\nYou survived!" % palavra)
        else:
            print("You lost!\n")

    elif choice2 ==  'exit':
        break

