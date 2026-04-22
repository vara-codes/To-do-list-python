Tasks=[]

while True:
  print("\n -----TO-DO lIST-----")
  print("1.add task")
  print("2.show task")
  print("3.delete task")
  print("4.exit task")
  
  work = input("Enter ur choice :")
  
  if (work == "1"):
    task = input("Enter your tasks :")
    Tasks.append(task)
    print("Your task is added succesfully:)")

  elif(work == "2"):
    if not Tasks:
      print("no task added yet")
    else:
      for i in range(len(Tasks)):
        print(i+1, Tasks[i])

  elif(work == "3"):
    if not Tasks:
      print("no task added yet")
    else:
      for i in range(len(Tasks)):
        print(i+1, Tasks[i])

      num= int(input("Enter the index no. to delete : "))
      index=num-1

      if ((index >= 0) and (index < len(Tasks))):
        Tasks.pop(index)
        print("Tasks is deleted !")
      else:
        print("enter the valid number")

  elif(work == "4"):
    print("Good bye :)")
    break
    



    
