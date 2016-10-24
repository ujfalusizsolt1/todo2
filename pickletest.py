import pickle
while True:
        operation = (str(input("Please specify operation: ")))
        try:
            todolist = pickle.load(open("test", "rb"))
            marklist = pickle.load(open("mark.p", "rb"))
        except EOFError:
            marklist=[]
            todolist=[]
            marklist.append(False)
            pickle.dump(marklist, open("mark.p", "wb"))
            todolist.append(str(input("input your task: ")))
            pickle.dump(todolist, open("test", "wb"))
        if operation == "a":
            marklist.append(False)
            pickle.dump(marklist, open("mark.p", "wb"))
            todolist.append(str(input("input your task: ")))
            pickle.dump(todolist, open("test", "wb"))
        elif operation == "v":
            todolist = pickle.load(open("test", "rb"))
            print(todolist)
        elif operation == "r":
            todolist = pickle.load(open("test", "rb"))
            remid = int(input("which task do you want to remove? "))
            todolist.remove(todolist[remid])
            marklist.remove(marklist[remid])
            pickle.dump(todolist, open("test", "wb"))
            pickle.dump(marklist, open("mark.p", "wb"))
        elif operation == "m":
            todolist = pickle.load(open("test", "rb"))
            marklist = pickle.load(open("mark.p", "rb"))
            mark = (int(input("ID of task you want to mark as done: ")))
            print = (todolist[mark], marklist[mark])
        
        elif operation == "x":
            break