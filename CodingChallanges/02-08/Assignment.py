1- difference between extend and append?

append: Python list append function is a pre-defined function that takes a value as a parameter and adds it at the end of the list. 
append() function can take any type of data as input, including a number, a string, a decimal number,
a list, or another object.

a= [1,2,3,4]
b=["varun","Dharshan"]
a.append(b)
print(a)

print(a[4])  # append is use for adding value end of list 
# output -['varun', 'Dharshan']

extend: List extend() function is an in-built function of Python that extends a list by adding values of an iterable (list, tuple, string, etc)
at the end of that list.

a= [1,2,3,4]
b=["varun","Dharshan"]

a.extend(b)

print(a)     # extend is inbuld function in python.use for adding elements an iterable.
#output ->  [1, 2, 3, 4, 'varun', 'Dharshan']


2- difference between extend and concatenation?

extend: extend() is in build function of that extend a list by adding values an iterable.
  
a= [1,2,3,4]
b=["varun","Dharshan"]

a.extend(b)

print(a)     # extend is inbuld function in python.use for adding elements an iterable.
#output ->  [1, 2, 3, 4, 'varun', 'Dharshan']

Concatinations: Concatinations is nothing but adding two string or values etc. (+)

a= ["varun"]
b=["Dharshan"]
c=a+b
print(c)   # output ["varun","Dharshan"]

3) difference between insert and append?

Append: append functin is adding the element end of the list..
a=[1,2,3,4,5,6]
a.append(7)
print(a)   #output-[1, 2, 3, 4, 5, 6, 7]

insert: insert function is mainly used for adding the values in particular index value:

a=[1,2,3,4,5,7]
a.insert(5,"varun")
a.insert(3,232323)
print(a)        #output- [1, 2, 3, 232323, 4, 5, 'varun', 7]


4- difference between string and list?

string : string is nothing but a character squence. string is fallow "",' ' (double quotes or singe quotes)

list : list is nothing but collection of elements. each value has index values .. in list we can append the values 
remove the values and deleteing list.

5- name mutable and immutable data type.?
Mutable: lists are mutable .. mutable means you can change the list add the values delete the elements .. 

UnMutable : immutables are tapule.. once they createeeeevalues it is not possible to change..



6- what is the use of remove function in string?

Strings are data types used to represent text/characters. In this article, we present different methods for the problem 
                                                                                                         
  of removing the ith character from a string and talk about possible solutions that can be employed in achieving them using Python






