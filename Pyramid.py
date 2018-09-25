# Assignment - Algorithms Practice



# Assignment 1 - Remove Duplicates

names = ["Alex","John","Mary","Steve","John", "Steve"]
x = []

for name in names:
    if name in x:
        pass
    else:
        x.append(name)
print(x)

# Assignment 2 - Largest number

list = [1,2,3,4,5,6,7,8,9]
largest = max([1,2,3,4,5,6,7,8,9])

print(largest)


# Assignment 3 - Smallest number

list = [1,2,3,4,5,6,7,8,9]
smallest = min([1,2,3,4,5,6,7,8,9])

print(smallest)


# Assignment 4 - Pyramid

j = 9

for i in range (1,18,2):  
    print(" " * j+i * "*")
    j = j -1
