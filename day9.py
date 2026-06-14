
file = open("sabu.txt", "w")

file.write("Hello Python")

file.close()

file = open("sabu.txt","r")
file.read()
file.close()

file = open ("sabu.txt","a")
file.write("\nwelcome to python")
file.close() 

file = open ("sabu.txt","r")
for line in file:
    print(line)
    file.close()

name = input("Enter Name: ")
age = input("Enter Age: ")

file = open("sabu.txt", "w")
file.write(f"\n{name} - {age}")

print("Data Saved")


f = open ("myfile.txt","w")
f.write("sadbuddhi bhaigade")    
f.close()    


f = open("myfile.txt","a")
f.write("\nkalyan")
f.close()

marks = open("marks.txt","w")
marks.write("\n80")
marks.write("\n90")
marks.write("\n100")
marks.write("\n400")
marks.write("\n101")
marks.close()

