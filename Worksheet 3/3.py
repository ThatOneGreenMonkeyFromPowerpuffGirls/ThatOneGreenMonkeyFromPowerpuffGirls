list1 = [2,5,15,36,47,56,59,78,156,244,268]
list2 = [18,39,42,43,66,69,100]
list3 = []
count = 0
sorted = False

while sorted == False:
    if len(list3) == len(list1)+len(list2):
        print("bish bash bosh\nsorted")
    sorted = True
    count+=1
    if list1[count]>list2[count]:
        list3.append(list1[count])
    elif list1[count]==list2[count]:
        list3.append(list1[count])
        list3.append(list2[count])
        count+=1
    else:
        list3.append(list2[count])


print(list1)
print(list2)
print(list3)