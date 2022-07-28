# Напишите программу, удаляющую из текста все слова, содержащие "абв".
st = []
with open('text_5_1.txt', 'r', encoding='utf-8') as f:
    st = f.read()
st = [word for word in st.split() if 'абв' not in word]
with open('text_5_2.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(st))