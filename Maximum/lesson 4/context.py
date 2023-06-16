from contextlib import contextmanager

# f = open('test.text', 'w', encoding='utf-8')
# f.write("Скоро лето")
# f.close()

# with open('test.txt', 'w', encoding='utf-8') as f:
#     f.write("Люблю лето")

my_list = [1, 2]
@contextmanager
def exc_handler(exc):
    try:
        yield True
    except exc:
        print('Была ошибка, но мне окей')
    
with exc_handler(IndexError):
    my_list[5]