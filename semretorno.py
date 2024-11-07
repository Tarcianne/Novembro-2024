def multiplicar(x, y):
    print(x * y)

def somar(x, y):
    print(x + y)

def dividir(x, y):
    if y != 0:
        print(x / y)
    else:
        print("Divisão por zero não permitida")

def subtrair(x, y):
    print(x - y)

# Valores de x e y
x = 10
y = 5

# Chamando as funções
print(multiplicar(x, y))
print(somar(x, y))
print(dividir(x, y))
print(subtrair(x, y))
