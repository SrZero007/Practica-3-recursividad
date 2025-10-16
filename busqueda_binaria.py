import time

# ----- Búsqueda binaria iterativa -----
def binary_search_iter(arr, target):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# ----- Búsqueda binaria recursiva -----
def binary_search_rec(arr, target, lo, hi):
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_rec(arr, target, mid+1, hi)
    else:
        return binary_search_rec(arr, target, lo, mid-1)

if __name__ == "__main__":
    n_str = input("Introduce el tamaño del arreglo (ej: 1000000): ")
    target_str = input("Introduce el valor a buscar (ej: n-1): ")

    try:
        n = int(n_str)
        target = int(target_str)
    except ValueError:
        print("Error: Debes ingresar números válidos.")
        exit(1)

    arr = list(range(n)) # Arreglo ordenado de 0 a n-1

    # Iterativa
    t0 = time.perf_counter()
    idx_iter = binary_search_iter(arr, target)
    t1 = time.perf_counter()
    print("\n--- Búsqueda binaria iterativa ---")
    print("Índice encontrado:", idx_iter)
    print(f"Tiempo iterativo: {t1 - t0:.8f} s")

    # Recursiva
    t0 = time.perf_counter()
    idx_rec = binary_search_rec(arr, target, 0, len(arr)-1)
    t1 = time.perf_counter()
    print("\n--- Búsqueda binaria recursiva ---")
    print("Índice encontrado:", idx_rec)
    print(f"Tiempo recursivo: {t1 - t0:.8f} s")
