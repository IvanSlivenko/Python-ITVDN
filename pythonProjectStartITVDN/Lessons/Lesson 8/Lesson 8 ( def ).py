from itertools import count


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

#---------------------------------------------------- Позиційні аргументи
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
#-------------------------------------------------------- Запаковка - розпаковка
def make_pizza(*topings):
    for topping in topings:
        print(f'- {topping}')
make_pizza('mushrums','sausages','cheese','capers')
print('-----------------------------------')
#--------------------------------------------------------- Ключові агрументи
def make_pizza_2(first, second, third):
    print(f'{first=} {second=} {third=}')
make_pizza_2(second='second',first='FIRST', third='THIRD')
print('----------------------------------------------------')

def hello_user(name, surname, middlename):
    print(f'hello {name} {surname} {middlename} ')
hello_user(surname='Dil',name='Mark',middlename='Mon')
print('----------------------------------------------------------')
#----------------------------------------------------------------------default значення параметрів
def hello_user_2(name='Ivan', surname='Kanduba', middlename='Uranian'):
    print(f'hello {name} {surname} {middlename} ')
hello_user_2(surname='Dil',name='Mark',middlename='Mon')
hello_user_2(surname='Dil',name='Mark')
hello_user_2()
#-------------------------------------------------------------------- Мікс параметрів (позиційні, кючові, дефолтні)
hello_user_2('Sergiy', middlename='Kozak')
print('------------------------------------------------------------')
def hello_user_3(job_position, name='Ivan', surname='Kanduba', middlename='Uranian',**kwargs):
    print(kwargs)
    print(f'hello {name} {surname} {middlename} your job position is {job_position}')
hello_user_3('programer',surname='Dil',name='Mark',work_country='Brazil',work_kar='KAT')
print('------------------------------------------------------------')

#--------------------------------------------------------------------------return
def sum_2(*params):
    return sum(params)
result = sum_2(5, 5, 5, 5, 5)
print(result)
print('--------------------------------------------------------------')

def sum_3(*params):
    result = sum(params)
    return result
res = sum_3(5, 5, 5, 5, 5)
print(res)
print(type(sum_3))

print('--------------------------------------------------------------')
#----------------------------------------------------------------------- Вкладеність функцій

def external(*params):
    def internal():
        pass
    return internal

type(external())
print('----------------------------')
#--------------------------------------------------------------------- Var 1_1
def finding_max_value_in_list(list):
    i_max = 0
    for i in list:
        if i > i_max:
            i_max = i

    if i_max <= 0:
        return 'Максимальне число менше 0'
    else:
        return i_max


max_value_from_list = finding_max_value_in_list([1, 2, 3, 100, 200, 300])
print('Var 1:', max_value_from_list)
#--------------------------------------------------------------------- Var 1_2
def finding_max_value_in_list_2(list):
    i_max = 0
    for i in list:
        if i > i_max:
            i_max = i
    return 'Максимальне число менше 0' if i_max <= 0 else i_max

max_value_from_list_2 = finding_max_value_in_list_2([1, 2, 3, 100, 200, 400])
print('Var 2:', max_value_from_list_2)

#--------------------------------------------------------------------- Var 1_3
def finding_max_value_in_list_2(list):
    i_max = max(list)
    return 'Максимальне число менше 0' if i_max <= 0 else i_max

max_value_from_list_2 = finding_max_value_in_list_2([1, 2, 3, 100, 200, 400, 500])
print('Var 3:', max_value_from_list_2)

#----------------------------------------------------------------- Var 2_1_
def countting_letters_word(word):
    count = 0
    for el in word:
        count += 1
    print(f'Кількість літер у слові {word} дорівнює : {count}')
    return count
print('--------------------------------------------------------------------')
countting_letters_word('Gwadalachara')
#----------------------------------------------------------------- Var 2_2_
def countting_letters_word_2(word):
    count = len(word)

    print(f'Кількість літер у слові {word} дорівнює : {count}')
    return count

countting_letters_word_2('Argentuna')
print('-----------------------------------------------------------------------')
#-------------------------------------------------------------------Var 3_1
def exponentiate_number(number, power):
    if power>0:
        result = number ** power
        print(f'Число {number} у степені {power} становитиме : {result}')
        return result
    elif power == 0:
        print(f'Значення параметру ступінь {power} дорівнює 0 ')
    else:
        print(f'Значення параметру ступінь {power} менше 0 ')

exponentiate_number(10,2)
print('---------------------------------------------------------------------')
#-------------------------------------------------------------------Var 3_2
def exponentiate_number_2(number, power):
    if power>0:
        result = pow(number, power)
        print(f'Число {number} у степені {power} становитиме : {result}')
        return result
    elif power == 0:
        print(f'Значення параметру ступінь {power} дорівнює 0 ')
    else:
        print(f'Значення параметру ступінь {power} менше 0 ')

exponentiate_number_2(100,2)
print('---------------------------------------------------------------------')
numbers = [1, 2, 3]
#----------------------------------------------------------------- Var 4_1
def reversing_list_numbers(n):
    print('Список до змін', numbers)
    n = n.copy()
    n.reverse()
    print('Список після змін', n)
    return n

reversing_list_numbers(numbers)
print('-----------------------------------------------------')
#----------------------------------------------------------------- Var 4_2
def reversing_list_numbers(n):
    print('Список до змін', numbers)
    n = n[:]
    n.reverse()
    print('Список після змін', n)
    return n

reversing_list_numbers(numbers)
print('-----------------------------------------------------')








