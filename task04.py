# Python Operators
# Arithmatic operators
print("Arithematic Operation")
x = 34
y = 45
print("x = ", x)
print("y = ", y)
print("Sum = ", x + y)
print("Difference = ", x - y)
print("Multiplication = ", x * y)
print("2 power of 5 = ", 5 ** 2)
print("Division = ", x / y)
print("Floor Division = ", x // y)
print("Modulus = ", x % y)

# Comparision Operator
print("Comparision Operations")
a = 23
b = 21
print("a = ", a)
print("b = ", b)
print("Greater then", a > b)
print("Less than", a < b)
print("Equal to ", a == b)
print("Greater then or equal to", a >= b)
print("Less than or Equal to ", a <= b)
print("Not Equal to", a != b)

# Assignment Operator
c = 65
d = c
print("c = ", c)
print("d = ", d)

# Logical Operators
print("Logical Operation")
e = True
f = False
g = True

if e and g:
    print("True, Both e and g are true, AND condition")
if e or f:
    print("Minimum,One of these should be true for True, OR Condition")
if not e:
    print("e is true, NOt Operation")
else:
    print("e is false, Not Operation")
    
# Bitwise Operation
print("Bitwise Operation")
h = 10
i = 4
print("h = ",h)
print("i = ", i)
print("AND h & i = ", h & i)
print("OR h | i = ", h | i)
print("NOT ~h = ", ~h)
print("XOR h ^ i = ", h ^ i)
print("Right Shift h>> = ", h >> 1)
print("Left Shift <<h = ", h << 1)

# Membership Operator
print("Membership Operation ")
j = [23, 45, 54, 95, 64, 25]
print("j = ",j)
print("95 in j ", 95 in j)
print("66 not in j ", 66 not in j )

# Identity Operator
k = ["Karachi", "Lahore", "Peshawar", "Swat"]
l = ["Karachi", "Lahore", "Peshawar", "Swat"]
m = k
print("k = ", k)
print("l = ", l)
print("m = ", m)
print("k is m ")
print(k is m)
print("k is not l")
print(k is not l)
print("It gives false because both k and l does not belong to same memory.")
print("k == l ", k == l)

# Ternery Operators
n = 8

res = "Even" if n%2==0 else "Odd"
print(res)

# Operator Overloading 
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return self.a + other.a, self.b + other.b
C1 = Complex(3, 6)
C2 = Complex(6, 8)
C3 = C1 + C2
print(C3)

# Operator Set
import operator
o = 23
p = 34
print("o = ", o)
print("p = ", p )
print("This is Set 01")
print(operator.add(o, p))
print(operator.sub(o, p))
print(operator.mul(o,p))
print(operator.pow(5,2))
print(operator.truediv(o,p))
print(operator.floordiv(o,p))
print(operator.mod(o,p))
print(operator.lt(o,p))
print(operator.lt(o,p))
print(operator.eq(o ,p))
print(operator.gt(o,p))
print(operator.ge(o,p))
print(operator.ne(o,p))

print("This is set 02")
q = [1, 5, 8, 2, 9]
print("q = ", q)
operator.setitem(q, 2, 7)
print(q)
operator.setitem(q, slice(0,3),[5,8,9,1])
print(q)
r = [5, 8, 0, 7, 6]
print("r = ", r)
operator.delitem(r, 2)
print(r)
operator.delitem(r, slice(0,1))
print(r)

s = [0,1,2,3,4,5,6]
t = [9,8,7]
print("s = ",s )
print("t = ", t)
u = operator.concat(s,t)
print(u)

v = 0
w = 1
print("v = ", v)
print("w = ", w)
print(operator.and_(v, w))
print(operator.or_(v,w))
print(operator.xor(v,w))
print(operator.invert(v))
print(operator.invert(w))

# Difference between == and is statement

x = [8,4,6,7,5]
y = [8,4,6,7,5]
z = x
print("x = ", x)
print("y = ", y)
print("z = ", z)
print("By using is statement to check x is equal to y ")

if x is y:
    print("x is eqaul to y")
else:
    print("x is not equal to y")

if x is z:
    print("x is equal to z")
else:
    print("x is not equal to z")

print("By using == to check x is equal to y ")

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")

# String
A = "My email is Umar34@gmail.com"
print(A)

# List
myList = [5,9,7,5,2,8]
print(myList)

#Tuple
myTuple = ("Lahore", "Karachi", "Multan")
print(myTuple)

# Iteration

for i in myList:
    print(i)
