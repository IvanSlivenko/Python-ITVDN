def print_sum():
    print(2+2)
print_sum()
print('----------------------')
def print_sum_2(a, b):
    print(a+b)
print_sum_2(2,3)
print('----------------------')
def example_1():
    pass
example_1()
print(' example_1 -------------------------')

def example_2():
    ...
example_2()
print('example_2 .........................')
def example_3():
    """ docstring for information"""
example_3()
print(' example_3 .........................')
# print(help(example_3))


first, second, third, *anything_left = ('FIRST', 'SECOND', 'THIRD','FOURTH','FIFTH','...')
print(first, second, third, anything_left)
print('--------------------------------------')

# def printing_positional_arguments(first, second,*anythining_left):
def printing_positional_arguments(first, second, *test):
    print(f'{first=} {second=}')
printing_positional_arguments('FIRST','SECOND','THIRD','FOURTH','FIFTH','...')
print('----------------------------------------')

def print_sum_2(a, b,*elements):
    return(a+b+sum(elements))

result = print_sum_2(2,3,4,5,6,7,8,9,10)
print('result:', result)

def make_pizza(*topings):
    for topping in topings:
        print(f'- {topping}')
make_pizza('mushrums','sausages','cheese','capers')
print('-----------------------------------')
