# Создайте программу для игры в ""Крестики-нолики"".
import os
from random import randint

os.system('cls')
my_dict = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
kon_ig = 0
tek_igrok = randint(1, 2)
hod = lambda h: 'X' if tek_igrok == 1 else 'O'
perehod = lambda tek_igrok: tek_igrok + 1 if tek_igrok == 1 else tek_igrok - 1
vic = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
       [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
while kon_ig == 0:
    os.system('cls')
    print(' ' + str(my_dict[1]) + ' | ' + str(my_dict[2]) + ' | ' + str(my_dict[3]) + ' \n---|---|---\n'
          ' ' + str(my_dict[4]) + ' | ' + str(my_dict[5]) + ' | ' + str(my_dict[6]) + ' \n---|---|---\n'
          ' ' + str(my_dict[7]) + ' | ' + str(my_dict[8]) + ' | ' + str(my_dict[9]) + ' ')
    print('Игрок № ' + str(tek_igrok) + ' выберите свободное поле:')
    my_dict[int(input())] = hod('1')
    kon_ig = int(lambda i: 1 if my_dict[vic[i[0]]] == my_dict[vic[i[1]]] == my_dict[vic[i[2]]] =='X' \
        else (2 if my_dict[vic[i[0]]] == my_dict[vic[i[1]]] == my_dict[vic[i[2]]] =='O' else 0))
# #____________________________________________________
#     if (my_dict[1] == 'X' and my_dict[2] == 'X' and my_dict[3] == 'X') or \
#         (my_dict[4] == 'X' and my_dict[5] == 'X' and my_dict[6] == 'X') or \
#         (my_dict[7] == 'X' and my_dict[8] == 'X' and my_dict[9] == 'X') or \
#         (my_dict[1] == 'X' and my_dict[4] == 'X' and my_dict[7] == 'X') or \
#         (my_dict[2] == 'X' and my_dict[5] == 'X' and my_dict[8] == 'X') or \
#         (my_dict[3] == 'X' and my_dict[6] == 'X' and my_dict[9] == 'X') or \
#         (my_dict[1] == 'X' and my_dict[5] == 'X' and my_dict[9] == 'X') or \
#         (my_dict[3] == 'X' and my_dict[5] == 'X' and my_dict[7] == 'X'):
#         kon_ig = 1
#         break
#     if (my_dict[1] == 'O' and my_dict[2] == 'O' and my_dict[3] == 'O') or \
#         (my_dict[4] == 'O' and my_dict[5] == 'O' and my_dict[6] == 'O') or \
#         (my_dict[7] == 'O' and my_dict[8] == 'O' and my_dict[9] == 'O') or \
#         (my_dict[1] == 'O' and my_dict[4] == 'O' and my_dict[7] == 'O') or \
#         (my_dict[2] == 'O' and my_dict[5] == 'O' and my_dict[8] == 'O') or \
#         (my_dict[3] == 'O' and my_dict[6] == 'O' and my_dict[9] == 'O') or \
#         (my_dict[1] == 'O' and my_dict[5] == 'O' and my_dict[9] == 'O') or \
#         (my_dict[3] == 'O' and my_dict[5] == 'O' and my_dict[7] == 'O'):
#         kon_ig = 2  
#         break  
# #_______________________________________________   
    tek_igrok = perehod(tek_igrok)
os.system('cls')
print(' '+ str(my_dict[1]) +' | ' + str(my_dict[2]) + ' | ' + str(my_dict[3]) + ' \n---|---|---\n' \
    ' '+ str(my_dict[4]) +' | ' + str(my_dict[5]) + ' | ' + str(my_dict[6]) + ' \n---|---|---\n' \
    ' '+ str(my_dict[7]) +' | ' + str(my_dict[8]) + ' | ' + str(my_dict[9]) + ' ')
print('Игрок № ' + str(kon_ig) + ' выиграл.')