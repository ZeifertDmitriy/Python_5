# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Просто игра

from random import randint

kol_konf = 2021
tek_igrok = randint(1, 2)
hod = lambda k: kol_konf - k
perehod = lambda tek_igrok: tek_igrok + 1 if tek_igrok == 1 else tek_igrok - 1
while kol_konf > 0:
    print('Общее количество конфет: ' + str(kol_konf))
    print('Игрок № ' + str(tek_igrok) + ' введите количество конфет не превышающее 28:')
    kol_konf = hod(int(input()))
    if kol_konf > 0:
        tek_igrok = perehod(tek_igrok)

print('Игрок № ' + str(tek_igrok) + ' - выиграл')