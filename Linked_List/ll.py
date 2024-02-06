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
        print(linkedlist[current][data])
        current = linkedlist[current][pointer]
    print("List is finished")
    return

traverse(linkedlist)