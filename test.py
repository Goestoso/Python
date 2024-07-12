numero = -123.4567

# Formatando o número com diferentes especificações
print("1. Número com 2 dígitos após a vírgula: {:.2f}".format(numero))
print("2. Número com largura mínima do campo de 10, alinhado à direita: {:>10.2f}".format(numero))
print("3. Número com sinal de mais: {:+}".format(numero))
print("4. Número com sinal de menos mesmo para números positivos: {:-}".format(numero))
print("5. Número com zero à esquerda e largura mínima do campo de 10: {:=10.2f}".format(numero))
print("6. Número formatado em notação exponencial: {:.2e}".format(numero))
