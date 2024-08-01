# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# Concatination +  is mainly used to add the two strings. joining of two strings is called concatinations.
'''
FirstName=input("enter the first name:")
LastName=input("enter the last name:")
FullName=FirstName+" " +LastName
print(FullName)

'''

# String Problms
'''
a="hello hai"
print(a)
b=""
print(b)
print(id(b))
print(a[1])   # output-e
print(a[2])   # output-l
print(a*4)   # repetation
'''

### MEMBERSHIP OPERATERS ..
##--> IN,NOTIN

'''a="hai hello bye"

print("hai" in a)   #true

print("no" in a)    # false

print("no" not in a)    #true'''

# you can return a range of characters using the slice syntax..
# syntax print(a[start:end:steps])

a="hai hello bye"

print(a[:13:1])     #hai hello bye

print(a[0::1])      #hai hello bye

print(a[4::1])       #hello bye

print(a[-1:-8:-1])   #eyb oll

print(a[-1:-14:-1])   #eyb olleh iah   

print(a[3:])          #hello bye

print(a[-4:])        # bye

print(a[:-4:1])     # hai hello

print(a[:])        #hai hello bye

t=len(a)

print(t)       #13


print(a[::-1])   #reverse the string

#######FUNCTIONS OF STRINGS

b='hai boys .hope you are doing great'

print(len(b))

print(b.capitalize())      #Hai boys .hope you are doing great

print(b.upper())          #HAI BOYS .HOPE YOU ARE DOING GREAT

print(b.lower())         # hai boys .hope you are doing great

print(b.title())        #Hai Boys .Hope You Are Doing Great(each character of first word should be upper).
