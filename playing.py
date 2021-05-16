'''
name = 'Jhonny'
age = 55
# The clean way to use variables
print(f'hi {name}. You are {age} years old')


# String indexes
selfish = '01234567'
# where to look at []
print(selfish[2])
# Where to start/ where to finish [start:over]
selfish = '01234567'
print(selfish[0:4])
# Stepover [start"stop:stepover]
print(selfish[0:8:2])
# go all the way to the end
print(selfish[1:])
# all before there
print(selfish[:-5])
# reverse the string
print(selfish[::-1])


# lenght of things
print(len(selfish[::-1]))

# built-in functions
quote = 'to be or not to be'
print(quote.find('be'))

tula = (quote.replace('be', 'tula'))
print(tula)
print(quote)


# booleans
name = 'Fer'
is_cool = False
is_cool = True

# Exercise, Age guesser

name = 'Fer'
age = 50
relationship_status = 'Single'

relationship_status = 'It\'s complicated'

print(relationship_status)


birth_year = int(input('what year were yo born? \n'))

from datetime import datetime


sys_date = str(datetime.now())



actual_year = sys_date[0:4]

guessing_age = int(actual_year) - birth_year

age_message = (
    f'Hello {name}. It\'s been passed {guessing_age} years from your birth day!')

print(age_message)


# Exercise Password checker

user_name = str(input('Hello,write your name here: \n') #Ask user name's
)


pswd = str(input(f'{user_name}, please write your password: \n'))

pswdlen = len(pswd)

pswdsec = ('*' * pswdlen)

print(f'{user_name}. Your password {pswdsec} is {pswdlen} letters long')

li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1,2,'a',True]


amazon_cart = ['notebooks', 'sunglasses']

print(amazon_cart[0])



# list slicing

amazon_cart = [
  'notebooks',
  'sunglasses',
  'toys',
  'grapes'
  ]


amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:]
new_cart[0] = 'gum'


print(new_cart)
print(amazon_cart)



# Matrix

matrix = [
  [1,9,3],
  [2,4,5],
  [7,8,9]

]

print(matrix[0][1])
basket = [1,2,3,4,5]

basket.append(100)
basket.extend([104])
basket.insert(2, 909)
new_list = basket[:]
# adding

print(basket)
# print(new_list)

# removing
basket.pop() # removes the last
basket.pop(0) #removes by index
basket.remove(4) #removes the objetc
print(basket)

print(basket.clear())


basket = ['a','j','z','b','c','d','e']

print(basket.index('a'))

print(basket.index('d', 0 ,6))

print('d' in basket)
print('x' in basket)
print('My' in 'My name\'s is ian')

print(basket.count('d'))
basket.sort()
print(basket)


| = or
& = and





is_friend = True
is_user = False
can_message = "Message allowed" if is_friend else "message not allowed"

relationship = "Best Friends" if (is_friend | is_user) else "No best friends"

print(relationship)
print(can_message)




is_magician = False
is_expert = True



if(is_magician and is_expert):
  print("You are a master magician")
elif (is_magician and not is_expert):
  print("At least you're getting here")
elif not is_magician:
   print("You need magic powers")
else:
  print("wow")



user = {
  'name': 'Golem',
  'age': 5600,
  'can_swim': True
}



for item in user.items():
  print(item)


for key, value in user.items():
  print(key, value)

for item in user.keys():
  print(item)

for item in user.values():
  print(item)



_list = [1, 2, 3 ,4, 5, 6, 7, 8, 9, 10]


counter = 0

for item in _list:
  counter = counter + item

print(counter)



for _ in range(10):
  print(_)

for _ in range(2):
  print(list(range(10)))

"this doesnt works"
for _ in range(10, 0):
  print(_)

for _ in range(10, 0, -1):
  print(_)



for i,char in enumerate('Helloooo'):
  print(i,char)


for i,char in enumerate(list(range(101))):
  print(i,char)




seeking_number = int(input("Type any number from 0 to 100: \n"))

for i,char in enumerate(list(range(100))):
  if (char == seeking_number):
    print(f'the index of your number {seeking_number} is: {i}')



my_list = [1,2,3]

for item in my_list:
  print(item)

i = 0
while i < len(my_list):
  print(my_list[i])
  i += 1

while True:
  response = input('type something: ')
  if response == 'bye':
    break



# exercise

picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
]


def show_tree():
  for row in picture:
    for pixel in row:
      if (pixel == 1):
        print('*', end = '')
      else:
        print(' ', end = '')
    print('')



# finding duplicates

my_list = ['a','b','c','d','d','e','f','g','h','m','m']

duplicates = []
for letter in my_list:
  if my_list.count(letter) > 1:
    if letter not in duplicates:
      duplicates.append(letter)
print(duplicates)


def say_hello():
  print("hello")
say_hello()

show_tree()
print('')
show_tree()


def sum(num1, num2):
  def another_func(n1, n2):
    return n1 + n2
  return another_func(num1, num2)

total = sum(10,20)
print(total)


def is_even(num):
  if num % 2 == 0:
    return True
  return False
print(is_even(51))

def is_even_btt(num):
  return num % 2 == 0
print(is_even_btt(51))


#
# *args **kwargs

def super_funct(name, *args, i='hi', **kwargs):
  total = 0
  for items in kwargs.values():
    total += items
  return sum(args) + total


print(super_funct('Andy', 1,2,3,4,5, num1=5, num2=10))

# Rule: params, *args, default parameter, **kwargs



def highest_even(li):
  evens = []
  for items in li:
    if items % 2 == 0:
      evens.append(items)

  return max(evens)


print(highest_even([10,2,3,4,8,11,100,88]))



a = 'helloooooooo'

if (n := len(a)) > 10:
  print(f"too long {n} elements")



while ((n := len(a)) > 1):
  print(n)
  a = a[:-1]

print(a)

'''

