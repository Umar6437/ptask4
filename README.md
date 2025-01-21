
# Python Operators

There are Different types of operators used in Python. Some of them are as following: 

1. Arithmetic Operators
2. Comparison Operators
3. Assignment Operators
4. Logical Operators
5. Bitwise Operators
6. Membership Operators
7. Identity Operators


We can use above operators to perform our operations and can perform different task

Most commonly used operators are arithematic operators, comparison operators and logial operators.

## Arithematic Operators

Arithematic Operators are simple operators which are commonly used in Mathematics. These are as following:

* Addition(+), 
* Subtraction(-), 
* Multiplication(*), 
* Power (**)
* Division(/), 
* Floor division{It gives the answer in round off}, 
* Module(%) {It gives the reminder}.

These are some operators which are called Arithematic Operators

## Comparison Operators

Camparison operators are those operators which are used to campare values. These are as following:

* Greater Than (>)
* Less Than (<)
* Equal To (==)
* Greater and Eqaul to (>=)
* Less Than and Equal to (<=)
* Not Eqaul to (!=)

## Assignment operator

Assignment operator is used to assign any value to variable in python.  Equal to(=) is a assignment operator.

## Logical Operators

Logical operator are those operator which are similar to that which are used in truth table. Which are as following:

* AND (If both values are true than returns true)
* OR (If atleast only one value is true than it returns true)
* NOT (It convert True into false and vise verse)

## Bitwise Operators

Bitwise operators are those operators which are used to convert into binary form and then perform the calculation bit by bit. These are as following:

* Bitwise AND(x & y)
* Bitwise OR (x | y)
* Bitwise NOT (~x)
* Bitwise XOR (x ^ y)
* Bitwise right shift (x>>)
* Bitwise left shift (x<<)

## Membership Operators

Mmembership operators are those operators which are used to check that the value is present in the list or not. The membership operator is as following:

* in (return true value found in the sequence)
* not in (return true value if not found in the sequence)

## Identity Operators
Identity Operators are those operators which are used to check identicalness of the two variable. The Identity operators are as following:

* is (return true if oprands are identical)
* is not (return true when oprands are not identical)

# Ternary Operators

Ternary Operators are those operators we can also called it conditional operation as it used condition to calculate. It allows simple conditional calculation in single line which is very useful for developer. It syntax is as following:

[on true] if[Expression] else[on false]

# Division Operators

Division operator is used to divide to values given to it and return its quotient. It divids the number on its left with number on the right of the divide operator and returns it quotient. There are two type of quotient. Which are as following:

1. Simple Integer quotient
2. Decimal quotient

In python we need both types of answers. For this we use two types of division operator:

1. Float Division for decimal answer
2. Integer Division also known as Floor Division Operator used to round off the answer of the quotient

## Float Division Operator

Float Division operator simply use the synatax (/) which returns the value in float/decimal number

    a = 10
    b = 4
    c = a/b

It gives the answer of 2.5 

## Floor Division Operator

