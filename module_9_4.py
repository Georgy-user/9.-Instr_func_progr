print('Пример работы Lambda-функции:')
first = 'Мама мыла раму'
second = 'Рамена мало было'

mp = map(lambda str1, str2: True if str1 == str2 else False, first, second)
print(list(mp))
print()

print('Пример результата Замыкания см. в example.txt.')


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for line in data_set:
                line = str(line)
                file.seek(0)
                file.write(line + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка.', ['А', 'это', 'уже', 'число', 5, 'в', 'списке.'])
print()

print('Пример использования метода __call__:')
from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
