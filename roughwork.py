# ❗❗❗LISTS IN PYTHON ❗❗❗

marks= [94.5, 87.5, 95.2]
print(marks)
print(type(marks))
    # this is a list 

print(marks[1])
    #   indexes start from 0
    
student = ['John', 24, 3.8]
print(student)
    # can store different data types in a list 
    
student[0] = 'Jane'
print(student)
# can change the value of an element in a list

age= [20, 21, 22, 23]
print(age[1:3])
print(age[:2])
print(age[1:])
print(age[:])
print(age[-3:-1])
# list slicing
# negative indexing slicing

# ✏️LIST METHODS ✏️

#  append adds one element at the end
list1= [2, 1, 3]
list1.append(4)
print(list1)
 
#  sort() -- sorts the list in ascending order
list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)
# sort(reverse= True) --  sort in descending order

list1.reverse()
print(list1)
# reverse() -- reverse the list

list1.insert(2, 5)
print(list1)
# insert() -- insert element 5 at index 2 also shifts the elements to the right after index 2

list = [1, 2, 1, 3, 4]
list.remove(1)
print(list)
# remove() -- removes the first occurrence of element 1

list2= [1, 2, 3, 4]
list2.pop(1)
print(list2)
# pop() -- removes the element at index 1

list3= [5, 6, 7]
list4= list3.copy()
print(list3)
# copy() -- copies list3 to list4

print(len(list4))
# len() -- returns the length of the list

del list4[1]
print(list4)
# deletes the element at index 1 from list4

courses = ['Maths', 'Physics', 'Chemistry']
for course in courses:
    print(course)
    # iterating through a list using for loop
    
if 'Maths' in courses:
    print("Maths is present in the courses list")
else:
    print("Maths is not present in the courses list")
# checking if an element is present in the list using 'in' keyword


# ❗❗❗TUPLE IN PYTHON❗❗❗

tup= (1, 2, 3, 4)
print(type(tup))

# tup[0]= 5
# print(tup)
# # tuple is immutable i.e we cannot change the value of an element in a tuple

tup1 = ()
print(tup1)
# empty tuple

tup2= (5)
print(type(tup2))
# consider as an integer

tup3= ('john')
print(type(tup3))
# consider as a string

# if there is only one element in a tuple, we need to add a comma after the element
tup5 = (5,)
print(type(tup5))

# ✏️TUPLE METHODS ✏️

a= ( 2, 1, 3, 1)
print(a.index(3))
# index() -- returns the index of the first occurrence of the element 3

print(a.count(1))
# count() -- returns the total count of occureneces of element 


# ❗❗❗DICTIONARY IN PYTHON❗❗❗

# Used to store data in key-value pairs

info = {
    'key': 'value',
     'name': 'John',
      'age': 24,
      'subjects': ['Maths', 'Physics', 'Chemistry'],
      'topics': ("dictionary", 'set'),
      18 : 'eighteen',
      9.48: 'nine point four eight'
}
print(type(info))

# dictionaries are mutable
# they are unordered (no index)
# don't allow duplicate keys


# to print individual values, use the keys

print(info['name'])

info['name'] = 'gayathri'
print(info)

# can add new key-value pairs

info['grade'] = 'A'  
print(info)



