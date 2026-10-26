# R2 - Cola: turnos en orden de llegada
# FIFO: el primer cliente en llegar es el primero en ser atendido.
class Nodo:
    def __init__(self, dni, nombre):
        self.dni = dni            # texto, para no perder los ceros iniciales
        self.nombre = nombre
        self.siguiente = None     # referencia al siguiente cliente de la fila

class ColaEnlazada:
    def __init__(self):
        self.head = None          # frente: de aquí se desencola
        self.tail = None          # final: aquí se encola
    def esta_vacia(self):         # esta_vacia: O(1)
        return self.head is None
    def enqueue(self, dni, nombre):        # enqueue: O(1), gracias a tail
        nuevo = Nodo(dni, nombre)
        if self.tail:                      # cola con elementos: enlazar tras el final
            self.tail.siguiente = nuevo
        else:                              # cola vacía: el nuevo es frente y final
            self.head = nuevo
        self.tail = nuevo
    def dequeue(self):            # dequeue: O(1), gracias a head
        if self.esta_vacia():
            raise IndexError("La cola está vacía (Queue Underflow)")
        nodo = self.head
        self.head = nodo.siguiente         # el frente avanza al siguiente nodo
        if self.head is None:              # la cola quedó vacía: limpiar tail
            self.tail = None
        return nodo.dni, nodo.nombre
    def insertar_al_frente(self, dni, nombre):  # insertar_al_frente: O(1), deshace un "atender"
        nuevo = Nodo(dni, nombre)
        nuevo.siguiente = self.head
        self.head = nuevo
        if self.tail is None:              # estaba vacía: también es el final
            self.tail = nuevo
    def eliminar_ultimo(self):    # eliminar_ultimo: O(n), deshace un "registrar"
        if self.esta_vacia():
            raise IndexError("La cola está vacía (Queue Underflow)")
        ultimo = self.tail
        if self.head is self.tail:         # un solo nodo: la cola queda vacía
            self.head = self.tail = None
        else:
            actual = self.head             # sin referencia previa: recorrer hasta el penúltimo
            while actual.siguiente is not self.tail:
                actual = actual.siguiente
            actual.siguiente = None
            self.tail = actual
        return ultimo.dni, ultimo.nombre
    def mostrar(self):            # mostrar: O(n), recorre desde head
        if self.esta_vacia():
            print("Cola vacía")
            return
        elementos = []
        actual = self.head
        while actual:
            elementos.append(f"[{actual.dni} - {actual.nombre}]")
            actual = actual.siguiente
        print("Frente -> " + " -> ".join(elementos) + " -> Final")

def probar():                     # caso de prueba de la cola
    print("Prueba de la cola")
    cola = ColaEnlazada()
    cola.enqueue("1100000001", "Ana")
    cola.enqueue("1100000002", "Luis")
    cola.enqueue("1100000003", "Marta")
    cola.mostrar()
    assert cola.dequeue() == ("1100000001", "Ana")      # FIFO: sale el primero
    cola.insertar_al_frente("1100000001", "Ana")        # vuelve al frente
    assert cola.eliminar_ultimo() == ("1100000003", "Marta")
    assert cola.dequeue() == ("1100000001", "Ana")
    assert cola.dequeue() == ("1100000002", "Luis")
    assert cola.esta_vacia()
    try:
        cola.dequeue()            # dequeue en cola vacía debe dar underflow
    except IndexError as error:
        print("Underflow controlado:", error)
    print("Cola OK")

if __name__ == "__main__":
    probar()
