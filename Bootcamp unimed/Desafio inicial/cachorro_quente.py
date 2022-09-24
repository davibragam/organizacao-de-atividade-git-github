valores = input().split(" ") 

hotdogts_consumidos = int(valores[0])
participantes = int(valores[1])

resultado = hotdogts_consumidos/participantes

if (1 <= hotdogts_consumidos, participantes <= 1000):
  print(f'{resultado:.2f}')