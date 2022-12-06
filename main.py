import sympy as sy
from sympy import *
import os
import time


def calculadora():
    os.system("cls")
    #  variavel de integração
    print("|-----------------------------------------------------|\n")
    print("*********          Executar Calculo           *********\n")
    print("|-----------------------------------------------------|\n")

    variavel_integracao = sy.Symbol(input('Insira a variavel de integração: '))
    #  função a ser integrada
    integral_funcao = input("\nFunção a ser integrada: ")
    #  integração inferior
    integracao_inferior = input("\nLimite de integração inferior:")
    #  integração superior
    integracao_superior = input("\nLimite de integração superior:")

    if (integracao_inferior and integracao_superior != None):
        sy.preview(
            f"${sy.latex(Integral(integral_funcao, (variavel_integracao, integracao_inferior, integracao_superior)))} = {sy.latex(sy.integrate(integral_funcao, (variavel_integracao, integracao_inferior, integracao_superior)))}$",
            output="png")
    else:
        sy.preview(
            f"${sy.latex(Integral(integral_funcao, (variavel_integracao)))} = {sy.latex(sy.integrate(integral_funcao, (variavel_integracao)))} + C$",
            output="png")


def main():
    reset = 0
    while (reset == 0):
        os.system("cls")
        print("|-----------------------------------------------------|\n")
        print("********* Calculadora de Integrais do Grupo 5 *********\n")
        print("|-----------------------------------------------------|\n")
        print(
            "Código feito para ser apresentado à professora Adriana Nogueira :D\n"
        )
        print("[1] - Executar Calculo\n")
        print("[2] - Sair\n")
        escolha = input(">> ")
        if (escolha == '1'):
            calculadora()
        elif (escolha == '2'):
            print("Até a próxima!")
            time.sleep(3)
            return
        else:
            print("Escolha invalida. Tente novamente...")
            time.sleep(3)


main()
