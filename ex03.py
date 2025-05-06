# autor: Michel
# data: 06/05/2025

# Inicializa as variáveis com valores que garantem a atualização na primeira iteração
maior = float('-inf') # Menor valor possível
menor = float('inf')  # Maior valor possível


# Loop infinito até que o usuário digite 0
while True:
    valor = int(input("Digite um valor inteiro (0 para parar): "))
    if valor == 0:
        break

    # Atualiza o maior e o menor valor
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    print("Entrada inválida. Digite um número inteiro.")


#Saida
# Imprime o maior e o menor valor, se algum foi informado
if maior != float('-inf') and menor != float('inf'):
    print("Maior valor:", maior)
    print("Menor valor:", menor)
else:
    print("Nenhum valor foi informado.")