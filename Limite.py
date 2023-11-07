import sympy as sp

# Defina a variável simbólica e a função
x = sp.symbols('x')
f = (x**4 - 4*x + 3) / (x**3 - 3*x + 2)

# Calcule o limite da função com o passo a passo
limite = sp.limit(f, x, 1, dir='-')

print("Limite:")
sp.pprint(limite, use_unicode=True)
