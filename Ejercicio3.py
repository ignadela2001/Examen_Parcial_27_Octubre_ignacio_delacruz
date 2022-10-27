#Ejercicio 3
class Producto():
    def _init_(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print(f"Se acaba de crear un producto: {self.nombre},cuyo codigo es: {self.codigo}, con un precio de {self.precio}, de el tipo concreto: {self.tipo}")   

    def _str_(self):
        return "Codigo: {}, Nombre: {}, Precio: {}, Tipo: {} ".format( self.codigo, self.nombre, self.precio, self.tipo )
    print("La clase Producto se ha creado con exito")

Producto1 = (1314, "Alcaparra", 1, "Alimento")
Producto2 = (6969, "Balda", 10, "Mobiliario")
Producto3 = (3478, "Balon", 15, "Objeto deportivo")
Producto1.remove("1")
Producto1.insert(2,"2")

