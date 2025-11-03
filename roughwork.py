# # ❗❗❗LISTS IN PYTHON ❗❗❗

# marks= [94.5, 87.5, 95.2]
# print(marks)
# print(type(marks))
#     # this is a list 

# print(marks[1])
#     #   indexes start from 0
    
# student = ['John', 24, 3.8]
# print(student)
#     # can store different data types in a list 
    
# student[0] = 'Jane'
# print(student)
# # can change the value of an element in a list

# age= [20, 21, 22, 23]
# print(age[1:3])
# print(age[:2])
# print(age[1:])
# print(age[:])
# print(age[-3:-1])
# # list slicing
# # negative indexing slicing

# # ✏️LIST METHODS ✏️

# #  append adds one element at the end
# list1= [2, 1, 3]
# list1.append(4)
# print(list1)
 
# #  sort() -- sorts the list in ascending order
# list1.sort()
# print(list1)

# list1.sort(reverse=True)
# print(list1)
# # sort(reverse= True) --  sort in descending order

# list1.reverse()
# print(list1)
# # reverse() -- reverse the list

# list1.insert(2, 5)
# print(list1)
# # insert() -- insert element 5 at index 2 also shifts the elements to the right after index 2

# list = [1, 2, 1, 3, 4]
# list.remove(1)
# print(list)
# # remove() -- removes the first occurrence of element 1

# list2= [1, 2, 3, 4]
# list2.pop(1)
# print(list2)
# # pop() -- removes the element at index 1

# list3= [5, 6, 7]
# list4= list3.copy()
# print(list3)
# # copy() -- copies list3 to list4

# print(len(list4))
# # len() -- returns the length of the list

# del list4[1]
# print(list4)
# # deletes the element at index 1 from list4

# courses = ['Maths', 'Physics', 'Chemistry']
# for course in courses:
#     print(course)
#     # iterating through a list using for loop
    
# if 'Maths' in courses:
#     print("Maths is present in the courses list")
# else:
#     print("Maths is not present in the courses list")
# # checking if an element is present in the list using 'in' keyword


# # ❗❗❗TUPLE IN PYTHON❗❗❗

# tup= (1, 2, 3, 4)
# print(type(tup))

# # tup[0]= 5
# # print(tup)
# # # tuple is immutable i.e we cannot change the value of an element in a tuple

# tup1 = ()
# print(tup1)
# # empty tuple

# tup2= (5)
# print(type(tup2))
# # consider as an integer

# tup3= ('john')
# print(type(tup3))
# # consider as a string

# # if there is only one element in a tuple, we need to add a comma after the element
# tup5 = (5,)
# print(type(tup5))

# # ✏️TUPLE METHODS ✏️

# a= ( 2, 1, 3, 1)
# print(a.index(3))
# # index() -- returns the index of the first occurrence of the element 3

# print(a.count(1))
# # count() -- returns the total count of occureneces of element 


# # ❗❗❗DICTIONARY IN PYTHON❗❗❗

# # Used to store data in key-value pairs

# info = {
#     'key': 'value',
#      'name': 'John',
#       'age': 24,
#       'subjects': ['Maths', 'Physics', 'Chemistry'],
#       'topics': ("dictionary", 'set'),
#       18 : 'eighteen',
#       9.48: 'nine point four eight'
# }
# print(type(info))

# # dictionaries are mutable
# # they are unordered (no index)
# # don't allow duplicate keys


# # to print individual values, use the keys

# print(info['name'])

# info['name'] = 'gayathri'
# print(info)

# # can add new key-value pairs

# info['grade'] = 'A'  
# print(info)


# ❗❗❗CONDITIONAL STATEMENTS❗❗❗


# age = 21

# if age >= 18:
#     print("You are eligible to vote.")
#     print("can drive")
    
#                        ✏️IF ELSE STATEMENT✏️
# age=24
# if(age>18):
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")



#                           ✏️ELIF STATEMENT✏️

# light= 'green'
# if light == 'red':
#     print("Stop")
# elif light == 'yellow':
#     print("Get Ready")
# elif light == 'green':
#     print("Go")
    
# print("End of the program")

#                       ✏️ELIF else statement✏️

# light= 'pink'
# if light == 'red':
#     print("Stop")
# elif light == 'yellow':
#     print("Get Ready")
# elif light == 'green':
#     print("Go")
      
# else:
#     print("Invalid color")  #indentatation (proper spacing instead of curly braces)
    
# print("End of the program")


# marks = 85 
# marks = int(input("enter your marks: ")) # getting input from the user 

