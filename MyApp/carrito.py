class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        
        self.cart = self.session.get("cart")
        if self.cart is not None:
            self.products = self.cart['products']
            return
                
        self.session["cart"] = {}
        self.session['cart']['total'] = 0
        self.session['cart']['products'] = {}
        
        self.cart = self.session['cart']
        self.products = self.cart['products']

    def agregar(self, product):
        id = str(product.id)
        if id not in self.products.keys():
            self.products[id] = {
                "id": product.id,
                "name": product.name,
                "description" : product.description,
                "precio" : product.price,
                "unidad" : product.unit,

                "cantidad": 1,
                "subtotal" : product.price,
            }
            
        else:
            self.products[id]["cantidad"] += 1
            self.products[id]['subtotal'] += self.products[id]['precio']
        
        self.cart['total'] += product.price    
        self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if not id in self.products.keys():
            return
        
        self.products[id]["cantidad"] -= 1
        self.products[id]['subtotal'] -= self.products[id]['precio']
        self.cart['total'] -= self.products[id]['precio']
        
        if self.cart[id]["cantidad"] <= 0: 
            del self.products[id]
            
        self.guardar_carrito()
        
    def eliminar(self, producto):
        id = str(producto.id)
        if not id in self.products.keys():
            return
        
        print('eliminando')
        self.cart['total'] -= self.products[id]['subtotal']
        del self.products[id]
        
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def limpiar(self):
        self.session["cart"]['products'] = {}
        self.session['cart']['total'] = 0
        
        self.session.modified = True