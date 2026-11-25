temperatura = []
dias =["segunda","terça","quarta","quinta","sexta","sábado","domingo"]
for dias in range(6):
  temp =float(input("digite a temperatura: "))
  temperatura.append(temp)
media=sum(temperatura)/6
maximo = max(temperatura)
minimo = min(temperatura)
print("media_atual : ",(media,2))

for dias in range(2):
  if temperatura[dias]>media:
   print("Maior temperatura:", maximo, "graus")
   print("Menor temperatura:", minimo, "graus")