shopping =[]
while True:
    print("1.Add item")
    print("2.Remove item")
    print("3.View item")
    print("4.Exit")
    choose = int(input("Enter a number :"))
    if choose == 1:
        items = input("Enter a item to Add : ").split(",")
        for item in items:
            item =item.strip()
            shopping.append(item)
            print(item,"ADDED SUCCESSFULLY")
    elif choose == 2:
        items = input("Enter a item to remove : ").split(",")
        for item in items:
            item = item.strip()
            
            if item in shopping:
             shopping.remove(item)
             print(item,"remove succussfully")
            else:
                print(item,"is not found")
    elif choose == 3:
        if len(shopping) == 0  :
            print("shopping bag is empty") 
        else:
            print("\n shopping bag")    
            for item in shopping:
                print("-",item)    
    elif choose == 4:
        print("Thank you for using our service")  
        break
    else:
        print("invalid input ,enter input between 1 to 4") 

             