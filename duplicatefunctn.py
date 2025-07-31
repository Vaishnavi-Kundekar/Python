def Remove(duplicate):
    final_list=[]
    for n in duplicate:
        if n not in final_list:
            final_list.append(n)
    return final_list

duplicate=[2,4,6,7,2,6,10]
print(Remove(duplicate))