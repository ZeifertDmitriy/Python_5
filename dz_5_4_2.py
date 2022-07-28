# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

st = []
with open('text_5_4_2.txt', 'r', encoding='utf-8') as f:
    st = f.read()
st2 = []
count = 1
for i in range(len(st)):
    if st[i].isdigit():
        count = int(st[i])
        print(count)
        continue
    for j in range(count):
        st2.append(st[i])
print(st)
print(st2)
with open('text_5_4_22.txt', 'w', encoding='utf-8') as f:
    f.write(''.join(st2))