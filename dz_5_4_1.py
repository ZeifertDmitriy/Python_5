# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

st = []
with open('text_5_4_1.txt', 'r', encoding='utf-8') as f:
    st = f.read()
st2 = []
count = 1
for i in range(len(st) - 1):
    if st[i + 1] == st[i]:
        count += 1
    else:
        st2.append(str(count) + st[i])
        count = 1
with open('text_5_4_12.txt', 'w', encoding='utf-8') as f:
    f.write(''.join(st2))