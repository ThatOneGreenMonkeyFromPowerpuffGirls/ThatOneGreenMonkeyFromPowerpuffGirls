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
        save = current + 2
        current = linkedlist[current][pointer]
    return save

def add(linkedlist):
    add = input("Input: ")
    linkedlist[traverse(linkedlist)][data] = str(add)
    linkedlist[traverse(linkedlist)][pointer] = None
    print("List is finished\n")
    print(linkedlist)
    

add(linkedlist)
#need to fix the adding name part, current error is the added name replacing "Sharon"