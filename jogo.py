import random
def jogada(tent):
    randomNumber = random.randint(0, 100)
    guess = 101
    
    #TENTATIVA
    while guess != randomNumber:
        guess = int(input("Digite um número de 0 a 100: "))
        if guess > randomNumber:
            print("O número é menor que ", guess)
        elif guess < randomNumber:
            print("O número é maior que ", guess)
        tent.append(guess)
    return tent
    
#VARIAVEIS
tentativas = []
total_tentativas = []
again = "s"

#INTRODUCAO
print("Seja bem-vindo ao Jogo da Adivinhação!")
print("-----------------------------------")

#JOGANDO
while again != "n":
    tentativas = jogada(tentativas)
    total_tentativas.append(tentativas)
    print("-----------------------------------")
    print("Parabéns você acertou!")
    print("Você utilizou %d tentativas"%len(tentativas))
    again = input("Deseja continuar? (s/n) ")
    print("-----------------------------------")
    print()
    tentativas=[]
for i in range (0, len(total_tentativas), +1):
    print("Na %dª rodada foram feitas %d tentativas."%(i+1,len(total_tentativas[i])))