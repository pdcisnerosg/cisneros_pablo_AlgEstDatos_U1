# Gestor de turnos CarUPS
from pila import PilaEnlazada, probar as probar_pila
from cola import ColaEnlazada, probar as probar_cola
from lista import ListaEnlazada, probar as probar_lista

pila = PilaEnlazada()      # R1: historial de acciones (para deshacer)
cola = ColaEnlazada()      # R2: turnos en orden de llegada
lista = ListaEnlazada()    # R3: clientes registrados

def registrar_turno():
    dni = input("DNI: ").strip()
    if not dni.isdigit():
        print("DNI inválido: escriba solo números")
        return
    cliente = lista.buscar_por_dni(dni)    # ¿ya es cliente registrado?
    if cliente is None:
        nombre = input("Nombre: ").strip()
        if nombre == "":
            print("El nombre no puede estar vacío")
            return
        lista.agregar(dni, nombre)         # cliente nuevo: se agrega a la lista
    else:
        nombre = cliente.nombre            # cliente existente: se reutiliza su nombre
    cola.enqueue(dni, nombre)              # entra a la fila
    pila.push("registrar", dni, nombre)    # queda en el historial
    print(f"Turno registrado: {dni} - {nombre}")

def atender():
    if cola.esta_vacia():
        print("No hay turnos en espera")
        return
    dni, nombre = cola.dequeue()           # sale el primero en llegar (FIFO)
    pila.push("atender", dni, nombre)
    print(f"Atendiendo a: {dni} - {nombre}")

def deshacer():
    if pila.esta_vacia():
        print("No hay acciones para deshacer")
        return
    accion, dni, nombre = pila.pop()       # la última acción (LIFO)
    if accion == "registrar":
        cola.eliminar_ultimo()             # el turno recién registrado está al final
        print(f"Deshecho: registro del turno de {nombre} (sigue como cliente registrado)")
    else:
        cola.insertar_al_frente(dni, nombre)   # el cliente atendido vuelve al frente
        print(f"Deshecho: atención de {nombre}, vuelve al frente de la cola")

def buscar_cliente():
    nombre = input("Nombre a buscar: ").strip()
    encontrados = lista.buscar_por_nombre(nombre) if nombre else []
    if not encontrados:
        print("No se encontraron clientes")
    for cliente in encontrados:
        print(f"Encontrado: {cliente.dni} - {cliente.nombre}")

def ver_clientes():
    if lista.esta_vacia():
        print("No hay clientes registrados")
    else:
        lista.mostrar()

def ejecutar_pruebas():
    probar_pila()
    probar_cola()
    probar_lista()

def menu():
    print("\n=== Gestor de turnos CarUPS ===")
    print("1. Registrar turno")
    print("2. Atender siguiente turno")
    print("3. Deshacer última acción")
    print("4. Ver cola de turnos")
    print("5. Buscar cliente por nombre")
    print("6. Ver clientes registrados")
    print("7. Ver historial de acciones")
    print("8. Ejecutar casos de prueba")
    print("0. Salir")

def main():
    while True:
        menu()
        try:
            opcion = input("Opción: ").strip()
        except EOFError:                   # sin teclado (entrada terminada): salir sin error
            break
        if opcion == "1":
            registrar_turno()
        elif opcion == "2":
            atender()
        elif opcion == "3":
            deshacer()
        elif opcion == "4":
            cola.mostrar()
        elif opcion == "5":
            buscar_cliente()
        elif opcion == "6":
            ver_clientes()
        elif opcion == "7":
            pila.mostrar()
        elif opcion == "8":
            ejecutar_pruebas()
        elif opcion == "0":
            print("Hasta luego")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