# Scope - what variables do i have access to?


# # class PlayerCharacter:
# #     # Class object attribute
# #     membership = True

# #     def __init__(self, name, age):
# #         if(PlayerCharacter.membership):
# #             self.name = name
# #             self.age = age
# #         else:
# #             print('No membership')

# #     def shout(self):
# #         print(f'my name is {self.name}')

# #     def run(self, hello):
# #         print(f'my name is {self.name}')


# # player1 = PlayerCharacter('Andre', 33)
# # player2 = PlayerCharacter('Fer', 54)
# # player2.attack = 50

# # print(player1.run('hello'))
# # print(player1.shout())
# # # print(player1.run())
# # # print(player2.age)

# # # help(list)
# # # print(player2)

# # # print(player2.attack)
# # # print(player2.membership)


# class PlayerCharacter:
#     membership = True

#     def __init__(self, name, age):

#         self.name = name
#         self.age = age

#     def shout(self):
#         print(f'my name is {self.name}')

#     @classmethod
#     def adding_things(cls, num1, num2):
#         return cls('Teddy', num1 + num2)


#     @staticmethod
#     def adding_things2(num1, num2):
#         return (num1 + num2)


# player3 = PlayerCharacter.adding_things(2, 2)
# print(player3.name)
# print(player3.age)


# class PlayerCharacter:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     def playerinfo(self):
#         print(f'my name is {self._name} and I am {self._age} years old')
# # _variable --> _ means private

# player1 = PlayerCharacter('Fer', 23)

# print(player1.playerinfo())
# print(player1.speak())


# users
# class User:
#     def __init__(self, email):
#       self.email = email

#     def sign_in(self):
#         print('logged in')

#     def attack(self):
#         print('Do Nothing')


# class Wizzard(User):
#     def __init__(self, name, power, email):
#         super().__init__( email)
#         self.name = name
#         self.power = power

#     def attack(self):
#         User.attack(self)
#         print(f'attacking with power of {self.power}')


# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f'attacking with {self.num_arrows} arrows')


# wizard1 = Wizzard('Mage', 60, 'mage@gmail.com')
# archer1 = Archer('Bowy', 30)


# def player_attack(char):
#     char.attack()


# print(isinstance(wizard1, object))
# player_attack(wizard1)
# player_attack(archer1)

# for char in [wizard1, archer1]:
#     char.attack()

# print(wizard1.name)
# print(wizard1.email)


# print(dir(wizard1)) # dir makes possible the object introspection

# class Toy():
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age
#         self.my_dict = {
#             'name': 'Yoyo',
#             'has_pets': False
#         }

#     def __str__(self):  # Changes the value of the method
#         return f'{self.color}'

#     def __len__(self):  # Changes the value of the method
#         return 590

#     def __del__(self):  # Changes the value of the method
#         print('deleted!')

#     def __call__(self):
#         return ('yeeeesss???')

#     def __getitem__(self, i):
#         return self.my_dict[i]


# action_figure = Toy('red', 0)
# print(action_figure.__str__())
# print(str(action_figure))  # Changes the value of the method
# print(len(action_figure))  # Changes the value of the method
# print(action_figure())
# print(action_figure['name'])


