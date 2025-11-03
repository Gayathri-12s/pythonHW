# import my_module as m # m is alias 

# from my_module import calculator as c  # "from" can be used if you want to import only a certain function from the module. also "c" alias can be given to calculator .
# # calculator(3,2)
# c(3,2)

#  print(my_module.a)
# print(m.a)
# print(my_module.area_of_square(4))

# from my_module import calculator, a, area_of_square
# print(a)
# print(area_of_square(4))

from my_module import *  # '*' can print everything  
print(a)
print(area_of_square)
calculator(2,4)

