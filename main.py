
list1 = [x ** 2 for x in range(1,11)]

print(list1)


#func of sum
def sum(a ,b):
    return a + b


#func of union set
def union_set(set1:set,set2:set) -> set:
    return set1.union(set2)


#func of unique list
def unique_list(list1:list) -> list:
    return list(set(list1))


#func function that counts letters
def count_char_in_text(text:str, enter_char: str)  -> int :
    counter = 0
    for char in text:
        if char == enter_char:
            counter += 1
    return counter