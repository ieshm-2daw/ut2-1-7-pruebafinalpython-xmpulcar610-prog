"""
Examen: Gestión de Inventario con Persistencia JSON y Programación Orientada a Objetos
Autor/a: _______________________________________
Fecha: __________________________________________

Objetivo:
Desarrollar una aplicación orientada a objetos que gestione un inventario de productos
con persistencia de datos en ficheros JSON y uso de listas y diccionarios anidados.

Clases requeridas:
- Proveedor
- Producto
- Inventario

"""

import json
import os


# ======================================================
# Clase Proveedor
# ======================================================

class Proveedor:
    def __init__(self, codigo, nombre, contacto):
        self.codigo = codigo
        self.nombre = nombre
        self.contacto = contacto

    def __str__(self):
        # TODO: devolver una cadena legible con el nombre y el contacto del proveedor
        {f"El nombre del proveedor es {self.nombre}, cuyo código es {self.codigo} y su contacto es {self.contacto}"}


# ======================================================
# Clase Producto
# ======================================================

class Producto:
    def __init__(self, codigo, nombre, precio, stock, proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = float(precio)
        self.stock = stock
        self.proveedor = proveedor

    def __str__(self):
        # TODO: devolver una representación legible del producto
        # Ejemplo: "[P001] Teclado - 45.99 € (10 uds.) | Proveedor: TechZone (ventas@techzone.com)"
        {f"[{self.codigo}] {self.nombr} - {self.precio} € ({self.stock} uds.) | Proveedor: {self.proveedor.nombre} ({self.proveedor.contacto})"}


# ======================================================
# Clase Inventario
# ======================================================

class Inventario:
    def __init__(self, nombre_fichero):
        self.nombre_fichero = nombre_fichero

    def cargar(self, archivo = "inventario.json"):
        """
        Carga los datos del fichero JSON si existe y crea los objetos Producto y Proveedor.
        Si el fichero no existe, crea un inventario vacío.
        """
        # TODO: implementar la lectura del fichero JSON y la creación de objetos
        try:
            with open(archivo, 'r') as f:
                cargar_inventario = json.load(f)
                self.prodcutos = []
                for p in cargar_inventario:
                    inventario = Producto(p["codigo"], p["nombre"], p["precio"], p["stock"])
                    inventario.completada = p["completada"]
                    self.producutos.append(inventario)
        except FileNotFoundError:
            print("No se encontró el archivo de tareas. Comenzando con una lista vacía.")

    def guardar(self, archivo="inventario.json"):
        """
        Guarda el inventario actual en el fichero JSON.
        Convierte los objetos Producto y Proveedor en diccionarios.
        """
        # TODO: recorrer self.productos y guardar los datos en formato JSON
        with open(archivo, 'w') as f:
            json.dump([p.__dict__ for p in self.prodcutos], f, default=str)

    def anadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario si el código no está repetido.
        """
        # TODO: comprobar si el código ya existe y, si no, añadirlo
        self.inventario = []
        self.inventario.append(producto)
        
        
    def mostrar(self):
        """
        Muestra todos los productos del inventario.
        """
        # TODO: mostrar todos los productos almacenados
        return {"f[{self.codigo}] {self.nombr} - {self.precio} € ({self.stock} uds.)"}

    def buscar(self, codigo):
        """
        Devuelve el producto con el código indicado, o None si no existe.
        """
        # TODO: buscar un producto por código
        for c in self.inventario:
            if c.codigo == int(codigo):
                return c

    def modificar(self, codigo, nombre=None, precio=None, stock=None, **kwargs):
        """
        Permite modificar los datos de un producto existente.
        """
        # TODO: buscar el producto y actualizar sus atributos
        for c in self.inventario:
            if c.codigo == codigo:
                codigo.actualizar(**kwargs)

    def eliminar(self, codigo):
        """
        Elimina un producto del inventario según su código.
        """
        # TODO: eliminar el producto de la lista
        c = self.inventario(codigo)
        if not c:
            print("No existe ese código de producto.")
            return
        else:
            self.inventario.remove(c)
            print("Producto eliminado.")

    def valor_total(self):
        """
        Calcula y devuelve el valor total del inventario (precio * stock).
        """
        # TODO: devolver la suma total del valor del stock
        pass

    def mostrar_por_proveedor(self, nombre_proveedor):
        """
        Muestra todos los productos de un proveedor determinado.
        Si no existen productos de ese proveedor, mostrar un mensaje.
        """
        # TODO: filtrar y mostrar los productos de un proveedor concreto
        pass


# ======================================================
# Función principal (menú de la aplicación)
# ======================================================

def main():
    # TODO: crear el objeto Inventario y llamar a los métodos según la opción elegida
    while True:
        print("\n=== GESTIÓN DE INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Calcular valor total")
        print("7. Mostrar productos de un proveedor")
        print("8. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        # TODO: implementar las acciones correspondientes a cada opción del menú

        if opcion == '1':
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            precio = input("Precio: ")
            stock = input("Stock: ")
            proveedor = input("Introduce los datos del proveedor:")
            try:
                nuevo_producto = Producto(codigo, nombre, precio, stock, proveedor)
                nuevo_producto.anadir_producto()
                print("Producto añadido")
            except ValueError:
                print("Vuelva a intentarlo.")
        
        elif opcion == '2':
            pass

        elif opcion == '3':
            pass

        elif opcion == '4':
            pass

        elif opcion == '5':
            codigo = input("Número de código del producto a eliminar: ").strip()
            codigo.eliminar(codigo)

        elif opcion == '6':
            pass

        elif opcion == '7':
            pass

        elif opcion == '8':
            print("Tareas guardadas exitosamente.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")
            
if __name__ == "__main__":
    main()
