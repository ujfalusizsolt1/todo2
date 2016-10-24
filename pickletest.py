import pickle
while True:
        operation =(str(input("Please specify operation: ")))
        todolist = pickle.load(open("test", "rb"))
        #marklist = pickle.load(open("mark", "rb"))
        if operation == "a":
            todolist.append(str(input("input your task: ")))
            pickle.dump(todolist, open("test", "wb"))
        elif operation == "v":
            todolist = pickle.load(open("test", "rb"))
            print(todolist)
        elif operation == "r":
            todolist = pickle.load(open("test", "rb"))
            remid = int(input("which task do you want to remove? "))
            todolist.remove(todolist[remid])
            pickle.dump(todolist, open("test", "wb"))
        elif operation == "x":
            break