# if(marks>=90):
#     grade='A'
    
# elif(marks>=80 and marks<90):
#     grade='B'
    
# elif(marks>=70 and marks<80):
#     grade='C'
# else:
#     grade='D'
# print("Your grade is:", grade)

#                   ✏️NESTED IF-ELSE✏️

# age = 10
# if (age>=18):
#     if(age>=65):
#         print("cannot drive ")
#     else:
#          print("can drive") 
# else:
#     print("cannot drive")


#    ❗❗❗LOOPS❗❗❗

# loops are used to repeat instructions .

#                   ✏️while loops✏️











#   ❗❗❗OOPS IN PYTHON❗❗❗


# TO MAP REAL WORLD SCENARIOS WE STARTED USING OBJECTS IN CODE .
# THIS IS CALLED OBJECT ORIENTED PROGRAMMING .

#         ✏️CLASSES AND OBJECTS✏️

# CLASS IS A BLUEPRINT FOR CREATING OBJECTS .


# creating a class 
# class student:
#     name = 'John'
   
# creating an object (instance of class)
# s1= student()
# print(s1.name)


#        ✏️ Class and Instance Attributes✏️


# class student:
#     college = "ABC College"   # class attribute (same for all objects take only one memory location)
#     def __init__(self, name, marks):
#         self.name = name   # instance attribute different for every object 
#         self.marks = marks     # instance attribute
# s1 = student("John", 95)

# s2 = student("Jane", 88)

# print(s1.college)
# print(s2.college)
# # also
# print(student.college)  # accessing class attribute using class name



#              ✏️--INIT-- FUNCTION✏️  (short for 'initialize')

# CONSTRUCTORS IN PYTHON  
# (ALL CLASSES HAVE A FUNCTION CALLED __INIT__(), WHICH IS ALWAYS EXECUTED WHEN THE OBJECT IS BEING INITIATED .)

# class student:
#     name = 'John'
#     def __init__(self):  # self kodthillel error varum 
#         print("adding new student in database")
#         print(self)
# s1 = student()   #--this will automatically call the (constructor or init.)
# print(s1)    #s1= student() and self  both are same  
    #   objects points to self (parameter)
    
    # we should always pass an argument to the constuctor.
    
                                            
    
# class student:   #self will always be the first parameter.
    # def __init__(self, fullname):
    #     self.name = fullname
        # inside name variable(called as attribute) we store the value of fullname parameter.
# s1= student("john")
# print(s1.name)

# default constructors
# class student:
#     def __init__(self):  #only one parameter .
        
# parameterised constructors
# class student:
#     def __init__(self, name, age): # there are other parameters other than self.


# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def welcome(self):
#         print("Welcome", self.name) 
#     def get_marks(self):
#         return self.marks
# s1 = student("John", 24)
# s1.welcome()
# print(s1.get_marks()) # calling method using object

# ✏️Static Method✏️

# METHODS THAT DON'T USE THE SELF PARAMETER (work at class level)
# @staticmethod  (called as decorator)


# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def welcome(self):
#         print("Welcome", self.name) 
#      @staticmethod 
#     def hello():
#         print("Hello Students")
    
#     def get_marks(self):
#         return self.marks
# s1 = student("John", 24)
# s1.welcome()
# s1.hello()
# print(s1.get_marks())


# Abstraction✏️

#  Hiding the implementation details of a class and only showing the essential features to the user.

# Encapsulation✏️

# Wrapping data and functions into a single unit (object). 


























# ✏️INHERITANCE✏️

# WHEN ONE CLASS (Child/Derived) DERIVES THE PROPERTIES AND METHODS OF ANOTHER CLASS (Parent/Base). here properties and methods mean attributes .

# class car:
#     @staticmethod
#     def start():
#         print("car started")
        
#     def stop():
#         print("car stopped")
        
# class electriccar(car):  # electriccar is inheriting the properties of car class
#     def __init__(self, name):
#         self.name = name

# car1 = electriccar("Tesla") 
# car2 = electriccar("Nissan")
    #  multi-level inheritance
# print(car1.start())  #start() method inherited from car class
# print(car2.name)


# good example 1

# class Human:
#     def eat(self):
#         print("I can eat")
#     def work(self):
#         print("I can work")
        
# class Male(Human):
#     def sing(self):
#         print("I can sing ")
        
# male_1 = Male()
# male_1.eat()


# # example 2

# class Human:
#     def eat(self):
#         print("I can eat")
#     def work(self):
#         print("I can work")
        
# class Male(Human):
#     def sing(self):
#         print("I can sing ")
        
