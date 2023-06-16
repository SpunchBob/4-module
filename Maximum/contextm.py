import time 


class Codetimer:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print(exc_type)
        # print(exc_val)
        # print(exc_tb)
        t = time.time() - self.start
        print(t)
        return True
        

session = Codetimer()

with session:
    l = [i for i in range(100)]
    l[101]