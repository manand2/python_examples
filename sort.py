# sorting lists, tuples, dictionary, and objects

# simple list of integers

li = [9,1,8,2,7,3,6,4,5]
# using sorted function here
s_li = sorted(li)

# s_li is sorted list while li is origina list

s_li = sorted (li, reverse=True)

# sort method also can be used on the list, however this will sort the original list
li.sort
# will sort the original list
li.sort(reverse=True)

# sorted function gives more flexible and can be used on other objects, tuple does
# not have sort method

tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup)
print('Tuple\t', s_tup)

# dictionary 
 di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print('Dict\t', s_di)

# sort integers based on absolute value)

li = [-6,-5,-4,1,2,3]
s_li = sorted(li)  # regular sorting 
print (s_li)

s_li = sorted(li, key=abs)

# key parameter is important 


