import time
import tracemalloc

# ----- Versión iterativa -----
def potencia_iter(base, exp):
    print("\n--- Proceso iterativo ---")
    resultado = 1
    for i in range(1, exp + 1):
        resultado *= base
        print(f"Iteración {i}: resultado={resultado}")
    return resultado

# ----- Versión recursiva -----
def potencia_rec(base, exp, nivel=0):
    print("  " * nivel + f"Llamada: potencia_rec({base}, {exp})")
    if exp == 0:
        print("  " * nivel + "→ Retorna 1")
        return 1
    if exp % 2 == 0:
        mitad = potencia_rec(base, exp // 2, nivel + 1)
        res = mitad * mitad
        print("  " * nivel + f"→ Retorna {res} (mitad*mitad)")
        return res
    else:
        res = base * potencia_rec(base, exp - 1, nivel + 1)
        print("  " * nivel + f"→ Retorna {res} (base*rec)")
        return res

# ----- Programa principal -----
if __name__ == "__main__":
    base = int(input("Base: "))
    exp = int(input("Exponente: "))

    tracemalloc.start()
    t0 = time.perf_counter()
    r_iter = potencia_iter(base, exp)
    t1 = time.perf_counter()
    _, mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"\nResultado iterativo: {r_iter}")
    print(f"Tiempo: {t1-t0:.6f} s | Memoria: {mem/1024:.2f} KB\n \n")

    tracemalloc.start()
    t0 = time.perf_counter()
    r_rec = potencia_rec(base, exp)
    t1 = time.perf_counter()
    _, mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"\nResultado recursivo: {r_rec}")
    print(f"Tiempo: {t1-t0:.6f} s | Memoria: {mem/1024:.2f} KB")
