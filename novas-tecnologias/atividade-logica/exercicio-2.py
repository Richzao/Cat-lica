# 2 - O quadrado de um número natural n é dado pela soma dos n primeiros números ímpares consecutivos.
# ex: 1² = 1, 2² = 1 + 3, 3² = 1 + 3 + 5.
# Dado um número n, calcule seu quadrado usando a soma de ímpares ao invés de produto.

def calcula_quadrado(n):
    resultado = 0
    nmr_impar = 1
    for i in range(n):
        resultado += nmr_impar
        nmr_impar += 2
    return resultado

num = int(input("Digite o número: "))
resultado = calcula_quadrado(num)

print(resultado)