# my_str = '1 22 54 76 2'.split()
# # for i in range(len(my_list)):
# #     my_list[i] = int(my_list[i])

# my_list = [int(item) for item in my_str if (int(item) > 10)]
# print(my_list)

# lambda

# f = lambda x: x**2 if x > 10 else x**3
# my_list = [12, 54, 3, 65]
# res = list(map(f, my_list))
# print(res)

# f = lambda x: True if x > 10 else False
# my_list = [12, 54, 3, 65]
# res = list(filter(f, my_list))
# print(res)

# my_list_1 = ['12', '54', '3', '65']
# my_list_2 = [15, 76, 1, 98]
# my_list_3 = [65, 68, 8]

# res = list(zip(my_list_1, my_list_2, my_list_3))
# print(res)

# my_list_1 = ['A', 'B', 'C', 'D']
# res = list(enumerate(my_list_1))
# print(res)

# 1. Удалить из исходной строки все слова с "абв"
# 'Привет, Мир Мы очабв любим Пайтонабв! Семинары'

my_str = 'Привет, Мир Мы очабв любим Пайтонабв! Семинары'
#f = lambda s: False if 'абв' in s else True
#my_list = list(filter(f, my_str))

# my_list = list(filter(lambda item: 'абв' not in item, my_str.split()))
# print(my_list)

res = [word for word in my_str.split() if 'абв' not in word]
print(' '.join(res))