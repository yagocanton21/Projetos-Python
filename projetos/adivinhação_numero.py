import random

print("Seja muito bem vindo!!")
choice_number = input("Digite o número teto do desafio: ")

# Verificão
if choice_number.isdigit():
   choice_number = int(choice_number)
else:
   print("Erro: valor informado não é numérico. Favor execute novamente e informe um número!!")
   quit()   

random_number = random.randint(0, choice_number)

n_choices = 0

#  Looping de tentativa
while True:
   answer_user = input("Adivinhe um número: ")
   
   if answer_user.isdigit():
       answer_user = int(answer_user)
   else:
      print("Erro: valor informado não é numérico. Favor informe um número")
      continue

   n_choices = n_choices + 1
   
   if answer_user == random_number:
      print("Parabéns, voçê acertouu!")
      break
   elif answer_user > random_number:
      print("Passou longe, o número a ser descoberto é menor que este..")
   else:
      print("Chutou baixo, o número a ser descoberto é maior que este..")

print(f"Numero de tentativas: {n_choices}")

