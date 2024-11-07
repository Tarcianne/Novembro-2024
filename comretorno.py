# Função para realizar as operações
def calcular(x, y):
    soma = x + y
    subtracao = x - y
    multiplicacao = x * y
    if y != 0:  # Verifica se o denominador é diferente de zero para evitar divisão por zero
        divisao = x / y
    else:
        divisao = "Erro: Divisão por zero"

    # Retorna os resultados em forma de dicionário
    return soma, subtracao, multiplicacao, divisao

# Exemplo de uso
x = 10
y = 5

resultado = calcular(x, y)

print(f"Soma: {resultado[0]}")
print(f"Subtração: {resultado[1]}")
print(f"Multiplicação: {resultado[2]}")
print(f"Divisão: {resultado[3]}")