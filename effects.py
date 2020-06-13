from time import sleep

# Efeito de digitação de texto
y = None
def rob_print(y):
    for i in y:
        sleep(0.1)
        print(i, end='', flush=True)
    print('')

# Cores de texto
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
reset = "\033[m"

# Estilos de letra
normal = "\033[0m"
bold = "\033[1m"
italic = "\033[3m"
underline = "\033[4m"
invert = "\033[7m"
framed = "\033[51m"  # um quadrado ao redor das palavras