import math
#first task
class stringtoUpper: 
    def __init__(aboba):
        aboba.s=0 
    def inputStrimg(aboba):
        aboba.s = input("Enter a string: ")
    def printString(aboba):
        print(aboba.s.upper())
s = stringtoUpper()
s.inputStrimg()
s.printString()  
#second task
class Shape:
    def area(self):
        self.a=0
class Square(Shape):
    def __init__(self, length):
        self.length=length
    def area(self):
        return self.length*self.length
dlina=int(input("Enter the length: "))
sqr=Square(dlina)
print(f"Area={sqr.area()}")


#third task
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
dlina2=int(input("Enter the length: "))
shirina=int(input("Enter the width: "))
rect=Rectangle(dlina2, shirina)
print(f"Area of Rectangle={rect.area()}")
#task 4th
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def dist(self, nextpoint):
        return math.sqrt((self.x - nextpoint.x) ** 2 + (self.y - nextpoint.y) ** 2)   #расстояние между двумя точками V((x1-x2)^2+(y1-y2)^2)
p1=Point(9, 2)
p2=Point(7, 0)
p1.show() 
p2.show()  
print("Distance between p1 and p2:", p1.dist(p2))
p1.move(1, 6)
p1.show()
#task 5    
class Account:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def deposit(self, money):
        if money>0:
            self.balance+=money
            print(f"Added {money} tenge. Balance={self.balance}")
        else:
            print("Added funds must be bigger than 0")    
    def withdraw(self, money):
        if money>self.balance:
            print("Not enough money. Try another sum")
        elif money<=0:
            print("Enter positive amount to withdraw")
        else:
            self.balance-=money
            print(f"Here is your money. New balance:{self.balance} tenge") 
acct = Account("Amanbol", 500)
acct.deposit(50)
acct.deposit(200)
acct.withdraw(70)
acct.withdraw(1000)
acct.withdraw(-10)  
#task 6
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers in the list:", prime_numbers)                         
                        