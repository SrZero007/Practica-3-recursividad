import time

# ----- Función iterativa -----
def revertir_iter(s: str) -> str:
    lst = []
    for ch in s:
        lst.insert(0, ch)
    return ''.join(lst)

# ----- Función recursiva -----
def revertir_rec(s: str) -> str:
    if s == "":
        return ""
    return s[-1] + revertir_rec(s[:-1])

if __name__ == "__main__":
    s = input("Introduce una cadena (larga para probar tiempos): ")

    # Iterativa
    t0 = time.perf_counter()
    r_iter = revertir_iter(s)
    t1 = time.perf_counter()
    print("\n--- Versión iterativa ---")
    print("Longitud original:", len(s))
    print("Caracteres del invertido:", r_iter[:1000])
    print(f"Tiempo iterativo: {t1 - t0:.6f} s")

    # Recursiva
    t0 = time.perf_counter()
    r_rec = revertir_rec(s)
    t1 = time.perf_counter()
    print("\n--- Versión recursiva ---")
    print("Longitud original:", len(s))
    print("Caracteres del invertido:", r_rec[:1000])
    print(f"Tiempo recursivo: {t1 - t0:.6f} s")
