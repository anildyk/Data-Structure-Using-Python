
#Swap two variables using a temporary variable.
def swapByTemp(a,b):
    temp = a
    a=b
    b=temp
    return a,b
#Swap without temporary variable.
# 1. Using Addition and Subtraction
def swapByAddSub(a,b):
    a = a+b
    b = a-b    # b = (a+b)-b = a
    a = a-b    # a = (a+b)-a = b
    return a,b
# 2. Using Division and Multiplication
def swapByMultiDiv(a,b):
    a = a*b
    b = a/b   # b = (a*b)/b = a
    a = a/b   # a = (a*b)/b = (a*b)/a = b
    return a,b
# 3. Using Bitwise Operator XOR (Only for integers)
def swapByXOR(a,b):
    a = a^b
    b = a^b
    a = a^b
    return a,b
# 4. Using Standard Pythonic way

def swapStandard(a,b):
    return b,a

a=10
b=32
#Test all the functions on a & b
print swapStandard(a,b)
print swapByTemp(a,b)
print swapByAddSub(a,b)
print swapByMultiDiv(a,b)
print swapByXOR(a,b)
