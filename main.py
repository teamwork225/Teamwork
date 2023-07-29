#Alinura Sultanova
#Gulat Kaipova
#07/29/2023
#print the list of choices
print("Please Choose your option from the list below:")
print("1.  CCS225")
print("2.  CSS100")
print("3.  CSS220")
print("4.  CSS200")
print("5.  CSS205")
print("0.  Exit")

choice=int(input("\nYour Choice: ")) #parse the input value to integer as input gives the value as string
#use if else and check what the user chose and display appropriate message
if(choice==1):
    print("You Selected Option: 1")
    print("Let's Start Learning CSS225")
elif(choice==2):
    print("You Selected Option: 2")
    print("Let's Start Learning CSS100")
elif(choice==3):
    print("You Selected Option: 3")
    print("Let's start learning CSS220")
elif(choice==4):
    print("You Selected Option: 4")
    print("Let's start learning CSS200")
elif(choice==5):
    print("You Selected Option: 5")
    print("Let's start learning CSS205")
elif(choice==0):
    exit()
