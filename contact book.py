
contact = {}
while True:
   print("1.add number")
   print("2.update number")
   print("3.view number")
   print("4.delete number")

   choose = int(input("Enter a number :"))
   if choose == 1:
       name = input("Enter a Name : " )
       phone_number = int(input("Enter a Number : "))
       print(f"name :{name}")
       print(f"phone number : {phone_number}")
       contact[name] = phone_number
       print("added successfully:")
   elif choose == 2:
       if name in contact:
        new_number = input("enter a new number")
        name = input("enter a name : ")
        print("new number added successfully") 
       else:
          print("Not found!")

   elif choose == 3:
       if  len(contact)== 0:
        print("contact list empty")
       else:
        print("\f All Contact")
        for name,phone_number in contact.items():
         print("name : ",name)
         print("phone_number : ",phone_number)
         print("-------------")
   elif choose == 4:
     
       delete_number = input("enter a number to delete")
       if name in contact:
        del contact[name]
        print("number delete successfully")
       else:
          print("number is not found")
   
   else:
        print("Invalid Input! Please enter a number between 1 and 5.")   
     
         
         
        

         


       
          
