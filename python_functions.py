from itertools import permutations #for task5
import random
#task 1
def grtoounce():
    weight=float(input("Enter weight in grams: "))
    ounce=weight*28.3495231
    print(f"Weight in ounces={ounce}")
grtoounce()
#task 2
def farToCel():
    farenheit=float(input("Enter temperature in Farenheits: "))
    celcius=(5/9) * (farenheit-32)
    print(f"Temp in Celcius={celcius}")
farToCel()
#task 3
def HowManyAnimals():
    numlegs=int(input("Enter number of legs: "))
    numheads=int(input("Enter the number of heads: "))
    rabbit=(numlegs - 2 * numheads) // 2
    chicken=numheads-rabbit
    print(f"Rabbits: {rabbit} and Chickens: {chicken}")
HowManyAnimals()
#task 4    
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]
numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("Prime numbers:", filter_prime(numbers))
#task 5
def print_permutations():
    s=input("Enter a string: ")
    permut=permutations(s) #создает список всех вариантов
    for p in permut:
        print("".join(p)) #выводит список вариантов
print_permutations()
#task 6
def reverse_words():
    sentence = input("Enter a sentence: ")
    words = sentence.split()         
    reversed_words = words[::-1]         
    new_sentence = " ".join(reversed_words)  
    return new_sentence
print(reverse_words())
#task 7
def has_33(nums):
    for i in range(len(nums) - 1):      #предпоследний
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))        #тру
print(has_33([1, 3, 1, 3]))     #фолс
#task 8
def spy_game(nums):
    code = [0, 0, 7]   
    for n in nums:
        if n == code[0]: #проверка первого числа
            code.pop(0) #убираем число из 007 теперь 07
        if not code:  #когда лист пуст, то всё сошлось
            return True
    return False
print(spy_game([1, 0, 2, 4, 0, 5, 7]))#тру
print(spy_game([1, 7, 2, 0, 4, 5, 0]))#фолс
#task 9
def sphere_volume():
    radius=int(input("Enter the radius: "))
    volume=(4/3)*3.14*radius**3
    print(volume)
sphere_volume()    
#task 10
def unique_list(lst):
    new_list = []   
    for item in lst:
        if item not in new_list:   # если число не в листе
            new_list.append(item)  # добавляем его
    return new_list #иначе, пропускаем
nums = [1, 2, 2, 3, 4, 4, 5, 1, 6, 3]
print(unique_list(nums))
#task 11
def is_palindrome(text):  
    return text == text[::-1] #смотрит тру или фолс
print(is_palindrome("madam"))
print(is_palindrome("hello"))
#task 12
def histogram(lst):
    for x in lst:
        print('*'*x)
histogram([4, 9, 7])
#task 13
def guess_number():
    number=random.randint(1, 20)
    name=input("Hello! What is your name?")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    tries=0
    while True:
        print("Take a guess")
        guess=int(input())
        tries+=1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {tries} guesses!")
            break
guess_number()


