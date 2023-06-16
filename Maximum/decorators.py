import time

def list_by_deafult_way(val):
    start = time.time()
    my_list = []
    for i in range(val):
        my_list.append(i)

    print(time.time() - start)

    return my_list

def get_list_by_list_comp(val):
    start = time.time()
    print(time.time() - start)
    return [i for i in range(val)]

list_by_deafult_way(10 ** 6 * 15)
get_list_by_list_comp(10 ** 6 * 15)