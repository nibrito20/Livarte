import os
from src.forma import *
from src.escala import *
from src.orcamento import *
from src.grafico import *


if __name__ == "__main__":
    os.system("clear")
    print("Olá! Bem-vindo ao Livarte.")

    while True:
        print("_______________________________")
        print("\nMenu de Opções:")
        print("1 - Calculadora de Áreas")
        print("2 - Conversor de Escalas")
        print("3 - Gerador de Orçamento Básico")
        print("4 - Gráficos de Projeto")
        print("5 - Encerrar")

        while True:
            try:
                opcao = int(input("\nDigite uma opção: "))
                break
            except ValueError:
                print("Opção inválida! Só é aceito números inteiros, tente novamente.")

        if opcao == 1:

            forma = menu_areas()
            medidas = receber_valores(forma)
            f = Forma(forma, medidas)
            print(f.calcular_area())

        elif opcao == 2:

            opcao, medida, fator = receber_dados()
            e = Escala(medida, fator, opcao)
            print(e.converter_escala())

        elif opcao == 3:
            gerenciar_orcamento()
            
        elif opcao == 4:
            gerar_grafico()

        elif opcao == 5:
            print("\nEncerrando...")
            break
        else:
            print("\nOpção inválida. Digite um número inteiro entre 1 e 5.")