class student:
    name ="sabu"
    age = "23"
s1 = student()
print(s1)
print(s1.name)
print(s1.age)

class student:
  def __init__(self,name ,age): 
    self.name= "sabu"
    self.age = 24
s1 = student("sabu",24)
print(s1.name)
print(s1.age)

class car:
    name ="om"
    age= 23
c1 = car()
print(c1.name)
print(c1.age)

class car:
    def __init__(self,surname,degree):
        self.surname ="bhaigade"
        self.degree ="bsc.it"
c1=car("bhiagde","bsc.it")    
print(c1.surname)
print(c1.degree)

class employee:
    def __init__(self,name,department,salary):
        self.name ="om"
        self.department ="science"
        self.salary =7000
E1= employee("om","science",7000)        
print(E1.name)
print(E1.department)
print(E1.salary)

        