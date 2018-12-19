 
tag = 'h1'
text = 'This is a headline'

sentence = '<{0}>{1}<{0}>'.format(tag,text)
print(sentnence)

#accessing elements from a dictionary and print
sentence = 'My name is {0} and I am {1} years old.'.format(person[name],person[age])
print(sentence)


sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence)

#dictionary and create a list and print a list
person = {'name': 'Jenn', 'age': 23}

#list
l = ['Jenn', 23]

sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(l)
print(sentence)

#let us define a class and print an instance of a class
class Person():
  
     def __init__(self,name,age):
         self.name = name
         self.age = age

 p1 = Person('Jack', '33')

 sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
 print(sentence)
    
#print using keys in the format and unpack the dictionary

 person = {'name': 'Jenn', 'age': 23}
 sentence = 'My name is {name} and I am {age} years old.'.format(**person)
 print(sentence)

# print integesrs

for i in range(1,11):
    sentence = 'The value is { }'.format(i)
    print(sentence)

# print 2 digit format - 01, 02, 03
for i in range(1,11):
    sentence = 'The value is {:02}'.format(i)
    print(sentence)

#format decimal places

pi = 3.14159265

sentence = 'Pi is equat to {:.3f}'.format(pi)
print(sentence)

#print out large numbers with comma separater -  add comma after colon

sentence = "1 MB is to {:,} bytes'.format(1000**2)
print(sentence)

#print out dates, time
import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)

sentence = '{:%B %d, %Y}'.format(my_date)

# look up doc for datetime module to figure out what you want to use

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)


  

