import pickle
operation =(str(input("Please specify operation: ")))
todolist = pickle.load(open("test", "rb"))
if operation == "a":
    todolist.append(str(input("input your task: ")))
    pickle.dump(todolist, open("test", "wb"))
if operation == "v":
    todolist = pickle.load(open("test", "rb"))
    print(todolist)
    




