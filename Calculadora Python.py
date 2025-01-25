#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def soma(x, y): return x + y
def subtrair(x, y): return x - y
def multiplicar(x, y): return x * y
def dividir(x, y): return 'Erro: divisão por zero.' if y == 0 else x / y

def calc():
    operacoes = {'somar': soma, 'subtrair': subtrair, 'multiplicar': multiplicar, 'dividir': dividir}
    while True:
        escolha = input('Escolha: somar, subtrair, multiplicar ou dividir (ou "sair" para encerrar): ').lower()
        if escolha == 'sair':
            print('Encerrando o programa')
            break
        if escolha in operacoes:
            x = float(input('Primeiro número: '))
            y = float(input('Segundo número: '))
            print(f'Resultado: {operacoes[escolha](x,y)}')
        else:
            print('Operação inválida')

calc()


# In[ ]:





# In[ ]:





# In[ ]:




