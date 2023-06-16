# class MyFile:
#     def __init__(self, file_name, read_type, encoding):
#         self.file_name = file_name
#         self.read_type = read_type
#         self.encoding = encoding

#     def __enter__(self):
#         self.file = open(f'{self.file_name}', f'{self.read_type}', encoding=f'{self.encoding}')
#         print(f"Файл {self.file_name}, с кодировокой {self.encoding} и режимом: {self.read_type}, открыт и готов к работе")
#         return self.file
    
#     def __exit__(self):
#         print(f"Файл {self.file_name} закрыт")
#         self.file.close()


# session = MyFile(file_name="test.txt", read_type="r", encoding="utf-8")
# session.__enter__()
# session.__exit__()


a = [1, 2, 3]

b = iter(a)
print(b)
