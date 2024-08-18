first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (len(word1) - len(word2) for word1, word2 in zip(first, second) if len(word1) != len(word2))
second_result = (True if len(first[i]) - len(second[i]) else False for i in range(len(first)))
print(list(first_result))
print(list(second_result))
