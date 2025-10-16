import time
import tracemalloc

# ----- Versión iterativa -----
def busqueda_binaria_iter(arr, x):
    print("\n--- Proceso iterativo ---")
    izq, der = 0, len(arr) - 1
    paso = 1
    while izq <= der:
        mid = (izq + der) // 2
        print(f"Iteración {paso}: rango=({izq}, {der}), medio={mid}, valor={arr[mid]}")
        if arr[mid] == x:
            print("→ Elemento encontrado en índice", mid)
            return mid
        elif arr[mid] < x:
            izq = mid + 1
        else:
            der = mid - 1
        paso += 1
    print("→ Elemento no encontrado")
    return -1

# ----- Versión recursiva -----
def busqueda_binaria_rec(arr, x, izq, der, nivel=0):
    print("  " * nivel + f"Llamada: rango=({izq}, {der})")
    if izq > der:
        print("  " * nivel + "→ No encontrado")
        return -1
    mid = (izq + der) // 2
    print("  " * nivel + f"Medio={mid}, valor={arr[mid]}")
    if arr[mid] == x:
        print("  " * nivel + "→ Encontrado en", mid)
        return mid
    elif arr[mid] > x:
        return busqueda_binaria_rec(arr, x, izq, mid - 1, nivel + 1)
    else:
        return busqueda_binaria_rec(arr, x, mid + 1, der, nivel + 1)

# ----- Programa principal -----
if __name__ == "__main__":
    n_str = int(input("Introduce el tamaño del arreglo (ej: 1000000): "))

    arr = list(range(n_str)) # Arreglo ordenado de 0 a n-1
    x = int(input("Número a buscar: "))

    tracemalloc.start()
    t0 = time.perf_counter()
    r_iter = busqueda_binaria_iter(arr, x)
    t1 = time.perf_counter()
    _, mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"\nResultado iterativo: {r_iter}")
    print(f"Tiempo: {t1-t0:.6f} s | Memoria: {mem/1024:.2f} KB \n\n")

    tracemalloc.start()
    t0 = time.perf_counter()
    r_rec = busqueda_binaria_rec(arr, x, 0, len(arr) - 1)
    t1 = time.perf_counter()
    _, mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"\nResultado recursivo: {r_rec}")
    print(f"Tiempo: {t1-t0:.6f} s | Memoria: {mem/1024:.2f} KB")
