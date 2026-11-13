import docx
import csv
import matplotlib.pyplot as plt
#Открываем исходный документ 
doc=docx.Document("lion.docx")
text=""
#Обьединяем все абзацы в одну строку через пробел
for p in doc.paragraphs:
    text=text+p.text+ " "
 # Переводим весь текст в нижний регистр
text=text.lower()
#Создаем пустой словарь для подсчета символов и счетчик общего количества символов
letters={}
total_letters=0
#Перебираем каждый символ и считаеп сколько раз он встречается
russian = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
for symbol in text:
    # Проверяем что символ является русская буква
    if symbol in russian:
        if symbol in letters:
            letters[symbol] = letters[symbol] + 1
#Если символ встретился впервые добавляем его в словарь со значением 1
        else:
            letters[symbol] = 1
#убираем знаки пунктуации
punctuation = '.,!?;:"()[]{}«»—-–…'
clean_text = text
for p_symbol in punctuation:
    clean_text = clean_text.replace(p_symbol, " ")
    # Разбиваем текст на список слов по пробелам
#Разбиваем сплошной текст на список отдельных слов 
words_list = clean_text.split()
#Счетчик общего колва слов в тексте
total_words=0
#Словарь для хранения частоты каждого слова
words={}
for word in words_list:
# Увеличиваем общий счетчик слов
    total_words=total_words+1
 #Если слово уже встречалось прибавляем 1 к его счетчику
    if word in words:
        count = words[word]
        words[word] = count + 1
#Если слово новое записываем его в словарь с колвом 1
    else: words[word]=1
#Создаем файл для таблицы со статистикой слов
with open("words_stat.csv","w",encoding="utf-8-sig", newline="") as file:
    writer=csv.writer(file,delimiter=";")
    writer.writerow(["слово", "частота встречи,раз", "частота встречи,%"])
#Проходим по всем словам из словаря считаем процент и записываем строку в файл
    for word in words:
        count=words[word]
        percent=round((count/total_words)*100, 2)
        writer.writerow([word,count,percent])
#сортируем символы по алфовиту
lettersort=sorted(letters.keys())
# Список для оси X
x_letters=[]
# Список для оси Y
y_counts=[]
#Заполняем списки для осей гистограммы
for letter in lettersort:
    x_letters.append(letter)
    y_counts.append(letters[letter])
#создаем окно
plt.figure(figsize=(10,5))
#строим гистограмму
plt.bar(x_letters,y_counts, color="blue", edgecolor="black")
#выводим ее
plt.show()