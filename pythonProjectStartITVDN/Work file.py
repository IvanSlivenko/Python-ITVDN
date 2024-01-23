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

def printing_positional_arguments(first, second):
    print(f'{first=} {second=}')
printing_positional_arguments('FIRST','SECOND')

