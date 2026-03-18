a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("A equação não possui números reais.")
else:
    x1 = (-b + (delta ** 0.5)) / (2*a)
    x2 = (-b - (delta ** 0.5)) / (2*a)

    print("Raiz x1:", x1)
    print("Raiz x2:", x2)