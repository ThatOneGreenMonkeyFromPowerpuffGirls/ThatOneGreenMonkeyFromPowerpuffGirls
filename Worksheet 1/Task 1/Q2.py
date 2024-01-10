name = ["beckey","1","haquey","2","braceosaurus","3","bob","4","katie","5","rishithesplendid","6"]
search = input("Input name: ")
x = 0
for i in range(0,len(name),2):
    if name[i] == search:
        x = name[i+1]
if x != 0:
    print("Student record number is " + str(x))
else:
    print("term was not found")