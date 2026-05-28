from src.utils import lerFloat

class Escala:

    def __init__(self, medida, fator, opcao):
        self.medida = medida
        self.fator = fator
        self.opcao = opcao

    def converter_escala(self):
         
        if self.opcao == 1:
            return self.medida / self.fator
        elif self.opcao == 2:
            return self.medida * self.fator
        else:
            return -1



def receber_dados():

    print("\n--- Livarte | Conversor de Escalas ---")
    print("\nMenu de Escalas:")
    print("1 - Converter de real para desenho")
    print("2 - Converter de desenho para real")

    while True:
        try:
            opcao = int(input("\nDigite a opção da forma: "))
        except ValueError:
            print("Opção inválida. Só é aceito números inteiros, tente novamente.")
            continue

        if opcao == 1:
            medida = lerFloat("\nDigite a medida real (em metros): ")
            fator = lerFloat("\nDigite o fator da escala (ex: 1:50 → fator = 50): ")
            break


        elif opcao == 2:
            medida = lerFloat("\nDigite a medida do desenho (em metros): ")
            fator = lerFloat("\nDigite o fator da escala (ex: 1:50 → fator = 50): ")
            break

        else:
            print("Opção inválida. Digite '1' ou '2'.")

    return opcao, medida, fator