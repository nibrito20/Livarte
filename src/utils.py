def lerFloat(mensagem): 
    while True:
        entrada = input(mensagem)
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.")
