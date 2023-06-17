word = input("Напишите слово: ")

if word.lower() == word.lower()[::-1]:
    print(True)
else:
    print(False)