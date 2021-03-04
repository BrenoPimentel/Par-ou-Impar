import random
from time import sleep


def jotnex():
    t1 = t2 = t3 = 0
    over = '//////////GAME OVER//////////'
    while True:
        pc = random.randint(1, 10)
        player = int(input('Digite um valor: '))
        esc = ' '
        while esc != 'par' and esc != 'impar' and esc != 'ímpar':
            esc = str(input('Par ou ímpar?: ')).lower().strip()
        soma = pc + player
        if esc in 'par':
            if soma % 2 == 1:
                for c in over:
                    new = c
                    if c == '/':
                        print(f'{new}', end='')
                        sleep(0)
                    elif c == ' ':
                        print(new, end='')
                        sleep(0)
                    else:
                        print(f'{new}', end='')
                        sleep(0.22)
                sleep(0.3)
                print(f'\nO computador escolheu {pc} e você {player}, a soma({soma}) é um número ímpar.')
                t3 += 1
                break
            if soma % 2 == 0:
                sleep(0.2)
                print('PROCESSANDO...')
                sleep(0.5)
                print('-' * 80)
                print(f'Você ganhou!!! O computador escolheu {pc} e você {player}, a soma({soma}) é um número par.')
                print('-' * 80)
                t1 += 1
        elif esc == 'impar' or esc == 'ímpar':
            if soma % 2 == 1:
                sleep(0.2)
                print('PROCESSANDO...')
                sleep(0.5)
                print('-' * 80)
                print(f'Você ganhou!!! O computador escolheu {pc} e você {player}, a soma({soma}) é um número ímpar.')
                print('-' * 80)
                t2 += 1
            elif soma % 2 == 0:
                for c in over:
                    new = c
                    if c == '/':
                        print(f'{new}', end='')
                        sleep(0)
                    elif c == ' ':
                        print(new, end='')
                        sleep(0)
                    else:
                        print(f'{new}', end='')
                        sleep(0.22)
                sleep(0.3)
                print(f'\nO computador escolheu {pc} e você {player}, a soma({soma}) é um número par.')
                t3 += 1
                break
    total = t1 + t2 + t3 - 1
    print('=-=' * 25)
    if total == 0:
        print('Voce perdeu de PRIMEIRA kkkkkkk')
    elif total == 1:
        print('Você ganhou apenas 1 vez :(')
    elif 1 < total <= 3:
        print(f'Parabéns, você conseguiu me ganhar {total} vezes seguidas. ')
    elif 3 < total <= 6:
        print(f'VOCE ESTÁ COM MUITA SORTE, conseguiu me ganhar {total} vezes, o que está acontecendo...')
    elif total > 6:
        print(f'OK!! Não sei mais o que está acontecendo, parabéns. Eu desisto. Você me ganhou {total} vezes seguidas.')
    keep = ' '
    while keep != 'sim' and keep != 's' and keep != 'n' and keep != 'não' and keep != 'nao':
        keep = str(input('Deseja continuar? [S/N]: ')).lower().strip()
        if keep == 'sim' or keep == 's':
            jotnex()
        else:
            break


if __name__ == '__main__':
    jotnex()
