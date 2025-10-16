import time
import tracemalloc

# ----- Versión iterativa -----
def invertir_iter(cadena):
    print("\n--- Proceso iterativo ---")
    invertida = ""
    paso = 1
    for c in cadena:
        invertida = c + invertida
        print(f"Iteración {paso}: agrega '{c}' → {invertida}")
        paso += 1
    return invertida

# ----- Versión recursiva -----
def invertir_rec(cadena, nivel=0):
    print("  " * nivel + f"Llamada: invertir_rec('{cadena}')")
    if len(cadena) <= 1:
        return cadena
    res = invertir_rec(cadena[1:], nivel + 1) + cadena[0]
    print("  " * nivel + f"Retorna '{res}'")
    return res

# ----- Programa principal -----
if __name__ == "__main__":
    cadena = input("Introduce una cadena: ")

    tracemalloc.start()
    t0 = time.perf_counter()
    r_iter = invertir_iter(cadena)
    t1 = time.perf_counter()
    _, mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print("\nResultado iterativo:", r_iter)
    print(f"Tiempo: {t1-t0:.6f} s | Memoria: {mem/1024:.2f} KB \n\n")

    tracemalloc.start()
    t0 = time.perf_counter()
    r_rec = invertir_rec(cadena)
    t1 = time.perf_counter()
    _, mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print("\nResultado recursivo:", r_rec)
    print(f"Tiempo: {t1-t0:.6f} s | Memoria: {mem/1024:.2f} KB")
