word = input("Напишите слово: ")

if word.lower() == word.lower()[::-1]:
    print("Слово полиндром")
else:
    print("Слово не полиндром")