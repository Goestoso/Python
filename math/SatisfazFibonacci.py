def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def verificar_equacao(n):
    if n <= 1:
        return True

    # Calcula F(n + 5)
    fn_10 = fibonacci(n + 10)

    # Calcula F(n + 2)
    fn_7 = fibonacci(n + 7)

    # Calcula F(n)
    fn_6 = fibonacci(n + 6)

    # Verifica se a equação é satisfeita
    if fn_10 == 3 * fn_7 + 2 * fn_6:
        return True
    else:
        return False

# Teste para n = 10
n = 1
resultado = verificar_equacao(n)
print(f"A equação é satisfeita para n = {n}? {resultado}")
