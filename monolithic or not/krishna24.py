def monolithicOrNot(values):
    values_set=set()
    for i in values:
        values_set.add(type(i))
    if len(values_set) == 1:
        print("Monolithic Array")
    else:
        print("Not a Monolithic Array")

#1 array is full of int values
array1 = [1,2,3,4]
monolithicOrNot(array1)

#2nd array is full of Str values
array2 = ['a','b','c','d']
monolithicOrNot(array2)