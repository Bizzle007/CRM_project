#logic Layer
id_list=[]
name_list=[]
age_list=[]
mob_list=[]

def addCustomer(id,name,age,mob):
    id_list.append(id)
    name_list.append(name)
    age_list.append(age)
    mob_list.append(mob)

def searchCustomer(id):
    index=id_list.index(id)
    return index

def deleteCustomer(id):
    i=id_list.index(id)
    id_list.pop(i)
    name_list.pop(i)
    age_list.pop(i)
    mob_list.pop(i)

def modifyCustomer(id, name , age , mob):
    i=id_list.index(id)
    name_list[i]=name
    age_list[i]=age
    mob_list[i]=mob

#presentation layer 
def showCustomer(i):
    print("Cust ID:", id_list[i] , "Cust Name:" , name_list[i], "Cust Age:" , age_list , "Cust mob:", mob_list)
def getID():
    while(1):
        id=input("Enter Cust Id:")
        if(id not in id_list):
            return
        else:
            print("Warning! Duplicate ID")
        




print("Welcome to Aryan's Mangement system")
while(1):
    choice=input("Enter Choice:1 ,for Add Cust:2  , For Search Cust:3 , For Display Cust:4 , Exit: 5 ")
    if(choice=="1"):
        id=input("Enter Cust ID:")
        name = input("Enter Cust Name:")
        age= input("Enter Cust age:")
        mob= input("Enter Cust Mobile:")
        addCustomer (id , name , age , mob)
        print("Customer added Successfully")
    elif(choice=="2"):
        id=input("Enter Cust Id to search:")
        i=searchCustomer(id)
        showCustomer(id)
    elif(choice=="3"):
        id=input("Enter Cust Id to delete:")
        deleteCustomer(id)
        print("Customer Deleted succesfully")
    elif(choice=="4"):
        id=input("Enter Cust to modify:")
        name = input("Enter Cust to udate name:")
        age= input("Enter Cust to update age:")
        mob= input("Enter Cust to update mob:")
        modifyCustomer(id,name,age,mob)
        print("Customer Modified Successfully")
    elif(choice=="5"):
        for i in range(len(id_list)):
            showCustomer(i)
    elif(choice=="6"):
        print("Print Thank you for using Aryan CRM")
        break
    else:
        print("Incorrect Choice")






