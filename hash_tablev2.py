
def hash_by_divide_10(list):
    dict_unique = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    for i in list:
        if i%10 in dict_unique.keys():
            if i not in dict_unique[i%10]:
                dict_unique[i%10].append(i)
    return  dict_unique
unique_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list=[829,1742,1544,1544,2544,2534,2535]
print(hash_by_divide_10(list))

