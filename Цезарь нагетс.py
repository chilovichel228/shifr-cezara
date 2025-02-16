alphabet_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
Alphabet_EN = "abcdefghijklmnopqrstuvwxyz"
lang = input("Выберите язык en/ru ")
if lang == "en":
    alphabet = Alphabet_EN
else:
    alphabet = alphabet_ru
message = input("ведите слово ").lower()
chiper = []
step = int (input("введите шаг сдвига "))
for simbol in message:
    index = alphabet.find(simbol)+step
    chiper.append(index)
print(chiper)
result = ""
for index in chiper:
    letter = alphabet[index-step]
    result += letter
print(result)
