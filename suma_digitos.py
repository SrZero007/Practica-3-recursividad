import time

# ----- Función recursiva -----
def sum_numeros_rec(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
    return (n % 10) + sum_numeros_rec(n // 10)

# ----- Función iterativa -----
def sum_numeros_iter(n: int) -> int:
    n = abs(n)
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

if __name__ == "__main__":
    num_str = input("Introduce un número (puede ser muy grande): ")
    
    try:
        num = int(num_str)
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        exit(1)

    # Suma iterativa
    t0i = time.perf_counter()
    result_iter = sum_numeros_iter(num)
    t1i = time.perf_counter()
    print("Suma de dígitos (iterativo) =", result_iter)
    print(f"Tiempo iterativo: {t1i - t0i:.8f} s")

    # Suma recursiva
    t0r = time.perf_counter()
    result_rec = sum_numeros_rec(num)
    t1r = time.perf_counter()
    print("Suma de dígitos (recursivo) =", result_rec)
    print(f"Tiempo recursivo: {t1r - t0r:.8f} s\n")