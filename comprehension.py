# list comprehension

nums = [1,2,3,4,5,6,7,8,9,10]
# I want 'n' for each 'n' in nums

my_list = []
for n in nums:
  my_list.append(n)
print my_list

#list comprehension instead of for loop
my_list = [n for n in nums]
print my_list

# more complicated example

# I want 'n*n' for each 'n' in nums

my_list = [n*n for n in nums]
print my_list

#another way to do this is using maps and lambda
# maps pretty much runs through functions
#lambda is a function
#using map + lambda
my_list = map(lambda n: n*n, nums)
# you can convert map and lambda to list comprehension as it is more readable
#learn map, lambda and filter

#I want 'n' for each 'n in nums if 'n' is even

my_list = []
for n in nums:
   if n%2 == 0:
       my_list.append(n)
print my_list

# using list comprehension

my_list = [n for n in nums if n%2 == 0]
print my_list

# Using a filter + lambda

my_list = filter(lambda n: n%2 == 0, nums)
print my_list

# more difficult example
# I want a letter and number pair for each letter in 'abcd' and each number in '0123'

my_list = [(letter,num) for letter in 'abcd' for num in range(4)]]


#dictionary and sets comprehension

# Dictionary comprehension
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# using for loop
for name in names:
    for hero in heros:
       my_dict[name] = hero
print my_dict

# using dictionary comprehension

my_dict = {name:hero for name, hero in zip(names, heros)}
print my_dict

#if name is not equal to Peter

my_dict = {name:hero for name, hero in zip(names, heros) if name != 'Peter'}
print my_dict


# set comprehension - similar to list but have unique values

nums = [1,1,2,2,3,3,4,4,5,5,6,7,8,9,9]

my_set = {n for n in nums}


# generators expression
# generators expressions are like list comprehension
def gen_func(nums):
   for n in nums:
      yield n*n

my_gen = gen_func(nums)

for in my_gen:
   print i

# let us change for loop code to comprehension

my_gen = (n*n for in in  nums)

for i in my_gen:
   print i
