import os
import time

# Função para limpar a tela do terminal.
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Texto principal da mensagem.
def exibir_mensagem():
    limpar_tela()

    # Mensagem de aniversário.
    print("\033[1;36m" + "=" * 50)
    print("\033[1;33m 🎉 FELIZ ANIVERSÁRIO! 🎉")
    print("\033[1;36m" + "=" * 50 + "\033[0m")
    print()
    time.sleep(1)

    