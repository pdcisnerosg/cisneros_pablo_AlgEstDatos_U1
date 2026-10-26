# R1 - Pila: historial de acciones
# LIFO: la última acción realizada es la primera que se debe deshacer (como Ctrl+Z).
class Nodo:
    def __init__(self, accion, dni, nombre):
        self.accion = accion      # "registrar" o "atender"
        self.dni = dni            # texto, para no perder los ceros iniciales
        self.nombre = nombre
        self.siguiente = None     # referencia al nodo de abajo

class PilaEnlazada:
    def __init__(self):
        self.cima = None          # la cima es la cabeza de la lista
    def esta_vacia(self):         # esta_vacia: O(1)
        return self.cima is None
    def push(self, accion, dni, nombre):   # push: O(1)
        nuevo = Nodo(accion, dni, nombre)  # crear el nodo
        nuevo.siguiente = self.cima        # apuntarlo a la antigua cima
        self.cima = nuevo                  # mover la cima
    def pop(self):                # pop: O(1)
        if self.esta_vacia():
            raise IndexError("La pila está vacía (Stack Underflow)")
        nodo = self.cima
        self.cima = nodo.siguiente         # desconectar el nodo de arriba
        return nodo.accion, nodo.dni, nodo.nombre
    def peek(self):               # peek: O(1), consulta la cima sin retirarla
        if self.esta_vacia():
            raise IndexError("La pila está vacía (Stack Underflow)")
        return self.cima.accion, self.cima.dni, self.cima.nombre
    def mostrar(self):            # mostrar: O(n), recorre desde la cima
        if self.esta_vacia():
            print("Historial vacío")
            return
        print("Cima:")
        actual = self.cima
        while actual is not None:
            print(f"  {actual.accion}: {actual.dni} - {actual.nombre}")
            actual = actual.siguiente

def probar():                     # caso de prueba de la pila
    print("Prueba de la pila")
    pila = PilaEnlazada()
    pila.push("registrar", "1100000001", "Ana")
    pila.push("atender", "1100000001", "Ana")
    pila.mostrar()
    print("Cima:", pila.peek())
    assert pila.pop() == ("atender", "1100000001", "Ana")     # LIFO: sale el último
    assert pila.pop() == ("registrar", "1100000001", "Ana")
    assert pila.esta_vacia()
    try:
        pila.pop()                # pop en pila vacía debe dar underflow
    except IndexError as error:
        print("Underflow controlado:", error)
    print("Pila OK")

if __name__ == "__main__":
    probar()
