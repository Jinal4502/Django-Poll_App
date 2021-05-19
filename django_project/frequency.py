array = [56, 89, 1, 2, 7, 9, 6, 6, 2, 3, 1, 4, 5, 6, 8, 9, 9, 9, 5, 54, 56, 89, 7, 1, 2]
# key should be element
# value should be the frequency/count of an element present in the array
dictionary = dict()
for element in array:
    if element not in dictionary:
        dictionary[element] =  1
    else:
        dictionary[element] += 1       
print(*array)
print(sorted(array))
print(dictionary)