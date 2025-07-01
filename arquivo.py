import os
os.system("clear")
import math
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

def lerFloat(mensagem): 
    while True:
        entrada = input(mensagem)
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.")

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
        print("\n--- Livarte | Cálculo de Áreas ---")
        print("\nMenu de Formas:")
        print("1 - Quadrado")
        print("2 - Retângulo")
        print("3 - Círculo")
        print("4 - Triângulo")
        print("5 - Trapézio")
        print("6 - Área composta")

        while True:
            try:
                forma = int(input("\nDigite a opção da forma: "))
            except ValueError:
                print("Opção inválida. Só é aceito números inteiros, tente novamente.")
                continue

            if forma == 1:
                lado = lerFloat("\nDigite o lado do quadrado (em metros): ")
                area = lado **2
                print(f"\nA área é de {area:.2f} m².")
                break

            elif forma == 2:
                largura = lerFloat("\nDigite a largura (em metros): ")
                comprimento = lerFloat("\nDigite o comprimento (em metros): ")
                area = largura * comprimento
                print(f"\nA área é de {area:.2f} m².")
                break
            
            elif forma == 3:
                raio = lerFloat("\nDigite o raio do círculo (em metros): ")
                area = math.pi * (raio**2)
                print(f"\nA área é de {area:.2f} m².")
                break

            elif forma == 4:
                base = lerFloat("\nDigite a base do triângulo (em metros): ")
                altura = lerFloat("\nDigite a altura do triângulo (em metros): ")
                area = (base * altura) / 2
                print(f"\nA área é de {area:.2f} m².")
                break

            elif forma == 5:
                baseMaior = lerFloat("\nDigite a base MAIOR (em metros): ")
                baseMenor = lerFloat("\nDigite a base MENOR (em metros): ")
                altura = lerFloat("\nDigite a altura (em metros): ")
                area = ((baseMaior + baseMenor) * altura) / 2
                print(f"\nA área é de {area:.2f} m².")
                break
            
            else:
                print("Opção inválida! Tente novamente.")

    elif opcao == 2:
        print("\n--- Livarte | Conversor de Escalas ---")
        print("\nMenu de Escalas:")
        print("1 - Converter de real para desenho")
        print("2 - Converter de desenho para real")

        while True:
            try:
                opcaoEscala = int(input("\nDigite a opção da forma: "))
            except ValueError:
                print("Opção inválida. Só é aceito números inteiros, tente novamente.")
                continue

            if opcaoEscala == 1:
                medidaReal = lerFloat("\nDigite a medida real (em metros): ")
                fator = lerFloat("\nDigite o fator da escala (ex: 1:50 → fator = 50): ")
                conversao = medidaReal / fator
                print(f"\nA medida no desenho será de {conversao:.2f} metros.")
                break

            elif opcaoEscala == 2:
                medidaDesenho = lerFloat("\nDigite a medida do desenho (em metros): ")
                fator = lerFloat("\nDigite o fator da escala (ex: 1:50 → fator = 50): ")
                conversao = medidaDesenho * fator
                print(f"\nA medida real será de {conversao:.2f} metros.")
                break

            else:
                print("Opção inválida. Digite '1' ou '2'.")

    elif opcao == 3:
        print("\n--- Livarte | Gerado de Orçamentos ---")
        print("\nMenu de Orçamentos:")
        print("1 - Adicionar orçamentos")
        print("2 - Visualizar orçamentos")

        while True:

            try:
                opcaoOrcamento = int(input("\nDigite a opção de orçamento: "))
            except ValueError:
                print("Erro: digite apenas número inteiros.")
                continue

            if opcaoOrcamento == 1:

                materiais = []
                custo_total_material = 0
                nome_projeto = input("\nDigite o nome do projeto: ").capitalize()
                servico = input("Digite o tipo de serviço: ").capitalize()

                while True:

                    nome_material = input("Digite o nome do material: ").capitalize()

                    try:
                        quantidade = float(input("Digite a quantidade de material necessário (em m², litros, unidades): "))
                        preco_unitario = float(input("Digite o preço unitário: R$ "))
                    except ValueError:
                        print("Erro: entrada inválida. Digite apenas números.")

                    custo_material = quantidade * preco_unitario
                    custo_total_material += custo_material
                    materiais.append((nome_material, quantidade, preco_unitario, custo_material))

                    continuar = input("\nDeseja adicionar mais materiais? (s/n): ").strip().lower()
                    if continuar != "s":
                        break

                try:
                    mao_de_obra = float(input("Digite o valor da mão de obra: R$ "))
                except ValueError:
                    print("Erro: digite apenas números.")

                custo_total = custo_total_material + mao_de_obra

                with open("orcamentos.txt", "a", encoding="utf-8") as file:
                    file.write(f"\n--- ORÇAMENTO: {nome_projeto.upper()} ---\n")
                    for i, (nome, qnt, preco, custo) in enumerate (materiais, start=1):
                        file.write(f"\n{i}. {nome}: {qnt} x R$ {preco:.2f} = {custo:.2f}\n")

                    file.write(f"Custo total dos materiais = {custo_total_material:.2f}\n")
                    file.write(f"Custo da mão de obra = {mao_de_obra}\n")
                    file.write(f"Custo total do orçamento = {custo_total:.2f}\n")
                
                print(f"\nOrçamento salvo com sucesso!")
                break

            elif opcaoOrcamento == 2:

                try:
                    with open("orcamentos.txt", "r") as file:
                        conteudo = file.read()
                        if conteudo.strip() == "":
                            print("O arquivo está vazio! Adicione um orçamento antes de visualizar.")
                        else:
                            print("\n--- ORÇAMENTOS SALVOS ---\n")
                            print(conteudo)
                except FileNotFoundError:
                    print("\nErro: nenhum arquivo encontrado.")

                break

            else:
                print(f"\nOpção inválida! Digite um número inteiro entre 1 e 2.")
                
    elif opcao == 4:

        while True:

            print("\n--- Livarte | Gráficos de Projeto ---")
            print("\nMenu de Gráficos:")
            print("0 - Voltar para o Menu Principal")
            print("1 - Distribuição de Áreas")
            print("2 - Orçamento por Categoria")
            print("3 - Cronograma do Projeto")

            while True:
                try:
                    opcaoGrafico = int(input("\nDigite a opção de gráfico: "))
                    break
                except ValueError:
                    print("Opção inválida. Tente novamente.")
                    continue

            if opcaoGrafico == 0:
                print("\nVoltando para o menu principal...")
                break

            elif opcaoGrafico == 1:

                print("\n--- Gráfico de Distribuição de Áreas ---")

                while True:

                    ambientes_str = input("\nDigite os nomes dos ambientes separados por vírgula (ex: Sala, Cozinha, Quarto): ")
                    valores_str = input("Digite as áreas correspondentes (em m²), na mesma ordem, separadas por vírgula (ex: 25, 15, 30): ")

                    labels = []
                    for amb in ambientes_str.split(","):
                        labels.append(amb.strip().capitalize())

                    valores = []
                    for valor in valores_str.split(","):
                        valores.append(float(valor.strip()))

                    if len(labels) != len(valores):
                        print("Erro: o número de ambientes e áreas não correspondem.")
                        continue

                    else:

                        plt.pie(valores, labels=labels, autopct='%1.1f%%', startangle=90)
                        plt.title("Distribuição de Áreas por Ambiente")
                        plt.axis('equal')
                        plt.show()
                        break

            elif opcaoGrafico == 2:

                print("\n--- Gráfico de Orçamento por Categoria ---")

                while True:

                    categorias_str = input("\nDigite as categorias separadas por vírgula (ex: Estrutura, Acabamento): ")
                    custos_str= input("Digite os custos correspondentes, na mesma ordem, separados por vírgulas (ex: 200, 450): ")

                    categorias = []
                    for categ in categorias_str.split(","):
                        categorias.append(categ.strip().capitalize())

                    try:
                        custos = []
                        for c in custos_str.split(","):
                            custos.append(float(c.strip()))
                    except ValueError:
                        print("Erro: certifique-se de digitar apenas números nos custos.")
                        continue

                    if len(categorias) != len(custos):
                        print("Erro: o número de categorias e valores não correspondem.")
                        continue

                    cores = plt.cm.tab10(range(len(categorias)))

                    plt.bar(categorias, custos, color=cores)
                    plt.title("Orçamento por Categoria")
                    plt.xlabel("Categoria")
                    plt.ylabel("Custo (R$)")

                    for i, valor in enumerate(custos):
                        plt.text(i, valor + (valor * 0.01), f'R$ {valor:.2f}', ha='center', fontsize=9)

                    plt.tight_layout()
                    plt.show()
                    break
            
            elif opcaoGrafico == 3:

                print("\n--- Gráfico de Cronograma do Projeto ---")

                fases = []
                inicios = []
                duracoes = []

                while True:

                    fase = input("\nDigite a fase da obra: ").strip().capitalize()

                    try:
                        data_str = input("\nDigite a data início do projeto (DD-MM-AAAA): ")
                        inicio = datetime.datetime.strptime(data_str, "%d-%m-%Y").date()
                        duracao = int(input("Digite a data de duração (em dias): "))

                    except ValueError:
                        print("Dados inválidos. Tente novamente.")
                        continue

                    fases.append(fase)
                    inicios.append(inicio)
                    duracoes.append(duracao)

                    continuar = input("Deseja adicionar outra tarefa? (s/n): ").strip().lower()
                    if continuar != "s":
                        break
                
                fig, ax = plt.subplots(figsize=(10, 5))
                cores = plt.cm.tab10(range(len(fases)))

                for i in range(len(fases)):
                    ax.barh(fases[i], duracoes[i], left=inicios[i], color=cores[i])

                formato_data = mdates.DateFormatter('%d-%m-%Y')
                ax.xaxis.set_major_formatter(formato_data)

                plt.xticks(rotation=45)
                ax.set_xlabel("Data")
                ax.set_title("Cronograma da Obra")
                ax.grid(True)

                plt.tight_layout()
                plt.show()
                break

            else:
                print("Opção inválida! Digite um número inteiro entre 1 e 3.")
                continue

    elif opcao == 5:
        print("\nEncerrando...")
        break

    else:
        print("\nOpção inválida. Digite um número inteiro entre 1 e 5.")
        continue