# del action_figure  # Changes the value of the method


# class SuperList(list):

#     def __len__(self):
#         return 1000


# super_list1 = SuperList()
# print(len(super_list1))
# super_list1.append(5)
# print(super_list1[0])
# print(len(super_list1))
# print(issubclass(SuperList, list))
# print(issubclass(list, object))

# class User():
#     def sign_in(self):
#         print('You are logged in')


# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f'attacking with power of {self.power}')

# class Archer(User):
#     def __init__(self, name, arrows):
#         self.name = name
#         self.arrows = arrows

#     def check_arrows(self):
#         print(f'{self.arrows} remaining')

#     def run(self):
#       print('ran really fast')

# class HybridBorg(Wizard, Archer):
#   def __init__(self, name, power, arrows):
#     Archer.__init__(self, name, arrows)
#     Wizard.__init__(self, name, arrows)

# hb1 = HybridBorg('borgie', 50, 100)

# print(hb1.attack())
# print(hb1.check_arrows())
# print(hb1.sign_in())

# MRO - Method Resolution Order

# class A:
#     num = 10


# class B(A):
#     pass


# class C(A):
#     num = 1


# class D(B, C):
#     pass

# print(D.mro())

# class X:pass
# class Y:pass
# class Z:pass
# class A(X,Y):pass
# class B(Y,Z):pass
# class M(B,A,Z):pass

# print(M.__mro__)


# Functional programming


# map . filter , zip, and ,reduce

# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list
# new_list = ''

# # print(map(multiply_by2, ([1,2,3])))

# from functools import reduce
# # map()
# my_list = [1, 2, 3]
# your_list = [10, 20, 30]
# their_list = (5, 3, 2)


# def multiply_by2(item):
#     return item*2


# print(list(map(multiply_by2, my_list)))
# print(my_list)

# # filter()


# def only_odd(item):
#     return item % 2 != 0


# print(list(filter(only_odd, my_list)))

# # zip()

# print(list(zip(my_list, your_list, their_list)))
# print(my_list)

# # reduce()


# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item

# print(reduce(accumulator, my_list, 0))

# # lambda expressions
# # lambda param: action(param)

# print(list(map(lambda item: item*2, my_list)))

# print(list(filter(lambda item: item % 2 !=0, my_list)))

# print(reduce(lambda acc, item: acc + item, my_list))

# my_list = [5, 4, 3]

# #Square
# new_list = print(list(map(lambda item: item**2, my_list)))
# print(new_list)
# #List sorting base in the second number

# li = [(0,2),(4,3),(9,9), (10,-1)]

# print(sorted(li, key = lambda x: x[1]))

# list, set, dictionary comprehension


# my_list = [char for char in 'hello']
# my_list2 = [num for num in range(0,100)]
# my_list3 = [num*2 for num in range(0,100)]
# my_list4 = [num**2 for num in range(0,100) if num % 2 == 0]

# print(my_list4)
# print(my_list3)
# print(my_list)
# print(my_list2)

# set comprehension
# my_list = {char for char in 'hello'}
# my_list2 = {num for num in range(0, 100)}
# my_list3 = {num*2 for num in range(0, 100)}
# my_list4 = {num**2 for num in range(0, 100) if num % 2 == 0}
# # print(my_list4)
# print(my_list3)
# print(my_list)
# print(my_list2)


# dict comprehension

# simple_dict = {
#     'a': 1,
#     'b': 2

# }

# my_dict = {k: v**2 for k, v in simple_dict.items() if v % 2 == 0}

# print(my_dict)

# my_dict2 = {num:num*2 for num in [1, 2, 3]}
# print(my_dict2)
# some_list = ['a','b','c','b','d','m','n','n']

# duplicate = list(set([letter for letter in some_list if some_list.count(letter) >1 ]))
# print(duplicate)

# High Order Function HOC

# def greet(func):
#   func()

#   def greet2():
#     def func():
#       return 5
#     return func

# Decorator Pattern


from time import time


