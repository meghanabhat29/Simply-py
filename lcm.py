def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)
def lcm(a,b):
    return a*b/(gcd(a,b))
print("Enter two numbers,say a and b : ")
a=int(input("a = "))
b=int(input("b = "))
print("The LCM of %1d and %1d is %1d" %(a,b,lcm(a,b)))
