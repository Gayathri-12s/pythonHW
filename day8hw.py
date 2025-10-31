
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
       


class Trainer(Employee):
    def __init__(self, name, role, specialization):

        Employee.__init__(self, name, role)
        self.specialization = specialization

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)
 


class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
      
        Employee.__init__(self, name, role)
        self.yoga_style = yoga_style

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Yoga Style:", self.yoga_style)
      


class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
      
        Employee.__init__(self, name, role)   
        self.specialization = specialization   
        self.yoga_style = yoga_style           

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)
        print("Yoga Style:", self.yoga_style)
       


emp1 = Employee("Anu", "Receptionist")
trainer1 = Trainer("Ravi", "Fitness Trainer", "Cardio Training")
yoga1 = YogaInstructor("Sita", "Yoga Instructor", "Hatha Yoga")
multi1 = MultiTrainer("Raj", "Multi Trainer", "Weight Training", "Power Yoga")


emp1.display()
trainer1.display()
yoga1.display()
multi1.display()
