def compressor(dict):    
    for a in (dict.items()):
        key_val_a = list(a)
        all_dict[key_val_a[0]] = key_val_a[1]

dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}
dict_d = {7:70, 8:80}
all_dict = {}

compressor(dict_a)
compressor(dict_b)
compressor(dict_c)
compressor(dict_d)

print(all_dict)