def my_decoratorPattern(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_func


# hello()

# @my_decorator
# def bye():
#   print('see you later')

# bye()


# # Decorator example
# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         print('*************')
#         func(*args, **kwargs)
#         print('*************')
#     return wrap_func


# @my_decorator
# def hello(greeting, emoji=':('):
#     print(greeting, emoji)


# hello('hiii')

# # Decorator


# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, **kwargs)
#         t2 = time()
#         print(f'took {t2-t1} ms')
#         return result
#     return wrapper


# @performance
# def long_time():
#     for i in range(1000):
#         i*5

# long_time()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        # Here valid equals True , *args[0] = (('name': 'Sorna'), ('valid': True)), ['valid'] = True or False
        if args[0]['valid']:
            return fn(*args, **kwargs)
        else:
            print('Ups, You are not logged in')  # Here valid equals to False
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


# message_friends(user1)


# Error handling in Python
# while True:
#     try:
#         age = int(input('how old are you?'))
#         10/age
#         print(age)
#     except ValueError:
#         print('please enter a number')
#     except ZeroDivisionError:
#         print('please enter age higher than zero')
#     else:
#       print('thank you')
#       break

# def sum(num, num2):
#     try:
#         return num/num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(f'please enter numbers or letters! -> {err}')


# print(sum(1, 0))


# while True:
#     try:
#         age = int(input('how old are you?'))
#         10/age
#         raise ValueError('hey cut it out')
#     except ZeroDivisionError:
#         print('please enter age higher than zero')
#         break
#     else:
#         print('thank you')

#     finally:
#         print('ok, i am already done')
#     print('can you hear me')


# Generators

# range(100)
# list(range(100))


# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i)
#     return result

# my_list = make_list(1000)
# print(my_list)
# # print(list(range(1000)))


# def generator_function(num):
#     for i in range(num):
#         yield i


# g = generator_function(100)

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# # for item in generator_function(1000):
# #   print(item)


# # Why generators


def performance(fn):  # This allows to take the time of the script
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} ms')
        return result
    return wrapper


# @performance
# def long_time():
#     print('1')
#     for i in range(100000):
#         i*5


# @performance
# def long_time2():
#   print('2')
#   for i in list(range(100000)):
#     i*5


# long_time()
# long_time2()


# So generators

# def gen_fun(num):
#   for i in range(num):
#     yield i

# for item in gen_fun(100):
#   pass


# This is a for loop

# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             print(next(iterator)*2)
#         except StopIteration:
#             break


# special_for([1, 2, 3])


# # This is how a range() works
# class MyGen():
#     current = 0

#     def __init__(self, first, last):
#         self.first = first
#         self.last = last

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if MyGen.current < self.last:
#             num = MyGen.current
#             MyGen.current += 1
#             return num
#         raise StopIteration


# gen = MyGen(0, 100)


# for i in gen:
#     print(i)


# # Fibonacci generator

# @performance
# def fib_num(num):
#     a = 0
#     b = 1
#     for i in range(num):
#         yield a
#         temp = a
#         a = b
#         b = temp + b


# for x in fib_num(2000):
#     print(x)

# @performance
# def fib_num2(num):
#     a = 0
#     b = 1
#     result = []
#     for i in range(num):
#         result.append(a)
#         temp = a
#         a = b
#         b = temp + b
#     return result

# print(fib_num2(2000))

# from utility import multiply, divide
# from shopping.more_shopping import shopping_cart


# # print(shopping_cart.buy('item'))
# # print(divide(2, 3))
# # print(multiply(4, 20))
# # print(max([1,2,3]))


# # # if __name__ == '__main__'':
# #     # print(shopping_cart.buy('item'))
# #     # print(divide(2, 3))
# #     # print(multiply(4, 20))
# #     # print(max([1,2,3]))

# # # print(__name__)
# import utility
# import shopping.shopping_cart
# print(utility.divide(1, 2))

# print(shopping.shopping_cart.buy('item'))


# # Useful modules

# from collections import Counter, defaultdict, OrderedDict

# li = [1,2,3,4,5,6,7,7,7]
# sentence = 'blah blah blah thinking about python'

# print(Counter(li))
# print(Counter(sentence))

# my_dict = defaultdict(int,{'a' : 1, 'b':2})  # lambda: x -> this will return anything its in the variable lambda

# print(my_dict['a']) # returns 0 because nothing is inside the dictionaryt

# d = OrderedDict()

# d['a']=1
# d['b']=2


# d2 = OrderedDict()
# d2['b'] = 2
# d2['a'] = 1
# print(d2 ==d)

# import datetime
# print(datetime.time(2,0,0))

# print(datetime.date.today())


# from array import array

# arr = array('i', [1,2,3])
# print(arr[0])


# debuggin' tips

# use a linting for type errors in code
# use an IDE or a code editor instead
# learn to read errors

# PDB Python Debugger https://docs.python.org/3/library/pdb.html

# import pdb
# def add(num1, num2):
#     pdb.set_trace()
#     return num1 + num2


# add(4, 'asdasdasd')
# #

my_file = open('test.txt')

print(my_file)