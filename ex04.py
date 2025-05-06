# autor: Michel
# data: 06/05/2025

# Define a matriz 3x3 (Exemplo) - Substitua pelos valores desejados
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# a. Soma da linha 2
soma_linha2 = sum(matriz[1])  # Índice 1 corresponde à segunda linha (0-indexed)
print("Soma da linha 2:", soma_linha2)

# b. Soma da coluna 3
soma_coluna3 = 0
for linha in matriz:
    soma_coluna3 += linha[2] # Índice 2 corresponde à terceira coluna (0-indexed)
print("Soma da coluna 3:", soma_coluna3)


# c. Soma da diagonal principal
soma_diagonal_principal = 0
for i in range(3):  # Loop de 0 a 2
    soma_diagonal_principal += matriz[i][i]
print("Soma da diagonal principal:", soma_diagonal_principal)

# d. Soma da diagonal secundária
soma_diagonal_secundaria = 0
for i in range(3):
    soma_diagonal_secundaria += matriz[i][2 - i]
print("Soma da diagonal secundária:", soma_diagonal_secundaria)