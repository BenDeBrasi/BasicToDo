def place_list_in_file(master_list):
    for items in master_list:
        pickle.dump(items,file_handle)

import pickle
import os.path

class Node:
    
    def __init__(self, data, nextn):
        self.data = data
        self.nextn = nextn


class Linked_list: 
    def __init__(self, data):
       self.head = Node(data,None) 

    def add(self, data):
        node = Node(data,None)

        if self.head == None:
            self.head = Node(data, None)
            return self.head
        
        else:
            tmp = self.head
            while tmp.nextn!= None:
                tmp = tmp.nextn
            tmp.nextn = node
            return self.head

    def delete(self,data):
      
        tmp = self.head
        prev = self.head
        
        while tmp != None:
           
            if tmp.data == value:
                prev.nextn = tmp.next
                return self.head
            
            prev = tmp
            tmp = tmp.nextn

    def Print_list(linkedlist):
        tmp = linkedlist.head
        x = 0
        while tmp !=None:
            print(tmp.data)
            if x == 0:
                print("----------------")
                x = 1
            tmp = tmp.nextn

master_list =[]
if os.path.exists('todo.txt'): 
    file_handle = open('todo.txt', 'rb+')

    if os.path.getsize('todo.txt') == 0:
        pass
    else:
        while 1:
            try:
                master_list.append(pickle.load(file_handle))
            except EOFError:
                break

else:
    open('todo.txt', 'x')


file_handle = open('todo.txt', 'wb+')

"Add while loop to loop program. Find a way to auto-indent the rest"

print("Commands:")
print("---------")
print("'at'- Add task")
print("'al'- Add list")
print("'dl'- Delete list")
print("'dt'- Delete task")
print("'rl'- Read list")
print("'ml'- Read master list")
print("'s'- shutdown program")
print()

mode = input("What do you want to do?")

if mode == 's':
    print("Program shutting down")
    place_list_in_file(master_list)
    file_handle.close()
    exit()

'Error check for user chosen task'
if mode != 'at' and mode != 'al' and mode != 'dl' and mode != 'dt' and mode != 'rl' and mode != 'ml':
    print("Not a valid command")
    place_list_in_file(master_list)
    file_handle.close()
    exit()

if mode == 'al':
    list_name = input("Enter name of list you want to add: ")
    x = 0
    while x < len(master_list):
        if master_list[x].head.data == list_name:
            print("List already exists!")
            place_list_in_file(master_list)
            file_handle.close()
            exit()
        x+=1

    x = 0
    task_list = Linked_list(list_name)
    while x < len(master_list):
        if master_list == None:
            master_list[x]= task_list
            place_list_in_file(master_list)
            file_handle.close()
            exit()
        x += 1
            
    master_list.append(task_list)
    place_list_in_file(master_list)
    file_handle.close()
    exit()

if mode == 'rl':
    
    list_name = input("Which list do you want to read?")
    x = 0
    
    while x < len(master_list):
        if master_list[x].head.data == list_name:
           master_list[x].Print_list()
           place_list_in_file(master_list)
           file_handle.close()
           exit()
        x += 1

    print("List doesn't exist!")
    place_list_in_file(master_list)
    file_handle.close()
    exit()

if mode == 'dl': 
    x = 0
    list_name = input("Which list do you want to delete?")
    for items in master_list:
        if master_list[x].data == list_name:
            delete(master_list[x]) 
            place_list_in_file(master_list)
            file_handle.close()
            exit()
        x += 1
        
    print("List doesn't exist!")
    place_list_in_file(master_list)
    file_handle.close()
    exit()

if mode== 'at':
   
    list_name = input("Enter the list name: ")
    x = 0
    while x < len(master_list):
        
        if master_list[x].head.data == list_name:
            print("Entered match of data in at") 
            task_name = input("Enter the name of the task:")
            
            if task_name == list_name:
                print("List doesn't exist!")
                place_list_in_file(master_list)
                file_handle.close()
                exit()
            
            tmp = master_list[x].head

            while tmp != None:
                if tmp.data == task_name:
                    print("Task already exists!")
                    place_list_in_file(master_list)
                    file_handle.close()
                    exit()
                tmp = tmp.nextn
          
            master_list[x].add(task_name)
            place_list_in_file(master_list)
            file_handle.close()
            print("Task added!")
            exit()
        x +=1

    print("List doesn't exist!")
    place_list_in_file(master_list)
    file_handle.close()
    exit()

if mode == 'dt':
    
    list_name = input("Enter the list name: ")
    x = 0
    
    while x < len(master_list):
        
        if master_list[x].head.data == list_name:
            print("Entered match of data in at") 
            task_name = input("Enter the name of the task:")
            tmp = master_list[x].head
            prev = master_list[x].head

            while tmp != None:
                if tmp.data == task_name:
                    print("Task deleted!")
                    prev.nextn = tmp.nextn
                    place_list_in_file(master_list)
                    file_handle.close()
                    exit()
                prev = tmp
                tmp = tmp.nextn
          
            master_list[x].add(task_name)
            place_list_in_file(master_list)
            file_handle.close()
            print("Task doesn't exist!")
            exit()
        x +=1

    print("List doesn't exist!")
    place_list_in_file(master_list)
    file_handle.close()
    exit()

if mode == 'ml':
    for lists in master_list:
        lists.Print_list()
        print()
        
    place_list_in_file(master_list)
    file_handle.close()
    exit()
