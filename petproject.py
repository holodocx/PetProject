import pronouncing #Импорт библиотеки pronouncing (CMU! только английские слова)

def find_rhymes(word): #Функция, которая принимает параметр word
    rhymes = pronouncing.rhymes(word) #Функция rhymes из библиотеки pronouncing
    return rhymes #Возврат списка рифмующихся слов

input_word = input("Enter a word to search for rhymes: ") #Запрос слова у пользователя

rhyming_words = find_rhymes(input_word) #Поиск рифмы

if rhyming_words: #Если список содержит хоть слово:
    print("Rhymes for the word "+(input_word)+":") #Вывод рифм
    print(", ".join(rhyming_words)) #в одну строку
else: #Если в словаре нет рифмы:
    print("No rhymes found for "+(input_word)+".") #Вывод сообщения

