import pickle
operation =(str(input("Please specify operation: ")))
todolist = pickle.load(open("test", "rb"))
if operation == "a":
    todolist.append(str(input("input your task: ")))
    pickle.dump(todolist, open("test", "wb"))
if operation == "v":
    todolist = pickle.load(open("test", "rb"))
    print(todolist)
if operation == "r":
    todolist = pickle.load(open("test", "rb"))
    remid = int(input("which task do you want to remove? "))
    todolist.remove(todolist[remid])
    pickle.dump(todolist, open("test", "wb"))

    




