# 1 - Escreva um app que insere um número consistindo em cinco dígitos do usuário, separa o número em seus dígitos individuais e imprime os dígitos separados por 3 espaços cada.
# ex: 42339 -> 4   2   3   3   9

num = input("Digite o número de 5 dígitos: ")
lista_num = []

if len(num) != 5:
    print("Insira um número válido!")

for n in num:
    lista_num.append(n)

resultado = '   '.join(lista_num)
print(resultado)