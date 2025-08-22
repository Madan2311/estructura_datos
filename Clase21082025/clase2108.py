class Punto8:
    matriz = []
    tamanoMatriz = 0
    
    def __init__(self, tamano):
        self.tamanoMatriz = tamano
        
    def crearMatriz(self):
        for i in range(self.tamanoMatriz):
            filas=[]
            for j in range(self.tamanoMatriz):
                print("           ")
                producto= input("ingrese el nombre del producto: ")
                print("           ")
                precio = int(input("ingrese el precio del producto: "))
                print("           ")
                categoria = input("ingrese la categoria del producto: \n1. carnicos. \n2. lacteos. \n3. granos. \n")
                match categoria:
                    case "1":
                        categoriaProducto = "Grande"
                    case "2":
                        categoriaProducto = "Mediano"
                    case "3":
                        categoriaProducto = "Pequeño"
                    case _:
                        categoriaProducto = "Invalido"
                
                while categoriaProducto == "Invalido":
                    categoria = input("ingrese la categoria del producto: \n1. carnicos. \n2. lacteos. \n3. granos. \n")

                print("           ")
                inventario = {
                    "producto": producto,
                    "precio": precio,
                    "categoria": categoria
                }
                filas.append(inventario)
            self.matriz.append(filas)
        return self.matriz
    
    def mostrarMatriz(self):
        for x in range(len(self.matriz)):
            for z in self.matriz[x]:
                print(z)