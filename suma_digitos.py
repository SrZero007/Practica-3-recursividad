import time
import tracemalloc

# ----- Versión iterativa -----
def suma_digitos_iter(n):
    print("\n--- Proceso iterativo ---")
    suma = 0
    paso = 1
    while n > 0:
        digito = n % 10
        suma += digito
        print(f"Iteración {paso}: dígito={digito}, suma parcial={suma}")
        n //= 10
        paso += 1
    return suma

# ----- Versión recursiva -----
def suma_digitos_rec(n, nivel=0):
    print("  " * nivel + f"Llamada: suma_digitos_rec({n})")
    if n == 0:
        return 0
    parcial = suma_digitos_rec(n // 10, nivel + 1)
    total = n % 10 + parcial
    print("  " * nivel + f"Retorna {total} (por {n % 10} + {parcial})")
    return total

# ----- Programa principal -----
if __name__ == "__main__":
    n = int(input("Introduce un número entero: "))

    # --- Iterativa ---
    tracemalloc.start()
    t0 = time.perf_counter()
    r_iter = suma_digitos_iter(n)
    t1 = time.perf_counter()
    _, mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("\nResultado iterativo:", r_iter)
    print(f"Tiempo: {t1-t0:.6f} s | Memoria: {mem/1024:.2f} KB\n\n")

    # --- Recursiva ---
    tracemalloc.start()
    t0 = time.perf_counter()
    r_rec = suma_digitos_rec(n)
    t1 = time.perf_counter()
    _, mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("\nResultado recursivo:", r_rec)
    print(f"Tiempo: {t1-t0:.6f} s | Memoria: {mem/1024:.2f} KB")
