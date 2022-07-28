# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Игра против бота (скайнет)

from random import randint

print('Игрок № 1 - человек, игрок № 2 - бот')
kol_konf = 2021
tek_igrok = randint(1, 2)
hod_kol = lambda k: kol_konf - k
perehod = lambda tek_igrok: tek_igrok + 1 if tek_igrok == 1 else tek_igrok - 1
vib_bot = lambda kol_vib: kol_konf if kol_konf <= 28 else kol_konf // 28 + 1
bot_or_not = lambda kol: int(input()) if tek_igrok == 1 else vib_bot(1)
while kol_konf > 0:
    print('Общее количество конфет: ' + str(kol_konf))
    print('Игрок № ' + str(tek_igrok) + ' введите количество конфет не превышающее 28:')
    kol_konf = hod_kol(bot_or_not(1))
    if kol_konf > 0:
        tek_igrok = perehod(tek_igrok)
print('Игрок № ' + str(tek_igrok) + ' - выиграл')