entrada = input().split(" ")

distancia = int(entrada[0])
diametro1 = int(entrada[-1])
diametro2 = int(entrada[1])

resultado = distancia/(diametro1+diametro2)

if (0 < distancia < 1000):
  if (0 < diametro1, diametro2 <100):
    print(f'{resultado:.2f}')