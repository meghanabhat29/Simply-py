x=input("Enter a string : ")
upper=0
lower=0
for i in x:
    if i.isupper():
        upper=upper+1
    elif i.islower():
        lower=lower+1
    else:
        continue
print("The number of upper case letters : %1d" %(upper))
print("The number of lower case letters : %1d" %(lower))
