# Constant Time

#Assignment ops
x = 2

#Math Ops(+,-,*,/,%)
y = 7
z = x + y

#Comparison Ops
z > x

#Logrighmie: Binary Search is a great example of logrithmic time complexity

#Linear Time: O(n) - Operations for each piece of data input into the solution

def double_evens(alist):
    output = [] # Constant assignment

    for num in alist:# Linear Loop
        if num % 2 == 0:# Constant math, and comparison
            output.append(num * 2)# Constant append
        else:
            output.append(num)

    return output

# Stacked for loops are okay, as long as they are not nested

def double_split(alist):

    evens = []
    odds = []

    for num in alist:
        if num % 2 == 0:
            evens.append(num)

    for num in alist:
        if num % 2 != 0:
            odds.append(num*2)
                        
    return (evens, odds)

#Linear Log : Sorting .sort() and sorted() are examples of linear log time complexity

def sort_nums(alist):

    return sorted(alist) # Anytime you sort within a function you are creating a O(n log n) time complexity and is ok but try to avoid it

#Quadratic Time: O(n^2) - Nested loops

def small_run(alist):
    for num2 in alist:
        print(num2)

def nesting(alist):

    for num1 in alist:
        print('Run', num1)
        small_run(alist)# Do not nest loops, this is a bad practice espedially if it is another function

alist = [1,2,3,4,5]
nesting(alist)



#BE CAREFUL OF ADDING METHODS INSIDE OF A FOR LOOP

def count_repeats(alist):

    for num in alist:
        repeats = alist.count(num)
        print(str(num) + 'repeats' + str(repeats) + 'times')

count_repeats([1,1,2,3,3,4,4,4,4,5,5,6,6,7,6])

#This is a bad practice because it is a nested loop, and it is not necessary to use a loop to count the number of times a number repeats in a list

if 1 in alist:
    print('got 1')# Membership checks in a list are linear time complexity

('https://www.bigocheatsheet.com/')
('https://www.bigocalc.com')