from array import array
import datetime
from collections import Counter, defaultdict, OrderedDict
import utility
import shopping.shopping_cart
print(utility.divide(1, 2))

print(shopping.shopping_cart.buy('item'))


# Useful modules


li = [1, 2, 3, 4, 5, 6, 7, 7, 7]
sentence = 'blah blah blah thinking about python'

print(Counter(li))
print(Counter(sentence))

# lambda: x -> this will return anything its in the variable lambda
my_dict = defaultdict(int, {'a': 1, 'b': 2})

print(my_dict['a'])  # returns 0 because nothing is inside the dictionaryt

d = OrderedDict()

d['a'] = 1
d['b'] = 2


d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1
print(d2 == d)

print(datetime.time(2, 0, 0))

print(datetime.date.today())


arr = array('i', [1, 2, 3])
print(arr[0])


def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return 'Please enter a number'
    except ValueError as err:
        return err
    except TypeError as err:
        return err
