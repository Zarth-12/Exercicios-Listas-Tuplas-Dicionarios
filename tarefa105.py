print("Analise das temperaturas de julho")
print()

total_linhas = 0
soma_temperaturas = 0.0

min_temperatura = 100.0
max_temperatura = -100.0

data_hora_minima = ""

arquivo = open("banco-temperaturas-julho.txt", "r")

for linha in arquivo:

    partes = linha.strip().split("\t")
    data_hora = partes[0]
    temperatura = float(partes[1])
    
    total_linhas = total_linhas + 1 
    soma_temperaturas = soma_temperaturas + temperatura

    if temperatura > max_temperatura:
        max_temperatura = temperatura

    if temperatura < min_temperatura:
        min_temperatura = temperatura
        data_hora_minima = data_hora

arquivo.close()

media = soma_temperaturas / total_linhas

print("1. Total de linhas:", total_linhas)
print("2. Media das temperaturas:", round(media, 2), "C")
print("3. Temperatura minima:", min_temperatura, "C")
print("   Temperatura maxima:", max_temperatura, "C")
print("4. Primeiro registro da minima:", data_hora_minima)