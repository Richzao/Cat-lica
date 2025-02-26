# 3 - Defina uma função recursiva para calcular a soma de dois naturais usando as funções "suc(n)" e "pred(n)"
#  que devolvem, respectivamente, o sucessor e o predecessor de um natural n.

def suc(n):
    return n + 1

def pred(n):
    return n - 1

def soma(a, b):
    if b == 0:
        return a
    else:
        return suc(soma(a, pred(b)))
    
print (soma(5, 6))