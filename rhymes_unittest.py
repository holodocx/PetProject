import pronouncing
import unittest  #Нужно добавить модуль unittest

# Функция для поиска рифмующихся слов
def find_rhymes(word):
    return pronouncing.rhymes(word)

# Класс для юнит-тестов
class TestFindRhymes(unittest.TestCase):
    # Тестируем поиск рифм
    def test_find_rhymes(self):
        word = "cat"
        # Проверяем, что рифмы для слова найдены
        self.assertTrue(find_rhymes(word))

# Запуск тестов
if __name__ == '__main__':
    unittest.main()
