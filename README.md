# Sistema de Gestión de Turnos - Taller CarUPS

Aplicación de consola en Python para administrar la fila de espera y atención de clientes en el taller mecánico CarUPS, utilizando estructuras de datos lineales implementadas desde sus nodos.

* **Autor:** Pablo Cisneros
* **Materia:** Algoritmos y Estructuras de Datos — Unidad 1
* **Carrera:** Ciencia de Datos

---

## Cómo ejecutar

Requiere Python 3.8 o superior sin dependencias externas:

```bash
python main.py
```

Pruebas individuales por módulo:
```bash
python pila.py
python cola.py
python lista.py
```

---

## Módulos del sistema

* `pila.py`: Historial de acciones del operador para permitir deshacer operaciones.
* `cola.py`: Cola con referencias `head` y `tail` para atención en orden de llegada.
* `lista.py`: Registro general de clientes con cédula/DNI y nombre.
* `main.py`: Menú principal por consola y casos de prueba.

---

## Justificación de estructuras

* **Pila (LIFO):** Ideal para deshacer acciones (similar a Ctrl+Z). La última acción ejecutada es la primera en revertirse sin necesidad de recorrer la memoria.
* **Cola (FIFO):** Modela la atención por orden de llegada. Al mantener punteros a `head` y `tail`, tanto la llegada como la atención operan en O(1).
* **Lista enlazada:** Permite el crecimiento dinámico de clientes registrados sin reservar bloques fijos de memoria previa.

---

## Tabla de complejidades

| Estructura | Operación | Complejidad | Justificación técnica |
| :--- | :--- | :--- | :--- |
| **Pila** | `push` | O(1) | Inserta al inicio actualizando referencias. |
| **Pila** | `pop` | O(1) | Retira la cima y mueve el puntero al siguiente. |
| **Pila** | `peek` | O(1) | Consulta la cima sin iterar. |
| **Pila** | `mostrar` | O(n) | Recorre los n nodos para imprimirlos. |
| **Cola** | `enqueue` | O(1) | Conecta el nuevo nodo directo al puntero `tail`. |
| **Cola** | `dequeue` | O(1) | Extrae desde el puntero `head`. |
| **Cola** | `insertar_al_frente` | O(1) | Reubica al frente reasignando `head`. |
| **Cola** | `eliminar_ultimo` | O(n) | Recorre hasta el penúltimo nodo para actualizar `tail`. |
| **Cola** | `mostrar` | O(n) | Recorre desde `head` hasta el final. |
| **Lista enlazada** | `agregar` | O(1) | Inserta en la cabeza reasignando punteros. |
| **Lista enlazada** | `buscar_por_nombre`| O(n) | Búsqueda lineal en toda la lista. |
| **Lista enlazada** | `buscar_por_dni` | O(n) | En el peor caso recorre hasta el final. |
| **Lista enlazada** | `mostrar` | O(n) | Recorrido secuencial desde la cabeza. |

---

## Casos de prueba

Cada módulo incluye validaciones con `assert`: comportamiento LIFO en pila, orden FIFO y control de cola vacía en cola, y búsquedas con y sin coincidencia en la lista.
