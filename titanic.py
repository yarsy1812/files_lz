import pandas as pd
import matplotlib.pyplot as plt
#Открываем исходный файл 
data = pd.read_parquet("titanic.parquet")
#Сохраняем данные в формат csv в эту же папку
data.to_csv("titanic.csv", index=False)
#Открываем сохраненный файл csv для проверки и подсчета статистики
df = pd.read_csv("titanic.csv")
#Списки для хранения процентов выживших и не выживших по классам
survived_list = []
died_list = []
#Перебираем три класса билетов 
for pclass in range(1,4):
    #Выбираем пассажиров только этого класса
    class_data = df[df["Pclass"] == pclass]
    #Считаем сколько всего людей в этом классе
    total = len(class_data)
    #Считаем сколько выжило (1) и сколько не выжило (0)
    survived = len(class_data[class_data["Survived"] == 1])
    died = len(class_data[class_data["Survived"] == 0])
    #Считаем проценты и округляем до 1 знака после запятой
    survived_percent = round((survived / total) * 100, 1)
    died_percent = round((died / total) * 100, 1)
    #Добавляем результаты в списки
    survived_list.append(survived_percent)
    died_list.append(died_percent)
#Названия столбцов для оси X
classes = ["первый класс", "второй класс", "третий класс"]
#Создаем окно для графика
plt.figure(figsize=(8, 5))
# Строим нижние столбцы (выжившие)
plt.bar(classes, survived_list, width=0.4, color="blue", label="Выжил")
#Строим верхние невыживших поверх нижних
plt.bar(classes, died_list, width=0.4, bottom=survived_list, color="orange", label="Не выжило")
#Добавляем заголовок подписи и легенду
plt.title("Выживаемость пассажиров Титаника")
plt.ylabel("Процент пассажиров (%)")
plt.ylim(0, 100)
plt.legend()
#Выводим гистограмму на экран
plt.show()
