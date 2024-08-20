# Task 1: Implement a function to create a new list using list comprehension that 
# contains squares of numbers from 1 to n, where n is a parameter. 
# Analyze the time and space complexity of this operation.

def listComp(n):
    return [n*n for n in range(1, n + 1)]

print(listComp(9))

# According to bigocalc.com, The time complexity of this function is O(n) because 
# the list comprehension iterates over the range from 1 to n, performing a constant 
# amount of work for each iteration. The space complexity is also O(n) because the 
# function creates a list of size n to store the squared values.

# Task 2: Implement a function to merge two pre-sorted lists into a single sorted list.

def mergeList():
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 0]
    list3 = list1 + list2

    print(list3)

mergeList()

#The correct way to do it

l1 = [1,3,5,7,9]
l2 = [2,4,6,8]

def merge(list1, list2):

    one = 0
    two = 0
    merged = []

    while one < len(list1) and two < len(list2):

        if list1[one] < list2[two]:
            merged.append(list1[one])
            one += 1
        else:
            merged.append(list2[two])
            two += 1

    if one == len(list1):
        merged = merged + list2[two:]
    else:
        merged = merged + list1[one:]

    return merged

print(merge(l1,l2))












# According to bigocalc.com, The time complexity of this function is O(n), where n 
# is the total number of elements in both lists. This is because the function simply 
# concatenates the two lists together, which requires iterating through both lists 
# once to create the new merged list.

# The space complexity is also O(n), as the new merged list will contain all the 
# elements from both input lists. 

# Dictionaries

# Task 1 : Implement a function to merge two dictionaries, preserving the values of 
# common keys from the second dictionary. Analyze the time complexity of this operation.

def Merge(dict_1, dict_2):
    merged = (dict_1 | dict_2)
    print(merged)

dict_1 = {
'pie': 'apple',
'ice_cream': 'moose tracks',
'cobbler': 'peach',
'cake': None
}

dict_2 = {
'dinner': 'turkey',
'ice_cream': 'vanilla',
'appetizer': 'soup',
'cobbler': 'peach'
}

Merge(dict_1, dict_2)



# The time complexity of this Merge function is O(n), where n is the total number 
# of key-value pairs in both dictionaries. This is because the function iterates 
# through each key-value pair in both dictionaries and combines them into a new 
# dictionary.

# The space complexity is also O(n), as the function creates a new dictionary to 
# store the merged key-value pairs from both input dictionaries. The size of this 
# new dictionary will be equal to the total number of unique keys in both input 
# dictionaries.


# Task 2: Implement a function to find the intersection of two dictionaries, i.e.
# , keys common to both dictionaries along with their values. 

def intersection(dict_1, dict_2):
    intersected = dict(dict_1.items() & dict_2.items())
    print(intersected)

intersection(dict_1, dict_2)

# The time complexity of this function is O(min(n, m)), where n is the number of 
# key-value pairs in dict_1 and m is the number of key-value pairs in dict_2. This 
# is because the function iterates through the smaller of the two dictionaries to 
# find the intersection of key-value pairs.

# The space complexity of this function is O(min(n, m)), as the intersected dictionary 
# will contain at most min(n, m) key-value pairs.