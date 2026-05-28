import math

class Forma:

    def __init__(self, forma, medidas):
        self.forma = forma
        self.medidas = medidas


    def calcular_area(self):

        if self.forma == 1:
            return self.medidas["lado"]**2
        
        elif self.forma == 2:
            return self.medidas["base"] * self.medidas["altura"]
        
        elif self.forma == 3:
            return math.pi * (self.medidas["raio"]**2)

        elif self.forma == 4:
            return self.medidas["base"] * self.medidas["altura"] / 2
        
        elif self.forma == 5:
            return ((self.medidas["base_maior"] + self.medidas["base_menor"]) * self.medidas["altura"]) / 2
        
        else:
            return -1
        

def menu_areas():

    print("\n--- Livarte | Cálculo de Áreas ---")
    print("\nMenu de Formas:")
    print("1 - Quadrado")
    print("2 - Retângulo")
    print("3 - Círculo")
    print("4 - Triângulo")
    print("5 - Trapézio")

    while True:
        try:
            forma = int(input("\nDigite a opção da forma: "))
            break
        except ValueError:
            print("Opção inválida. Só é aceito números inteiros, tente novamente.")
            continue

    return forma

def receber_valores(forma):

    dic = {}

    if forma == 1:
        lado = float(input("Digite o lado: "))
        dic["lado"] = lado
        
    
    elif forma == 2 or forma == 4:
        base = float(input("Digite a base: "))
        altura = float(input("Digite a altura: "))
        dic["base"] = base 
        dic["altura"] = altura

    elif forma == 3:
        raio = float(input("Digite o raio: "))
        dic["raio"] = raio

    elif forma == 5:
        base_maior = float(input("Digite a base maior: "))
        base_menor = float(input("Digite a base menor: "))
        altura = float(input("Digite a altura: "))
        dic["base_maior"] = base_maior
        dic["base_menor"] = base_menor
        dic["altura"] = altura

    return dic