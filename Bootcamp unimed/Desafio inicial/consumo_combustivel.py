valores = input().split(" ")

t = int(valores[0])
v = int(valores[1])

#12 km por litro
d = (v*t)
litros = (d/12)

print(f'{litros:.3f}')