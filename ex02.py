# autor: Michel
# data: 06/05/2025

# Inicializa as variáveis
soma_impares = 0
qtd_impares = 0

# Loop infinito até que o usuário digite 0
while True:
    # Solicita um valor inteiro ao usuário
    valor = int(input("Digite um valor inteiro (0 para parar): "))
    
    # Sai do loop se o valor for 0
    if valor == 0:
        break
    
    # Verifica se o valor é ímpar
    if valor % 2 != 0:
        soma_impares += valor
        qtd_impares += 1
        
    print("Entrada inválida. Digite um número inteiro.")

# Calcula e imprime a média dos valores ímpares, se houver
if qtd_impares > 0:
    media = soma_impares / qtd_impares
    print("Média dos valores ímpares:", media)
else:
    print("Nenhum valor ímpar foi informado.")