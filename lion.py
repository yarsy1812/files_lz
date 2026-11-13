import docx
import csv
import matplotlib.pyplot as plt
doc=docx.Document("lion.docx")
text=""
for p in doc.paragraphs:
    text=text+p.text+ " "
text=text.lower()
letters={}
total_letters=0
for symbol in text:
    if symbol in letters:
        count=letters[symbol] 
        letters[symbol]=count+1
    else:
        letters[symbol] = 1

words_list=text.split()
total_words=0
words={}
for word in words_list:
    total_words=total_words+1
    if word in words:
        count = words[word]
        words[word] = count + 1
    else: words[word]=1

with open("words_stat.csv","w",encoding="utf-8=sig", newline="") as file:
    writer=csv.writer(file,delimiter=";")
    writer.writerow(["слово", "частота встречи,раз", "частота встречи,%"])
    for word in words:
        count=words[word]
        percent=round((count/total_words)*100, 2)
        writer.writerow([word,count,percent])

lettersort=sorted(letters.keys())
x_letters=[]
y_counts=[]
for letter in lettersort:
    x_letters.append(letter)
    y_counts.append(letters[letter])

plt.figure(figsize=(10,5))
plt.bar(x_letters,y_counts, color="blue", edgecolor="black")
plt.show()