#     def work(self):   #shows overriding 
#         print("I can code ")  
        
# male_1 = Male()
# male_1.eat()
# male_1.work()  # i can code   but if ypu give super 
# # =====================================================

# class Human:
#     def eat(self):
#         print("I can eat")
#     def work(self):
#         print("I can work")
        
# class Male(Human):
#     def sing(self):
#         print("I can sing ")
        
#     def work(self):
#         super().work()  #calls work from parent class
#         print("I can code ")
        
# male_1 = Male()
# male_1.eat()
# male_1.work() # i can work also shows 
# # =======================================================

# class Human:
#     def __init__(self):
#         self.num_eyes = 2
#         self.num_nose = 1
#     def eat(self):
#         print("I can eat")
#     def work(self):
#         print("I can work")
        
# class Male(Human):
#     def sing(self):
#         print("I can sing ")
        
#     def work(self):
#         super().work()  
#         print("I can code ")
        
        
# male_1 = Male()
# male_1.eat()
# male_1.work()
# print(male_1.num_eyes) # it can print 2 since it inherits from parent class

# # but when a constructor is given to the child class then it cant 

# class Human:
#     def __init__(self):
#         self.num_eyes = 2
#         self.num_nose = 1
#     def eat(self):
#         print("I can eat")
#     def work(self):
#         print("I can work")
        
# class Male(Human):
#     def __init__(self, name):
#         self.name = name 
   
#     def sing(self):
#         print("I can sing ")
        
#     def work(self):
#         super().work()  
#         print("I can code ")
        
        
# male_1 = Male() # shows error since no argument is passed 
# male_1.eat()
# male_1.work()
# print(male_1.num_eyes) # it can print 2 since it inherits from parent class

# ===============================================
# class Human:
#     def __init__(self):
#         self.num_eyes = 2
#         self.num_nose = 1
#     def eat(self):
#         print("I can eat")
#     def work(self):
#         print("I can work")
        
# class Male(Human):
#     def __init__(self, name):
#         self.name = name 
#     def sing(self):
#         print("I can sing ")
        
#     def work(self):
#         super().work()  
#         print("I can code ")
        
        
# male_1 = Male("John")
# male_1.eat()
# male_1.work()
# print(male_1.num_eyes) # shows error 
# =============================================

# class Human:
#     def __init__(self):
#         self.num_eyes = 2
#         self.num_nose = 1
#     def eat(self):
#         print("I can eat")
#     def work(self):
#         print("I can work")
        
# class Male(Human):
#     def __init__(self, name):
#         super().__init__() #now can get num_eyes from base class 
#         self.name = name 
#     def sing(self):
#         print("I can sing ")
        
#     def work(self):
#         super().work()  
#         print("I can code ")
        
        
# male_1 = Male("John")
# male_1.eat()
# male_1.work()
# print(male_1.num_eyes) #to access this we need to give super function .
# =========================================================

# class Human:
#     def __init__(self, num_heart):
#         self.num_eyes = 2
#         self.num_nose = 1
#         self.num_heart = num_heart
#     def eat(self):
#         print("I can eat")
#     def work(self):
#         print("I can work")
        
# class Male(Human):
#     def __init__(self, name, heart): #can also give num_heart too parameter name doesnt matter.
#         super().__init__(heart) 
#         self.name = name 
#     def sing(self):
#         print("I can sing ")
        
#     def work(self):
#         super().work()  
#         print("I can code ")
        
        
# male_1 = Male("John", 1)
# male_1.eat()
# male_1.work()
# print(male_1.num_eyes)
# print(male_1.num_heart) # num_heart thanne vilikanm

# ==================================================

# multiple inheritance

# class Human:
#     def eat(self):
#         print("i can eat")
#     def work(self):
#         print(" i can work")
# class Male:
#     def sing(self):
#         print("i can sing")
#     def work(self):
#         print(" i can code")
    
# class boy(Human, Male):  # (Male, Human) this will give me ---i can code as output
#     pass
        
# boy_1 = boy()
# boy_1.sing()
# boy_1.work() # i can work this points to human class
# Male.work(boy_1) 
# ============================================================

# class Human:
    
#     def eat(self):
#         print("i can eat")
#     def work(self):
#         print(" i can work")
# class Male:
#     def sing(self):
#         print("i can sing")
#     def work(self):
#         print(" i can code")
    
# class boy(Human, Male):
#     pass
        
# boy_1 = boy()
# boy_1.sing()
# # boy_1.work() 
# Male.work(boy_1) # can access by giving calling class name with method name and object as argument since no obj for male class.

