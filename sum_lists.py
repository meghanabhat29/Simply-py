from functools import reduce
list1=list(map(int,input("Enter a list of numbers : ").split()))
list2=[i*3 for i in list1]

print("List 1 : ",list1)
print("List 2 : ",list2)

sum1=reduce(lambda x,y:x+y,list1)
sum2=reduce(lambda x,y:x+y,list2)
print(sum1)
print(sum2)
