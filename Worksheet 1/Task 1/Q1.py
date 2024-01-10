nums=[1,2,3,4,5,6]
total=0
for num in nums:
    x=nums[-num]
    print(x)
    total+=x
average = total/len(nums)
print("Total: "+str(total))
print("Average: "+str(average))