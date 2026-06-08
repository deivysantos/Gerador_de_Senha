import random
import string
# Comando para gerar a minha senha
letras = string.ascii_letters
carac_especiais = string.punctuation
num = string.digits

# Quantidade de caracteres que eu irei querer pra gerar a minha senha
qtd_letras = int(input('Digite quantas letras você quer? '))
qtd_carc_especiais = int(input('Digite quantos caracteres especiais você quer? '))
qtd_num = int(input('Quantos números você quer? '))

senha = []

# Coloca a quantidade que eu quero para a minha senha
for _ in range(qtd_letras):
    senha.append(random.choice(letras))

for _ in range(qtd_carc_especiais):
    senha.append(random.choice(carac_especiais))

for _ in range(qtd_num):
    senha.append(random.choice(num))

# Embaralha a ordem dos caracteres para gerar a minha senha
random.shuffle(senha)

#Ordena a senha gerada numa unica string
senha_final = ''.join(senha)

print (senha_final)




