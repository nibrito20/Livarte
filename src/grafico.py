import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

class Grafico:

    def __init__(self, tipo, labels, valores):
        self.tipo = tipo
        self.labels = labels
        self.valores = valores

    def gerar_pizza(self):
        plt.pie(self.valores, labels=self.labels, autopct='%1.1f%%', startangle=90)
        plt.title("Distribuição de Áreas por Ambiente")
        plt.axis('equal')
        plt.show()

    def gerar_barra(self):
        cores = plt.cm.tab10(range(len(self.labels)))
        plt.bar(self.labels, self.valores, color=cores)
        plt.title("Orçamento por Categoria")
        plt.xlabel("Categoria")
        plt.ylabel("Custo (R$)")
        for i, valor in enumerate(self.valores):
            plt.text(i, valor + (valor * 0.01), f'R$ {valor:.2f}', ha='center', fontsize=9)
        plt.tight_layout()
        plt.show()

    def gerar_cronograma(self, fases, inicios, duracoes):
        fig, ax = plt.subplots(figsize=(10, 5))
        cores = plt.cm.tab10(range(len(fases)))
        for i in range(len(fases)):
            ax.barh(fases[i], duracoes[i], left=inicios[i], color=cores[i])
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
        plt.xticks(rotation=45)
        ax.set_xlabel("Data")
        ax.set_title("Cronograma da Obra")
        ax.grid(True)
        plt.tight_layout()
        plt.show()


def gerar_grafico():

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

    if opcaoGrafico == 1:
        
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
                g = Grafico(1, labels, valores)
                g.gerar_pizza()
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

            g = Grafico(2, categorias, custos)
            g.gerar_barra()
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
        
        g = Grafico(3, None, None)
        g.gerar_cronograma(fases, inicios, duracoes)

    else:
        print("Opção inválida! Digite um número inteiro entre 1 e 3.")
