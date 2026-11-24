data_buscada = input("Digite a data desejada (aaaa-mm-dd): ")

min_temperatura = 100.0
max_temperatura = -100.0
encontrou_data = False

arquivo = open("banco-temperaturas-julho.txt", "r")

for linha in arquivo:
    partes = linha.strip().split("\t")
    data_hora = partes[0]
    temperatura = float(partes[1])
    
    if data_hora.startswith(data_buscada):
        encontrou_data = True
        
        if temperatura > max_temperatura:
            max_temperatura = temperatura

        if temperatura < min_temperatura:
            min_temperatura = temperatura

arquivo.close()

if encontrou_data == True:
    amplitude = max_temperatura - min_temperatura
    print("Data encontrada:", data_buscada)
    print("Temperatura minima:", min_temperatura, "C")
    print("Temperatura maxima:", max_temperatura, "C")
    print("Amplitude termica:", round(amplitude, 2), "C")
else:
    print("O dia", data_buscada, "nao esta presente no arquivo.")