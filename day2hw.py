multiline = ''' This Python course introduces the basics of programming using Python.
It covers data types, loops, functions, file handling, and object-oriented programming. 
Students gain hands-on experience through exercises and projects, learning to write clean and efficient code.
By the end, learners can build simple applications and automate tasks, preparing for careers in software or data fields.
The Python course covers core programming concepts such as variables, loops, functions, and file handling. 
Students practice through real-world exercises and projects, gaining the skills to create basic programs and automation scripts useful for software, data, and web development careers.'''


print(len(multiline))

print(multiline[0:51])

print(multiline.replace("Python", "PYTHON"))

print(multiline.lower())

multiline_split = multiline.split()
print(multiline_split)

a = "course" in  multiline
print(a)

print("The course description is {} characters long and has {} words" .format(len(multiline), len(multiline_split)))