# =============================================================================

# class Human:
  
#     def eat(self):
#         print("i can eat")
#     def work(self):
#         print(" i can work")
# class Male:
    
#     def sing(self):
#         print("i can sing")
#     def work(self):
#         print(" i can code")
    
# class boy(Human, Male):
#     def sleep(self):
#         print("i can sleep")
#     def work(self):
#         print("i can test")
        
# boy_1 = boy()
# # boy_1.sing()
# boy_1.work() # gives i can test
# # Male.work(boy_1)
# print(boy.mro())  #  mro (method resoltution order) [<class '__main__.boy'>, <class '__main__.Human'>, <class '__main__.Male'>, <class 'object'>]
# =====================================================================================

# class Human:
#     def __init__(self):
#         self.num_eyes = 2
#         self.num_nose = 1
    
#     def eat(self):
#         print("i can eat")
#     def work(self):
#         print(" i can work")
# class Male:
#     def __init__(self, name):
#         self.name = name 
#     def sing(self):
#         print("i can sing")
#     def work(self):
#         print(" i can code")
    
# class boy(Human, Male):
#     def sleep(self):
#         print("i can sleep")
#     def work(self):
#         print("i can test")
        
# boy_1 = boy()
# print(boy_1.num_nose)
# print(boy_1.name) #shows error because acc to mro it will check class boy there no inint fun so goes to human but there no name argument so shows error.
# ===========================================================================================


# class Human:
#     def __init__(self, num_heart):
#         self.num_eyes = 2
#         self.num_nose = 1
#         self.num_heart = num_heart
    
#     def eat(self):
#         print("i can eat")
#     def work(self):
#         print(" i can work")
# class Male:
#     def __init__(self, name):
#         self.name = name 
#     def sing(self):
#         print("i can sing")
#     def work(self):
#         print(" i can code")
    
# class boy(Human, Male):
#     def __init__(self, name, heart, language):
#         self.language = language 
#         Human.__init__(self, heart)
#         Male.__init__(self, name)
        
#     def sleep(self):
#         print("i can sleep")
#     def work(self):
#         print("i can test")
        
#     def display(self):
#         print(f" Hi I am {self.name} and I work on {self.language}")
        
# boy_1 = boy("john", 1, 'python')
# # print(boy_1.num_nose)
# # print(boy_1.name)
# # print(boy_1.num_heart)
# # print(boy_1.language)
# boy_1.display()

# =============================================================================

# MULTILEVEL INHERITANCE

# class Human:
#     def eat(self):
#         print("I can eat")
        
#     def work(self):
#         print("I can work")
        
# class Male(Human):
#     def sleep(self):
#         print("I can sleep")

# class Boy(Male):
#     def work(self):
#         print("I can code")

# boy_1 = Boy()
# boy_1.eat() # i can eat.
# boy_1.work()  # i can code from class boy (mro).

# if you want to access the other work then
# =======================================================================

# class Human:
#     def eat(self):
#         print("I can eat")
        
#     def work(self):
#         print("I can work")
        
# class Male(Human):
#     def sleep(self):
#         print("I can sleep")

# class Boy(Male):
#     def work(self):
#         # Human.work(self)
#         super().work()
#         print("I can code")

# class programmer(Boy):
#     def work(self):
#         super().work()
#         print("i can write programm")
        
# boy_1 = Boy()
# prog_1= programmer()
# boy_1.eat() 
# boy_1.work() 
# prog_1.work()

# ===============================================================================

# class Human:  
#     can_breath= True #  class variable. can be accessed without init constr.
#     def __init__(self, num_heart):
#         self.num_eyes = 2
#         self.num_heart = num_heart
#         print("calling init from human class")
        
#     def eat(self):
#         print("I can eat")
        
#     def work(self):
#         print("I can work")
        
# class Male(Human):
#     def __init__(self, name):
#         self.name = name
        
#     def sleep(self):
#         print("I can sleep")

# class Boy(Male):
#     def __init__(self, heart, name, dance):
#         self.can_dance = dance
#         Human.__init__(self, heart)
#         Male.__init__(self, name)
        
#     def work(self):
#         super().work()
#         print("I can code")


        
# boy_1 = Boy(1, 'rahul', 'kathak')
# print(boy_1.num_eyes)
# print(boy_1.num_heart)
# print(boy_1.can_dance)
# print(boy_1.can_breath)
# print(Boy.mro())





# multiple inheritance

# class A:
#     varA = "welcome to class A"
    
# class B:
#     varB = "welcome to class B"
    
# class C(A, B):
#     varC = "welcome to class C"
    
