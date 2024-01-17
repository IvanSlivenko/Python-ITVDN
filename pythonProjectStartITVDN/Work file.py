# dictionary structure ^
#
# 'key' - string
# 'value' - string

# {'key' : 'value'}


# example_dict = {
# 'first_name':'Ivan',
# 'last_name':'Slivenko'
# }
# print(example_dict['first_name']) #--------------- Отримуємо за ключем
#
#
# print(example_dict.get('last_name')) #------------- Отримуємо методом get

#-----------------------------------------------------Створення словника Вар 1
print('---------------------------------------------------------')
capital_cities ={
    'Venesuela' : 'Caracas',
    'Nicaragua' : 'Managua',
    'Ukraine' : 'Kiev'
}

print(capital_cities)
#-----------------------------------------------------Створення словника Вар 2
print('-------------------------------------------------------')
capital_cities_2 = dict([['Venesuela' , 'Caracas'],['Nicaragua' , 'Managua'],['Ukraine' , 'Kiev']])

print(capital_cities_2)

#-----------------------------------------------------Створення словника Вар 3
print('-------------------------------------------------------')
capital_cities_3 = dict(Venesuela='Caracas', Nicaragua = 'Managua', Ukraina = 'Kiev' )
print(capital_cities_3)
print(capital_cities_3['Ukraina'])

#----------------------------------------------------------------------- Додаємо елементи до словника

#----------------------------------------------------------------------- Вар 1
print('--------------------------------------------------------')

capital_cities_3['Canada'] = 'Ottava'
capital_cities_3['Georgia'] = 'Tbilisi'
capital_cities_3['Moldova'] = 'Kishinev'
capital_cities_3['China'] = 'Beijing'

print(capital_cities_3)

print('---------------------------------------------------------')
#------------------------------------------------------------------Створення порожнього словника
#-----------------------------------------Вар 1
capital_cities_4 = {}
print(capital_cities_4)

#----------------------------------------Вар 2
capital_cities_5: dict = dict()
print(capital_cities_5)
#----------------------------------------
print('---------------------------------------------------------')

cities_year_fundation:dict = dict()
cities_year_fundation['Kharkiv'] = 1654
cities_year_fundation['Chuguiv'] = 1638
print(cities_year_fundation)
cities_year_fundation['Kharkiv'] = {'Year for fundation': 1654, 'Main rivers': ['Kharkiv', 'Lopan']}
print('----------------------------------------------------------')
print(cities_year_fundation)
print('---------------------------------------------------------')


#-------------------------------------------------- Видаляємо елемент словника
del cities_year_fundation['Chuguiv']
print(cities_year_fundation)
print('-----------------------------------------------------------')
#----------------------------------------------------Перебираємо словники
print(capital_cities_3)
for i in capital_cities_3:
    print(i)  # -------------------------Перебираємо ключі
    print(capital_cities_3[i])#--------------------------- Перебираємо значення

    print(i, capital_cities_3[i])
    print('--------------')


print('-----------------------------------------------------------')


#----------------------------------------- Методи словників
# x = dir(dict())
# for i in x:
#     print(i)
#----------------------------------- Переглядаємо список методів словників

#------------------------------------ Деструктуризація Словників------------------items()
print(capital_cities_3)
for country, capital in capital_cities_3.items():
    print('-------------------------------------')
    print(f'{country} : {capital}')

#------------------------------------- Очищення словників ------------------------clear()
print('----------------------------------------------------------------------------')
print(capital_cities_3)
# capital_cities_3.clear()
print(capital_cities_3)
print('-----------------------------------------------------------------------------')
#------------------------------------- Видаляємо значення за ключем та повертаємо його -------- pop()

del_el = capital_cities_3.pop('China')
print(del_el)
print(capital_cities_3)
print('---------------------------------------')
#------------------------------------ Видаляємо ключ та значення та повертаємо його ----------- popitem()
print(capital_cities_3)
del_el_two = capital_cities_3.popitem()
print(del_el_two)
print(capital_cities_3)
print('----------------------------------------')
#------------------------------------ Додаємо у кінець новий елемент словника -------------- update()
brazil = {'Brazil': 'Brazilia'}
capital_cities_3.update(brazil)
print(capital_cities_3)
print('----------------------------------------')
#----------------------------------- Отримуємо список значень (без ключів) ----------------- values()
print(capital_cities_3)
values_capital = capital_cities_3.values()
print(values_capital)
print('----------------------------------------')
#------------------------------------Отрмуємо список ключів ------------------------ keys()
print(capital_cities_3)
keys_capital_3 = capital_cities_3.keys()
print(keys_capital_3)
print('---------------------------------------')
#------------------------------------- Отримуємо значення за ключем -- або None------------- get()
print(capital_cities_3)
print(capital_cities_3.get('Brazil'))
print('--------------------------------------------')

#--------------------------------- Повертаємо значення за замовчуванням ----------- setdefault()
print(capital_cities_3)
capital_cities_3.setdefault('Romania', 'Bucharest')
print(capital_cities_3)
print('--------------------------------------------------------')
#--------------------------Повертаємо новий словник з ключами та значеннями (одним для всіх)---------- fromkeys()
print(capital_cities_3)
days_name_list = ['Monday', 'Thusdey', 'Wensdey']
empty_dictionary: dict = {}
new_dict = empty_dictionary.fromkeys(days_name_list, '24')
print(new_dict)
print('------------------------------------------------')

#-------------------- Скільки разів Ім'я зустрічається у списку --- Варіант 1
classmates_name = ['Sergiy', 'Igor', 'Tanya', 'Sergiy', 'Lena']
print('classmates_name', classmates_name)
answer = {}
for i in classmates_name:
    print(i)
    if i in answer.keys():
        answer[i] += 1
    else:
        answer[i] = 1
print('answer', answer)
print('---------------------------------------------------')
#-------------------- Скільки разів Ім'я зустрічається у списку --- Варіант 2
answerTwo = {}
for i in classmates_name:
    answerTwo[i] = classmates_name.count(i)#-------------------- count()
print('answerTwo', answerTwo)
print('--------------------------------------------------')

#-------------------- пройтися за словником та виявити всі значення, що мають парний ключ
data_dict = {1 :'one', 33 : 'any text', 3 : 3, 5 : 5, 6 : 'x', 9: 'end'}
print('data_dict', data_dict)
print('значення, у яких ключі - парні')
for el in data_dict:
    if el % 2 == 0:
        print(data_dict[el])
print('----------------------------------------------------------------')














