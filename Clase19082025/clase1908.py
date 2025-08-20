import random
class Ventas: 
    matriz= []
    tamanoMatriz = 0
    ventas= {}

    def __init__(self, tamano):
        self.tamanoMatriz = tamano

    def crearMatriz(self):
        for i in range(self.tamanoMatriz):
            filas=[]
            for j in range(self.tamanoMatriz):
                print("           ")
                tipoComida= input("ingrese el tipo de comida: \n1. hamburguesa. \n2. perro. \n3. papas. \n")

                match tipoComida:
                    case "1":
                        comida = "Hamburguesa"
                    case "2":
                        comida = "Perro"
                    case "3":
                        comida = "Papas"
                    case _:
                        comida = "Invalido"
                        print("Opción invalida")

                if comida == "Invalido" :
                    print("Se selecciono una opción invalida")
                    break
                print("           ")
                cantidad = int(input("ingrese la cantidad de la comida: "))
                print("           ")
                tamano = input("ingrese el tamaño de la comida: \n1. grande. \n2. mediano. \n3. pequeño. \n")
                match tamano:
                    case "1":
                        tamanoComida = "Grande"
                    case "2":
                        tamanoComida = "Mediano"
                    case "3":
                        tamanoComida = "Pequeño"
                    case _:
                        tamanoComida = "Invalido"
                        print("Opción invalida")
                
                if tamanoComida == "Invalido" :
                    print("Se selecciono una opción invalida")
                    break
                print("           ")
                valor = int(input("ingrese el valor de la comida: "))
                venta = {
                    "tipoComida": comida,
                    "cantidad": cantidad,
                    "tamano": tamanoComida,
                    "valor": valor
                }
                filas.append(venta)
            self.matriz.append(filas)
        return self.matriz
    
    def mostrarMatriz(self):
        for x in self.matriz:
            print(x)
    
    def totalVenta(self):
        for i in self.matriz:
            for j in i:
                if j["tipoComida"] not in self.ventas:
                    self.ventas[j["tipoComida"]] = {"cantidad": 0, "total": 0}
                self.ventas[j["tipoComida"]]["cantidad"] += j["cantidad"]
                self.ventas[j["tipoComida"]]["total"] += (j["valor"] * j["cantidad"])
        return self.ventas
    
    def mostrarTotalVentas(self):
        for tipo, datos in self.ventas.items():
            print(f"se vedieron {datos["cantidad"]} de {tipo} para un total de {datos["total"]}")
    
tamano = int(input("ingrese el tamaño de la matriz: "))
comidas = Ventas(tamano)
comidas.crearMatriz()
print("***************************************")
comidas.mostrarMatriz()
print("***************************************")
comidas.totalVenta()
comidas.mostrarTotalVentas()
print("               ")
