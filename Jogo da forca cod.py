# Projeto 1, desenvolvimento de um jogo da forca em python

# import
import random
from os import system, name


# função para limpar a tela a cada execução
def limpa_tela():
    # windows
    if name == 'nt':  # nt = windows
        _ = system('cls')

    # Mac ou lixus
    else:
        _ = systeam("clear")


# FUNÇÂO
def JOGO():
    limpa_tela()
    print("\n Bem-vindo(a) ao jogo da forca!")
    print("advinhe a palavra para se livrar da forca:\n")
    print("O tema é: Países")

    # lista dos paises do JOGO
    pais = ['brasil', 'bahamas', 'afeganistao', 'alemanha', 'eslovenia', 'letonia', 'austria', 'espanha', 'lituania',
            'belgica', 'luxemburgo', 'bulgaria', 'finlandia', 'malta', 'chequia', 'frança', 'paises Baixos', 'chipre',
            'grecia', 'polonia', 'croacia', 'hungria', 'portugal', 'dinamarca', 'irlanda', 'romenia', 'eslovaquia',
            'italia', 'suecia']

    # escolher aleatóriamente um pais
    pais_ale = random.choice(pais)  # choice = escolher

    # list comprehension
    letra_acertada = ['_' for letra in pais_ale]  # "_" para cada letra escolhida aleatóriamente na lista

    num_chances = 10

    # lista para as letras erradas
    letra_errada = []

    # loop enquanto o número de chances for maior do que zero
    while num_chances > 0:  # while=enquanto

        print(" ".join(letra_acertada))  # junção com o que tem do lado direito e do lado esquerdo
        print("\nchances restantes:",
              num_chances)  # num_chance pode ser que fique preso ao numero total de letras que é igual as chances
        print("Letras erradas", " ".join(letra_errada))

        # numero de tentativas                   #lower() tudo que for escrito ficara em minúsculo
        tentativa = input("\n Digite uma letra: ".lower())  # iput(enquanto não digitar nada ele não avança) # lower
        if tentativa.isnumeric():
            print("Por favor, digite apenas letras. Tente novamente.")
            continue

        # condicional
        if tentativa in pais_ale:
            index = 0
            for letra in pais_ale:
                if tentativa == letra:
                    letra_acertada[index] = letra  # colocar letra descoberta naquele index
                index += 1  # se for verdadeiro vai acrescentar
        else:
            num_chances -= 1  # diminuir número de chances
            letra_errada.append(tentativa)  # colocar a letra errada na lista de tentativas usando append

        # condicional

        if "_" not in letra_acertada:
            print("\n Parabéns, você venceu!!!!!!!!!")
            print(pais_ale)
            break

    if "_" in letra_acertada:
        print("Poxa, você perdeu!, a palavra era:", pais_ale)


# bloco main o bloco que avisa que é um programa python
if __name__ == "__main__":
    JOGO()
    print("\nparabéns! esta evoluindo: \n")
