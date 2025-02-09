alphabet_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
message = input("ведите слово ").lower()
chiper = []
print(alphabet_ru[0],alphabet_ru[12],alphabet_ru[21])
step = int (input("введите шаг сдвига "))
for simbol in message:
    index = alphabet_ru.find(simbol)+step
    chiper.append(index)
print(chiper)
result = ""
for index in chiper:
    letter = alphabet_ru[index-step]
    result += letter
print(result)
