'''
queue to add student names to a marking list.
when the teacher has marked they are removed.
max 5.
'''

#queue = ["darren","jmichael","jjohn","jonesy","HaqueS"]
queue = ["","","","",""]

front=0
rear=-1
size=0
name = ""

def isFull():
    #if queue[0] == "":
        #rear = 0 #does this work?
    if queue[-1] != "":
        print("queue is full")
        exit()
    

def enQueue(studentName):
    global size
    global rear
    global front
    isFull()
    rear+=1
    size+=1
    queue[rear] = studentName

def deQueue():
    global size
    global rear
    global front
    size-=1
    queue[front] = ""

def main():
    aorm = input("add name or remove? ")
    if aorm == "add":
        name = input("enter student name to add: ")
        enQueue(name)
    elif aorm == "remove":
        deQueue()
    elif aorm == "-999":
        print(queue)
        return
    else:
        print("invalid input")
        main()
    print(queue)

    main()

main()
#finish it