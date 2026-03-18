
cid1 = input("Informe a cidade de onde partiremos: ")
cid2 = input("Informe a cidade onde iremos: ")


distancia = int(input(f"Digite a distancia entre {cid1} e {cid2}:"))
tempV = int(input("Agora, digite o tempo estipulado entre os locais: "))

print(f'A velocidade media que o carro deve percorrer é igual a {distancia / tempV: .2f}')


