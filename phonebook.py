phonebook = {}
def contacts():
    try:
        while True:
            print ("\n1.Add Contact\n2.View Contact\n3.Delete Contact\n4.Exit")
            choice = input ("Enter your choice").strip()
            if choice == "1":
                name = input ("Enter your name").strip()
                if not name :
                    raise ValueError ("Name cannot be empty")
                number = input("Enter your number").strip()
                if not number.isdigit ():
                    raise ValueError ("Phone number must be numeric")
                phonebook[name] = number
                print ("Added successfully")
            elif choice == "2":
                name = input("Enter name to search").strip()
                if not name:
                    raise ValueError("Name cannot be empty")
                print (f"{name} {phonebook.get(name,"Contact not found")}")
            elif choice =="3":
                name = input("Enter a name to delete").strip()
                if not name:
                    raise ValueError("Name cannot be empty")
                if name in phonebook:
                    del phonebook[name]
                    print ("Contact deleted successfully")
                else:
                    print ("Contact not found")

            elif choice == "4":
                print ("exiting phonebook")
                break
            else:
                print ("Invalid Choice")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occured : {e}")


contacts()
