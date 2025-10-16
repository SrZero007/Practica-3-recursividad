import time
import sys
sys.setrecursionlimit(10000)

# ----- Potenciación iterativa -----
def potencia_iter(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

# ----- Potenciación recursiva -----
def potencia_rec(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = potencia_rec(base, exp // 2)
        return half * half
    else:
        return base * potencia_rec(base, exp - 1)

if __name__ == "__main__":
    try:
        base = int(input("Introduce la base: "))
        exp = int(input("Introduce el exponente: "))
    except ValueError:
        print("Error: Debes ingresar números enteros.")
        exit(1)

    # Iterativa
    t0 = time.perf_counter()
    r_iter = potencia_iter(base, exp)
    t1 = time.perf_counter()
    print("\n--- Potenciación iterativa ---")
    print("Resultado:", r_iter)
    print(f"Tiempo iterativo: {t1 - t0:.6f} s")

    # Recursiva
    t0 = time.perf_counter()
    r_rec = potencia_rec(base, exp)
    t1 = time.perf_counter()
    print("\n--- Potenciación recursiva ---")
    print("Resultado:", r_rec)
    print(f"Tiempo recursivo rápido: {t1 - t0:.6f} s")
