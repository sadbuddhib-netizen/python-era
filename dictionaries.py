'''student = {"name": "sabu",
           "age": "22",
            "school": "n.r.c school"}
print(student)
print(student["name"])
student["education"] = "bsc"
print(student)
student["age"] =23
print(student)
student.pop("age")
print(student)
print(student.keys())
print(student.values())

customer = {"name": "om","payment mode":"online","address":"ambivali"}
for key,values in customer.items():
    print(key,":",values)'''



customer = {
    "name": "sanika","age":20,"city":"pune","degree":"IT"
}

customer["skill"] = "python" # type: ignore
customer ["age"] = 23
print(customer)
print(customer.keys())
print(customer.values())

marks = {"amit": 50, "sabu": 90,"om": 100}
print(max(marks.values()))
average = (sum(marks.values())/len(marks))
print(average)


