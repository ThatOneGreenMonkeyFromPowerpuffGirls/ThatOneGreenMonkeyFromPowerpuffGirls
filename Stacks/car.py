cars = []
maxlen = 6
top = len(cars)

def isEmpty():
    top = len(cars)
    if top == 0:
        return True
    else:
        return False
def isFull():
    top = len(cars)
    if top == maxlen:
        return True
    else:
        return False
def push(x):
    top = len(cars)
    full = isFull()
    if full == True:
        print("List full, couldn't push")
    else:
        cars.append(x)
    top = len(cars)
def pop():
    top = len(cars)
    cars.pop(top-1)
    top = len(cars)

#Enters
push("Mondeo")
push("Golf")
print(f"Empty: {isEmpty()}")
push("Fiesta")
push("Punto")
pop()
push("Civic")
push("Porsche")
print(f"Full: {isFull()}") 
pop()
pop()

print(cars)