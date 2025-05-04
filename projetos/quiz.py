print("Seja bem vindo ao quiz do Yago!")
answer_user = input("Deseja começar? S/N: ")

if answer_user.upper() != "S":
    quit()

score = 0

print("Começando...\n")

# Primeira Pergunta
print("Qual menor país do mundo? \n A) Mônaco \n B) Malta \n C) Vaticano \n D) China")
answer_1 = input("Resposta: ")

if answer_1.upper() == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

# Segunda Pergunta
print("Qual maior país do mundo? \n A) Estados Unidos \n B) Rússia \n C) Austrália \n D) Brasil")
answer_2 = input("Resposta: ")

if answer_2.upper() == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

# Terceira Pergunta
print("Atualmente, quantos elementos químicos a tabela periódica possui? \n A) 113 \n B) 109 \n C) 108 \n D) 118")
answer_3 = input("Resposta: ")

if answer_3.upper() == "D":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

# Quarta Pergunta
print("Qual maior animal terrestre? \n A) Baleia Azul \n B) Dinossauro \n C) Elefante africano \n D) Girafa")
answer_4 = input("Resposta: ")

if answer_4.upper() == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print(f"Quiz acabou... Pontuação: {score}/4")
