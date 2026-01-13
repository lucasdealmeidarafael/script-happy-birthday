import os
import time
from pyfiglet import Figlet

# Função para limpar a tela do terminal.
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Texto principal da mensagem.
def exibir_mensagem():
    limpar_tela()
    f=Figlet(font='larry3d')

    # Mensagem de aniversário.
    print("\033[1;36m" + "=" * 50)
    print("\033[1;33m 🎉 FELIZ ANIVERSÁRIO! 🎉")
    print("\033[1;36m" + "=" * 50 + "\033[0m")
    print()
    time.sleep(1)

    print("\033[1;37m" + f.renderText('L') + "\033[0m")  # Cor branca brilhante
    time.sleep(1)

    # Mensagem personalizada.
    print("\033[1;35m" + " Que seu dia seja tão incrível quanto você!")
    print("  🎂🍰🎁🥳🎈🎊🎉" + "\033[0m")
    print()
    time.sleep(1)
    print("\033[1;33m" + " Pressione Ctrl+C para sair..." + "\033[0m")

# Execução principal.
if __name__=="__main__":
    try:
        exibir_mensagem()
        # Manter o programa aberto.
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        limpar_tela()
        print("\033[1;36m Até logo!🎉\033[0m")