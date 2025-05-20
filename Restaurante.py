class ItemMenu:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def calcular_total(self, cantidad=1):
        return self.precio * cantidad

class Bebida(ItemMenu):
    def __init__(self, nombre, precio, tamaño):
        super().__init__(nombre, precio)
        self.tamaño = tamaño

class Plato(ItemMenu):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo  

class Postre(ItemMenu):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo

class Pedido:
    def __init__(self):
        self.items = []
    
    def agregar_item(self, item, cantidad=1):
        self.items.append((item, cantidad))
    
    def calcular_total(self):
        subtotal = sum(item.calcular_total(cant) for item, cant in self.items)
        
        descuento = subtotal * 0.1 if subtotal > 50 else 0
        
        
        impuesto = subtotal * 0.19 #El IVA = 19% :D
        
        total = subtotal - descuento + impuesto
        
        return {
            'subtotal': subtotal,
            'descuento': descuento,
            'impuesto': impuesto,
            'total': total
        }
    
    def mostrar_factura(self):
        print("\nFactura: ")
        for i, (item, cant) in enumerate(self.items, 1):
            print(f"{i}. {item.nombre} x{cant} - ${item.precio * cant:.2f}")
        
        totales = self.calcular_total()
        print("\nResumen:")
        print(f"Subtotal: ${totales['subtotal']:.2f}")
        if totales['descuento'] > 0:
            print(f"Descuento: -${totales['descuento']:.2f}")
        print(f"Impuesto: ${totales['impuesto']:.2f}")
        print(f"Total a pagar: ${totales['total']:.2f}")
        

if __name__ == "__main__":
    
    refresco = Bebida("Refresco", 2.50, "mediano")
    cerveza = Bebida("Cerveza", 4.00, "grande")
    ensalada = Plato("Ensalada Felipe ;)", 6.50, "entrada")
    pizza = Plato("Pizza", 12.00, "principal")
    baby_beef = Plato("Baby beef", 20.00, "principal")
    banana_split = Postre("Banana split", 5.00, "postre")
    helado = Postre("Helado", 3.00, "postre")
    pollo_frito = Plato("Pollo frito", 8.00, "principal")
    hamburguesa = Plato("Hamburguesa", 10.00, "principal")
    brownie_chocolate = Postre("Brownie de chocolate", 4.00, "postre")


    
    pedido = Pedido()
    pedido.agregar_item(refresco, 2)
    pedido.agregar_item(cerveza)
    pedido.agregar_item(ensalada)
    pedido.agregar_item(pizza, 3)
    pedido.agregar_item(baby_beef, 2)
    pedido.agregar_item(banana_split)
    pedido.mostrar_factura()