#!/usr/bin/python3

import os
from bs4 import BeautifulSoup
import requests
import itertools

#Возвращает html-код страницы по адресу url в виде объекта Beautiful soup
#Или не так. Нашел в интернете, главное, что работает
def get_page(url):
    req = requests.get(url)

    if req.status_code == 200:
        return BeautifulSoup(req.text, 'html.parser')
    return None

#Возвращает текст в виде строки из html-кода
#Тоже взял из интернета, но чуть-чуть передалал. Работает, и ладно
def text_from_url(url):
    bs = get_page(url)
    if bs is None:
        return bs
    text = ""
    title = bs.find("title")
    if title:
        text = text + title.text + '\n'
    
    lines = bs.find_all("p")
    body = '\n'.join([line.text.strip() for line in lines])
    text = text + body

    return text

#Принимает на вход строку, в которой слова разделены символами переноса строки
#Удаляет возможные пустые подстроки в этой строке
def remove_empty_strings(text):
    new_text = ''
    for i in range(len(text)-1):        #пробегаем по символам строки
        if text[i] != '\n':             #если не перенос строки, то переносим символ в новую строку
            new_text += text[i]
        if text[i] == '\n':             #если перенос строки
            if text[i+1] != '\n':       #а следующий символ не является переносом строки
                new_text += text[i]     #то его тоже добавляем
            else:
                pass                    #иначе - игнорируем

    return new_text

#Оставляет в строке толко символы русского алфавита и символ переноса строки
#Остальное удаляет
def remove_spec_signs(text):
    new_text = ''
    for i in range(len(text)):
        if text[i] >= 'а' and text[i] <= 'я' or text[i] == ' ' or text[i] == '\n':
            new_text += text[i]
    
    return new_text

#Принимает на вход строку, в которой слова разделены символами переноса строки
#Удаляет все слова длинной меньше пяти букв
def remove_short_words(text):
    word = ''
    new_text = ''
    letter_count = 0

    for i in range(len(text)):          #пробегаем по символам строки
        if text[i] != '\n':             #если не конец строки
            word += text[i]             #то выписываем символ в новое слово
            letter_count += 1           #увеличиваем счетчик букв в слове
        if text[i] == '\n':             #если перенос строки (граница слова)
            if letter_count >= 5:       #если у текущего слова больше 5 букв
                word += '\n'            #дописываем к нему перенос строки (дописываем границу)
                new_text += word        #и добавляем его к новой строке слов
            word = ''                   #обнуляем буфер слова и счетчик букв
            letter_count = 0
    
    return new_text


#Принимает на вход строку, в которой слова разделены символами переноса строки
#Создает два списка: в первом уникальные слова, во втором - колличество вхождений этих слов
def count_words(text):
    text += '\n'
    words = []
    word_dic = []
    word_count = []
    word = ''


    for i in range(len(text)):                                      #пробегаемся по слову до границы и заполняем буфер слова
        if text[i] != '\n':
            word += text[i]
        if text[i] == '\n':
            if word_dic.count(word) > 0:                            #ищем это слово в списке обработанных. если оно там есть (кол-во вхождений > 0)
                num = word_dic.index(word, 0, len(word_dic))      #находим его номер в этом списке
                word_count[num] += 1                                #и в увеличиваем счетчик его вхождений в исходную последовательность
            else:                                                   #иначе (если это слово еще не встречалось)
                word_dic.append(word)                               #добавляем его в список уникальных слов
                word_count.append(1)                                #инициализируем счетчик его вхождений единицей
            word = ''

    #добавляем списки уникальных слов и кол-ва их вхождений в один список
    #получаем что-то типа двумерного массива
    #один столбец - уникальные слова, второй - количество вхождений этого слова
    words.append(word_dic)              
    words.append(word_count)

    return words


