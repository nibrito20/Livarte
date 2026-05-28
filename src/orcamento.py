class Orcamento:

    def __init__(self, nome_projeto, servico, materiais, mao_de_obra):
        self.nome_projeto = nome_projeto
        self.servico = servico
        self.materiais = materiais
        self.mao_de_obra = mao_de_obra

    def adicionar_material(self):
        nome_material = input("Digite o nome do material: ").capitalize()
        
        try:
            quantidade = float(input("Digite a quantidade: "))
            preco_unitario = float(input("Digite o preço unitário: R$ "))
        except ValueError:
            print("Erro: entrada inválida.")
            return
        
        custo_material = quantidade * preco_unitario
        self.materiais.append((nome_material, quantidade, preco_unitario, custo_material))

    def calcular_total(self):
        custo_total_material = sum(custo for _, _, _, custo in self.materiais)
        return custo_total_material + self.mao_de_obra

    def salvar(self):
        with open("../include/orcamentos.txt", "a", encoding="utf-8") as file:
            file.write(f"\n--- ORÇAMENTO: {self.nome_projeto.upper()} ---\n")
            for i, (nome, qnt, preco, custo) in enumerate(self.materiais, start=1):
                file.write(f"\n{i}. {nome}: {qnt} x R$ {preco:.2f} = {custo:.2f}\n")
            file.write(f"Custo total = {self.calcular_total():.2f}\n")

    def visualizar(self):
        try:
            with open("orcamentos.txt", "r") as file:
                conteudo = file.read()
                if conteudo.strip() == "":
                    print("Arquivo vazio!")
                else:
                    print(conteudo)
        except FileNotFoundError:
            print("Nenhum arquivo encontrado.")



def gerenciar_orcamento():
    print("\n--- Livarte | Gerado de Orçamentos ---")
    print("\nMenu de Orçamentos:")
    print("1 - Adicionar orçamentos")
    print("2 - Visualizar orçamentos")

    while True:
        try:
            opcao = int(input("\nDigite a opção de orçamento: "))
        except ValueError:
            print("Erro: digite apenas números inteiros.")
            continue

        if opcao == 1:
            nome_projeto = input("\nDigite o nome do projeto: ").capitalize()
            servico = input("Digite o tipo de serviço: ").capitalize()
            mao_de_obra = float(input("Digite o valor da mão de obra: R$ "))

            orcamento = Orcamento(nome_projeto, servico, [], mao_de_obra)

            while True:
                orcamento.adicionar_material()
                continuar = input("\nDeseja adicionar mais materiais? (s/n): ").strip().lower()
                if continuar != "s":
                    break

            orcamento.salvar()
            print("\nOrçamento salvo com sucesso!")
            break

        elif opcao == 2:
            orcamento = Orcamento("", "", [], 0)
            orcamento.visualizar()
            break

        else:
            print("Opção inválida! Digite 1 ou 2.")