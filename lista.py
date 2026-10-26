# R3 - Lista enlazada: clientes registrados
class Nodo:
    def __init__(self, dni, nombre):
        self.dni = dni            # texto, para no perder los ceros iniciales
        self.nombre = nombre
        self.siguiente = None     # referencia al siguiente cliente

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None        # primer nodo: único punto de acceso
    def esta_vacia(self):         # esta_vacia: O(1)
        return self.cabeza is None
    def agregar(self, dni, nombre):        # agregar: O(1), inserta al inicio
        nuevo = Nodo(dni, nombre)
        nuevo.siguiente = self.cabeza      # apuntarlo a la antigua cabeza
        self.cabeza = nuevo                # mover la cabeza
    def buscar_por_nombre(self, nombre):   # buscar_por_nombre: O(n), recorre toda la lista
        encontrados = []
        actual = self.cabeza               # variable auxiliar: nunca se pierde la cabeza
        while actual:
            if nombre.lower() in actual.nombre.lower():
                encontrados.append(actual)
            actual = actual.siguiente
        return encontrados
    def buscar_por_dni(self, dni):         # buscar_por_dni: O(n), peor caso recorre todo
        actual = self.cabeza
        while actual:
            if actual.dni == dni:
                return actual
            actual = actual.siguiente
        return None
    def mostrar(self):            # mostrar: O(n), recorre desde la cabeza
        actual = self.cabeza
        while actual:
            print(f"[{actual.dni} - {actual.nombre}]", end=" -> ")
            actual = actual.siguiente
        print("None")

def probar():                     # caso de prueba de la lista
    print("Prueba de la lista")
    lista = ListaEnlazada()
    lista.agregar("1100000001", "Ana Pérez")
    lista.agregar("1100000002", "Luis Mora")
    lista.agregar("1100000003", "Ana Gómez")
    lista.mostrar()
    assert len(lista.buscar_por_nombre("ana")) == 2     # dos coincidencias
    assert lista.buscar_por_nombre("zzz") == []         # sin coincidencias
    assert lista.buscar_por_dni("1100000002").nombre == "Luis Mora"
    assert lista.buscar_por_dni("999") is None
    print("Lista OK")

if __name__ == "__main__":
    probar()