Floor Division operator use double slash (//) which returns the answer in round off form.

    a = 20
    b = 3
    c = a//b

It returns the value of 6. In real if we divid the above number we get 6.6666... but it skips the .6666... and returns only 6.

# Operator Overloading In Python

Like in other programming languages, Operator overloading arises in Python and can be used for different purposes. We use operators in term of numbers. But in Python we can use these operator for strings like joining them or subtracting or multiplying, etc

But here we only discuss simplest operator overloading which is addition. Sometimes like in algebra we have two different variables which we want to be seperatly add divid or multiply like in case of vectors and complex numbers. So we use operator overloading which seperately in perfrom operations.

    class Complex:
        def __init__(self, x, y):
            self.x = x 
            self.y = y
        def __add__(self , z):
            return Complex(self.x + z.x, self.y + z.y )
    C1 = Complex(3, 5)
    C2 = Complex(4, 7)
    C3 = C1 + C3
    print(C3)

This gives the answer of (7, 12). This is operator overloading.

# Any and All in Python

Any and All are used to check the values that these are either true or false in the list. Any as name indicates that it returns true if any of the value is true whereas the All returns only true when all the values of list is true otherwise it returns false.

# Operator Function in Python | Set 01

There are many function in the __operator module__ which helps us easily use these function for our calculation. These are as following:

* add(a,b): It adds both numbers.
Function: a + b
* sub(a,b): It subtract second number from first number.
Function: a - b
* mul(a,b): It multiply both numbers.
Function: a * b
* truediv(a,b): It divide the both numbers.
Function: a / b 
* floordiv(a,b): It also divide the both numbers but return the answer in round off form.
Function: a // b
* pow(a,b): It gives the answer of b power of a.
Function: a ** b 
* mod(a,b): It gives the reminder when fisrt number is divided by second number.
Function: a % b
* lt(a,b): It checks whether a is less then b or not. It returns true when a is less then b.
Function: a < b 
* le(a,b): It checks whether a is less than or equal to b or not. It returns true when a is less than or equal to b.
Function: a <= b 
* eq(a,b): It checks whether a is equal to b or not. It returns true when a is equal to b.
Function: a == b
* gt(a,b): It checks whether a is greater than b or not. It returns true when a is greater than b.
Function: a > b
* ge(a,b): It checks whether a is greater or and equal to b or not. It returns true when a is greater then or equal to b.
Function: a >= b
* ne(a,b): It checks whether a is not equal to b or not. It returns true when a is not equal to b.
Function: a != b

_In above functions, we can use any other variable instead of a and b._ 

__Set 1 covers arithematic and comparison operators only.__

# Operator Functions in Python | Set 2

Set 2 also container some functions which are as following:

* setitem(): It is used to set a number in the list/object at the given position. We can set multiple values in the list by using slice instead of postion which helps us to set more then one values at the same time
_For single item_

Function: setitem(object, position,  new value)

_For multiple values_

Function: setitem(object, slice(a, b), [new values])

* delitem(); It is used to value in the list/object at given position. Also we can delete a range of number from the list by using slice which take a range of numbers
_For single item_

Function: delitem(object, position)

_For multiple item_
Function: delitem(object, slice(a,b))

* getitem(): It used to get the item in the list/object in the given position. For multiple range of items we use slice()

_For single item_

Function: getitem(object, position)

_For multiple item_

Function: getitem(object, slice(a,b))

* concat(): It is used to add/concatenate two strings. Which means that to join to strings and made a new string.

Function: concat(object1, object2)

* contains(): It is used to check whether object2 contains in object1. In simple way we can say that we can check that object2 is subset of object1. It will return true if yes otherwise gives false.

* and_(): It is used to get the __AND__ answer two aurgument in bitwise form.
Function: and_(a,b)
* or_(): It is used to get the __OR__ answer of two aurgument in bitwise form.
Function: or_(a,b)
* xor_(): It is used to get __XOR__ answer of two aurgument in bitwise form.
Function: xor_(a,b)
* invert(): It is used to __invert__ the aurgument in bitwise form.
Function: invert_(a)

# Difference between is operator and == operator
__is__ operator and __==__ operator both are different operators which is as following:

* __is__ operator only checks that the variable exist in the same memory only. It means if we declared that the object are equal then it confirms that they are equal.Otherwise for both are different objects which are equal but are not declared by user then it will show that they are not identical as they does not rely on the same memory box.

* __==__ operator checks the value of both objects if that operator found any uneqaulity in objects than it will declare unequal otherwise it will declare equal.

# Membership Operator and Identity Operator 

## Membership Operator
It is operator which is used to check that the given value is part of the object or not. It consist of two operators which are as following:

1. __in__ operator which returns true when value is present in that object.
2. __not in__ operator which returns true when value is __not__ present in object.

## Identity Operator
It is operator which is used to check that the given value is equal point to point to the main object. It also consist of two operators.

1. __is__ operator which returns true when both are equal.
2. __not is__ operator which returns true when both are __not__ equal.

# Python Data
Python data can be represent in four forms which are as following:
 
1. String
2. List 
3. Tuple
4. Iteration

## String 
String is a datatype which contains special characters which are stored in variable and can be print by using its variable. It contains letters, special characters and numbers.

    str = "My name is Umar Farooq.  My Email address is: Umar1234@gmail.com."
    print(a)

In above code, the value inside a is string.

## List
As the name indicate that is contains set/list of strings which can be stored. It is similar to array in C++ which store different values in one variable. Same is the case with that.

    MyList = ["Lahore", "Multan", "Zob", "Quetta", "Qila Abduallah"]
    print(MyList)

We can store string, integar, float numbers, and true false set. Also we can modify it when we want to. And also we add duplicate value.

## Tuple
Tuple is also list but it is different from list. We can modify the list anytime but in case of tuple we cannot change it value once we entered in it. Also in list we use square brackets[] but in tuple we use round brackets() for assigning values.

    MyTuple = ("Apple", "Banana", "Orange")
    print(MyTuple)

For only one value simply put a comma after the value.

## Iteration
It is the repeated execution of a set of statement which helps to do a task again and again perfectly. Which helps in many ways in our programing for e.g in print the value from 1 to 100 we donot need to type each number one by one we one give one iteration command by which it print the value 1 from 100. The code for that is given below

    for i in range(0, 100):
        print(i)

