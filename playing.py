'''
name = 'Jhonny'
age = 55
#The clean way to use variables
print(f'hi {name}. You are {age} years old')


# String indexes 
selfish = '01234567'
# where to look at []
print(selfish[2])
#Where to start/ where to finish [start:over]
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


#booleans
name = 'Fer'
is_cool = False
is_cool = True

#Exercise, Age guesser

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

age_message = (f'Hello {name}. It\'s been passed {guessing_age} years from your birth day!')

print(age_message)


#Exercise Password checker

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



#list slicing

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



#Matrix

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
#adding

print(basket)
#print(new_list)

#removing 
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

#Rule: params, *args, default parameter, **kwargs



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
class User:
    def __init__(self, email):
      self.email = email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print('Do Nothing')


class Wizzard(User):
    def __init__(self, name, power, email):
        super().__init__( email)
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with {self.num_arrows} arrows')


wizard1 = Wizzard('Mage', 60, 'mage@gmail.com')
archer1 = Archer('Bowy', 30)


def player_attack(char):
    char.attack()


print(isinstance(wizard1, object))
player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()

print(wizard1.name)
print(wizard1.email)


print(dir(wizard1)) # dir makes possible the object introspection


