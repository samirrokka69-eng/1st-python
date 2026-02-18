Name = input("Enter your name: ")
print("Welcome",Name,"!")

Task = []

while True:
    print("\n 1. Add Task")
    print("2. View Task")
    print("3. Mark Task as done")
    print("4. Remove Task")
    print("5. Exit")

    choice = int(input("Choose option: "))
    if(choice == 1):
        task = input("Add your task: ")
        for task in Task:
             print("Task already exists !")
        else:
         Task.append(task)

    elif(choice==2):
        if(len(Task)==0):
            print("Empty Task")
        
        else:
            print("\n your task:")
            for i in range(len(Task)):
                print(f"{i+1}. {Task[i]}")

    elif(choice == 3):
        if(len(Task)==0):
            print("Empty Task")

        else:
            print("\n your task:")
            for i in range(len(Task)):
                print(f"{i+1}. {Task[i]}")
            num = int(input("Enter which number task is done: "))
            if(1<=num<=len(Task)):
                    Task[num-1]=Task[num-1]+" (Done)"
                    print("Task Marked as Complete\n")

            else:
                    print("Invalid option")

    elif(choice == 4):
        if(len(Task)==0):
            print("Empty Task")

        else:
            print("\n your task:")
            for i in range(len(Task)):
                print(f"{i+1}. {Task[i]}")
            num = int(input("Enter which number task you want to remove: "))
            if(1<=num<=len(Task)):
                    removed = Task.pop(num - 1)
                    print(f"{removed} removed sucessfully")

            else:
                    print("Invalid option")

    elif(choice==5):
        print("Good bye ",Name)
        break

    else:
        print("Invalid option. Please choose 1-5.")
                  
                

