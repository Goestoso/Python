from sympy import symbols, expand

x, y = symbols('x y')

expression = (2*x**5 + y**2/2)**8

expanded_expression = expand(expression)

coefficient = expanded_expression.coeff(x**35 * y**2)

print("Coeficiente de x³⁵y²:", coefficient)
