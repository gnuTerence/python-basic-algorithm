#Factorial: Giai thừa
def fact(x):
    if x == 1:
        return x
    else:
        return x*fact(x-1)

fact(3) #Return 6
print(fact(4))