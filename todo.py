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
            todolist.append("[ ]" + str(input("input your task: ")))
            pickle.dump(todolist, open("test", "wb"))
        if operation == "n":
            marklist.append(False)
            pickle.dump(marklist, open("mark.p", "wb"))
            todolist.append(str(input("input your task: ")))
            pickle.dump(todolist, open("test", "wb"))
        elif operation == "v":
            todolist = pickle.load(open("test", "rb"))
            for i in range(len(todolist)):
                print('%d %s' % (i , todolist[i]))
                i+1
        elif operation == "r":
            while len(todolist) > 0:
                todolist = pickle.load(open("test", "rb"))
                remid = int(input("which task do you want to remove? "))
                todolist.remove(todolist[remid])
                marklist.remove(marklist[remid])
                pickle.dump(todolist, open("test", "wb"))
                pickle.dump(marklist, open("mark.p", "wb"))
            else:
                pass
        elif operation == "m":
            todolist = pickle.load(open("test", "rb"))
            marklist = pickle.load(open("mark.p", "rb"))
            mark = (int(input("ID of task you want to mark as done: ")))
            marklist[mark] = True
            pickle.dump(marklist, open("mark.p", "wb"))
            pickle.dump(todolist, open("test", "wb"))
        elif operation == "a":
            archin = (input("do you want to 'Archive' marked tasks? y/n : "))
            if archin == "y":
                marklist = pickle.load(open("mark.p", "rb"))
                todolist = pickle.load(open("test", "rb"))
                try:
                    for i in range(len(marklist)):
                        mark_in = (marklist.index(True))
                        mark_in = int(mark_in)
                        todolist.remove(todolist[mark_in])
                        marklist.remove(marklist[mark_in])
                        pickle.dump(marklist, open("mark.p", "wb"))
                        pickle.dump(todolist, open("test", "wb"))
                except ValueError:
                    pass
            else:
                pass
            




                

        
        elif operation == "x":
            break
        
        elif operation == "debug":
            todolist = pickle.load(open("test", "rb"))
            marklist = pickle.load(open("mark.p", "rb"))
            print(todolist)
            print(marklist)
            try:
                print(marklist.index(True))
                mark_ind=(marklist.index(True))
                print(mark_ind)
                mark_ind = 0
            except ValueError:
                pass 

           
            