# c1= C()
# print(c1.varA)
# print(c1.varB)

# ✏️Super Method✏️

# super() method is used to access the methods of parent class

# class Car:
#     def __init__(self, type):
#         self.type = type  #parent class attribute
#     @staticmethod   
#     def start():
#         print("car started")
#     @staticmethod  
#     def stop():
#         print("car stopped")
        
# class Toyota(Car):
#     def __init__(self, name, type):
#         self.name = name
#         # self.type = type  # i need type from parent class 
#         super().__init__(type)  # calling parent class constructor
#            #  now no error will come .
#         super().start()  # calling parent class method
# car1 = Toyota("Innova", 'SUV')
# print(car1.type)  #error because type is not defined in Toyota class  

# #          ✏️POLYMORPHISM✏️

# # WHEN THE SAME FUNCTION IS ALLOWED TO HAVE DIFFERENT MEANING ACCORING TO THE CONTEXT.


# print(1+2) #3
# print("gayathri"+"sunil") #gayathrisunil
# print([1,2,3]+[4,5,6]) #merge        # overloading  + pala meaning akm.


# =====================================================================================================

            #   ✏️MODULES✏️

# improve code reusability, reduce time , maintain the project , more redable

# types of module: 1. built in 
#                  2. create your own

# print(help ("modules")) #to check the modules.
# if you want to import any module just write import and name of the module.

# import math
# print(math.e)

# creating your on module

# ✏️ABSTRACTION✏️

# generalizing something to hide the complex part. 

# ABSTRACT CLASSES AND ABSTRACT METHODS


# class Vehicle:  #general class and blueprint for other classes 
#     def __init__(self, n):
#         self.no_of_tyres = n
#     def start(self):
#         pass 

# class Bike:
#     def __init__(self):
#         self.no_of_tyres = 2
#     def start(self):
#         print("start with kick") 
        
# class Scooty:
#     def __init__(self):
#         self.no_of_tyres = 2
#     def start(self):
#         print("self start")
        
# class Car:
#     def __init__(self):
#         self.no_of_tyres = 4
#     def start(self):
#         print("start with key")
# v = Vehicle()# in this object we dont know what no of tyres to pass as well as the method is empty so we want to restrict any one from making this class an object then we give abstract to it.   object should be like actual thing like bike 
# ==========================================================================================
 
 
# from abc import ABC , abstractmethod
 
# class Vehicle(ABC):
    
#     def __init__(self, n):
#         self.no_of_tyres = n
#     @abstractmethod   #   without this it will show error ( decorator )  
#     def start(self):  # this method is not considered abstract method , we need to make it abstract by providing  → abstractmethod (decorator)
#         pass 

# class Bike(Vehicle):
#     def __init__(self, n , color):
#         super().__init__(n)
#         self.color = color
#     def start(self):
#         print("start with kick") 
        
# class Scooty(Vehicle):
#     def __init__(self, n):
#         self.no_of_tyres = n
#     def start(self):
#         print("self start")
        
# class Car(Vehicle):
#     def __init__(self, n, gear):
#         self.no_of_gear = gear
        
#     def start(self):
#         print("start with key")


# bike =  Bike(2, "black")
# print(bike.color)
# bike.start()
# ====================================================================================================

# ✏️Acess Specific in Python✏️


# 1. public   (attributes and method can be used outside)
# 2. protected (not everyone can use )
# 3. private (not for everyone except you)

# class student:     # by default this is public.
#     def __init__(self, name):
#         self.name=name
        
#     def display(self):
#         print(f"hi myself {self.name} from student class")
        
# s1 = student("rahul")
# print(s1.name)
# s1.display()        
# # ============================================================================

# class student:
#     def __init__(self, name, rollno, age):  #parameter kodkilla '_' .
#         self.name=name  # public.
#         self._rollno = rollno #protected attribute.
#         self.__age = age
#     def __display(self):
#         print(f"hi myself {self.name} from student class")

# class branch(student):
#     pass 
# s1 = student("rahul", 23, 14)   
# # b1 = branch("nisha", 22, )
# # print(b1.name )
# # print(b1._rollno)
# s1.__display()
# print(s1.__age)    #its private cannot access it outside the class.
# s1 = student("rahul")
# print(s1.name)
#    




#     ❗ENCAPSULATION❗ 


# wrapping up of data into a single unit
# actual hiding of data is done , but in abstraction we are only finding out which data to be hidden from the user.




# ❗POLYMORPHISM❗

# means many forms 

print(1+2)  #add
print("1"+"2") #concat



