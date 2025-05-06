# autor: Michel
# data: 06/05/2025

# Loop infinito que só quebra quando o valor for válido
while True:
  # Solicita a nota ao usuário
        nota = float(input("Digite uma nota entre 0 e 10: "))
        # Verifica se a nota está dentro do intervalo válido
        if 0 <= nota <= 10:
            print("Nota válida:", nota)
            break  # Sai do loop se a nota for válida
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
  # Loop infinito que só quebra quando o valor for válido
        print("Entrada inválida. Digite um número.")