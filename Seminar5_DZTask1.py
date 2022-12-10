# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.
# Пример:
# Пугать ты галок пугай => заданная строка "галок" => Пугать ты пугай
# Пугать ты галок пугай => заданная строка "пуг" => Пугать ты галок


# my_text = input("Введите текст через пробел:\n")
# print(f"Исходный текст: {my_text}")
# find_element = "галок"
# lst = [i for i in my_text.split() if find_element not in i]
# print(f'Конечный результат: {" ".join(lst)}')


user_text = input("Введите текст:\n").split()
user_word = input("Введите слово:\n")

def delete_word (user_text: list, user_word:str) ->str:
    final_text = " "
    for i in range (0,len(user_text)):
        if str (user_text[i]).find(user_word) == -1:
            final_text += user_text[i] + " "
    return final_text

print(delete_word(user_text, user_word))
