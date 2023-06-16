# stroka = "aaabbbbccc"

# def str_count(stroka): # O(N ** 2)
#     for sym in set(stroka):
#         counter = 0
#         for i in stroka:
#             if sym == i:
#                 counter += 1
    
#         print(sym, counter)

# str_count(stroka=stroka)

def str_count(s): # O(N)
    dct = {}
    for sym in s:
        dct[sym] = dct.get(sym, 0) + 1
        for key, value in dct.items():
            print(key, value) 

str_count("aaaannnbbsssggf") 
