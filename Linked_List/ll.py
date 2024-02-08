data = 0       #makes it conceptually easier to see
pointer = 1
head = 0

print(f"Head is {str(head)}")

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
    check1 = False
    check2 = False
    check3 = False
    print(linkedlist)
    delete = input("Delete: ")
    for i in range(0,len(linkedlist)):
        if linkedlist[i][data] == delete:
            nextspointer = linkedlist[i][pointer]
            ii = i
            check1 = True
    if check1 == True:
        for i in range(0,len(linkedlist)):
            if linkedlist[i][pointer] == ii:
                check2 = True
                check3 = True
                previ = int(i)
        if check3 == True:
            linkedlist[previ][pointer] = nextspointer
            linkedlist[ii][data] = None
            linkedlist[ii][pointer] = None
        else:
            linkedlist[ii][data] = None
            linkedlist[ii][pointer] = None
    print(linkedlist)
    #check if this works!

#add(linkedlist)
delete(linkedlist)
