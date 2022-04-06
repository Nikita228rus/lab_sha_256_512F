from conf import *
import time


def main():
    case = input('1 - ввод из консоли\n2 - чтение из файла\n>>>\t')
    if case == '1':
        massive = input('Введите текст:\t')

    elif case == '2':
        with open("input.txt", "r") as file:
            massive = file.read()

    massive = text_to_bin(massive)

    choose = input('Выбор свертки\n256 - 1\n512 - 2\n>>>\t')
    if choose == '1':
        final = sha_256(massive)
        with open("output.txt", "a", encoding='utf-8') as file:
            file.write('256: {}\ntime:\t{}\n\n'.format(final, time.asctime()))

    elif choose == '2':
        final = sha_512(massive)
        with open("output.txt", "a", encoding='utf-8') as file:
            file.write('512: {}\ntime:\t{}\n\n'.format(final, time.asctime()))

main()
