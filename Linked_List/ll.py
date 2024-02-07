data = 0       #makes it conceptually easier to see
pointer = 1
head = 0

linkedlist = [
    ["Bob", 3],
    ["Sarah", 2],
    ["Sharon", None],
    ["Roberto", 1],
    [None, None],
    [None, None]
]

def traverse(linkedlist):
    if linkedlist[head][data] == None:
        print("List is empty")
        return
    current = head
    while current != None:
        current = linkedlist[current][pointer]

def findprev(linkedlist):
    for i in range(0,len(linkedlist)):
        if linkedlist[i][data] != None and linkedlist[i][pointer] == None:
            save2 = int(i)
            return save2

def freespace(linkedlist):
    for i in range(0,len(linkedlist)):
        if linkedlist[i][data] == None:
            save = int(i)
            return save


def add(linkedlist):
    add = input("Input: ")
    freespot = freespace(linkedlist)
    prevspot = findprev(linkedlist)
    linkedlist[prevspot][pointer] = freespot
    linkedlist[freespot][data] = add
    linkedlist[freespot][pointer] = None
    #print("List is finished\n")
    print(linkedlist)

def delete(linkedlist):
    print(linkedlist)
    delete = input("Delete: ")
    for i in range(0,len(linkedlist)):
        if linkedlist[i][data] == delete:
            save3 = linkedlist[i][pointer]
    for i in range(0,len(linkedlist)):
        if linkedlist[linkedlist[i][pointer]][pointer] == save3
            save4 = i
    linkedlist[save4][pointer] = save3
    linkedlist[save3][data] = None
    linkedlist[save3][pointer] = None
    print(linkedlist)
    #check if this works!

add(linkedlist)
delete(linkedlist)
#need to fix the adding name part, current error is the added name replacing "Sharon"