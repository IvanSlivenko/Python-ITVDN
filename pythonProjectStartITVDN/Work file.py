#  ['a','a', 'c'] -------------------------------------------- Список
# {'key0' : 'value', 'key1' : 'value1' , 'key2' : 'value2 ]----------------- Словник
# {'a', 'b', 'c'} --------------------------------------------- Множина
# ( )----------------- Кортеж
#
from turtle import clear

#-----------------------------------------Створюємо множину Вар 1
some_set = {'a', 'b', 'c', 'd', 'c'}
print(some_set) #------------------------- Елементи лише унікальні
print('----------------------------------------')

#-----------------------------------------Створюємо множину Вар 2
some_set_two = set([1,2,3,4,5])
print(some_set_two)
print('------------------------------------------')
#----------------------------------------------------------------
some_set_three = set('develuper')
print(some_set_three)# ---------------------будуть відібрані тільки інікальні значення та впорядковані
list = list('develuper')
print(list)
print('-----------------------------------')
#-------------------------------------- Визначаємо довжину множини len()
some_set_four = set('devops')
print(some_set_four)
print(len(some_set_four))
print('----------------------------------')

# -------------------------------------- перевіряємо наявність символа в середині нашої колекції
some_set_six = set('internet')
print(some_set_six)
print('w' in some_set_six)
print('i' in some_set_six)
print('-----------------------------------')
#---------------------------------------- Методи множин
# print(help(set)) # ------------------------------------------Перелік методів множин

#-------------------------------------------------незмінна множина Frozenset
some_frozen_set = frozenset('internet')
# print(some_frozen_set)
print('-----------------------------------')

# print(dir(some_frozen_set))
print('-----------------------------------------')
#-------------------------------------------------- очищаємо множину
print(some_set_six)
some_set_six.clear()
print(some_set_six)
print('------------------------------------------')
#---------------------------------------------------- видаляємо один (випадковий) елемент множини pop()
print(some_set_four)
some_set_four.pop()
print(some_set_four)
print('-------------------------------------------')
#----------------------------------------------------- видаляємо один (конкретний) елемент з множини discard()
#----------------------------------------------------- але не отримуємо помилки, якщо елементу немає у множині
print(some_set_four)
some_set_four.discard('e')
print(some_set_four)
some_set_four.discard('p')
print(some_set_four)
print('--------------------------------------------')
#----------------------------------------------------- видаляємо один (конкретний) елемент з множини remove()
#----------------------------------------------------- та отримуємо помилки, якщо елементу немає у множині
print(some_set_four)
some_set_four.remove('s')
print(some_set_four)
print('--------------------------------------------')
# some_set_four.remove('z')
print(some_set_four)
print('--------------------------------------------')
#-------------------------------------------------- додаємо елемент у множину на випадкову позицію add()
print(some_set_four)
some_set_four.add('z')
print(some_set_four)
some_set_four.add('w')
print(some_set_four)
print('---------------------------------------------')
#------------------------------------------------- Поєднання множин union()
print(some_set_four)
some_set_seven = set('antarktyda')
print(some_set_seven)
some_set_eight = some_set_four.union(some_set_seven)
print('some_set_eight', some_set_eight)
#------------------------------------------------------ або  Поєднання множин |
some_set_ten = some_set_four | some_set_seven
print('some_set_ten' , some_set_ten)
# ------------------------------------------------------або  Поєднання множин |=
some_set_ten |= some_set_seven
print('some_set_ten', some_set_ten)

print('-----------------------------------------------------------------------')

#-------------------------------------------------- Перетин множин intersection()
print('some_set_seven', some_set_seven)
print('some_set_eight', some_set_eight)
some_set_nine = some_set_eight.intersection(some_set_seven)

print('some_set_nine', some_set_nine)
print('------------------------------------------------------------------------')
#-------------------------------------------------- або Перетин множин   &
some_set_twelve = some_set_eight & some_set_seven
print('some_set_twelve', some_set_twelve)
#--------------------------------------------------Різниця між множинами difference()
print('some_set_seven', some_set_seven)
print('some_set_twelve', some_set_twelve)
some_set_thirteen = some_set_twelve.difference(some_set_seven)
print('some_set_thirteen', some_set_thirteen)
print('-------------------------------------------')
#----------------------------------------------------- isdisjoint()
print('some_set_twelve', some_set_twelve)
print('some_set_seven', some_set_seven)
print(some_set_twelve.isdisjoint(some_set_six))
print('--------------------------------------------')
#------------------------------------------------------ issubset()
print('some_set_twelve', some_set_twelve)
print('some_set_seven', some_set_seven)
print(some_set_twelve.issubset(some_set_seven))
# print(some_set_twelve <= (some_set_seven))
print('--------------------------------------------')
#----------------------------------------------------- Створення нової множини, що є симетричною
#----------------------------------------------------- до різниці між множинами symmetric_difference()
some_set_15 = {1, 2, 3}
some_set_16 = {1, 2, 3, 4}
print('some_set_15', some_set_15)
print('some_set_16', some_set_16)
some_set_17 = some_set_15.symmetric_difference(some_set_16)
#----------------------------------------------------- або ^ (робота тільки з множинами)
print('some_set_17', some_set_17)
some_set_18 = some_set_15 ^ some_set_16
print('some_set_18', some_set_18)
print('---------------------------------------------')
#----------------------------------------------------- Кортежі
some_tuple = (1, 2, 3)
print('some_tuple', some_tuple)
print('----------------------------------------------')
some_tuple_1 = ([], {}, set(), ())
print('some_tuple_1', some_tuple_1)
print('----------------------------------------------')

#------------------------------------------------------- Створення кортежів tuple()
some_tuple_3 = tuple(['a', 'b', 'c'])
print('some_tuple_3', some_tuple_3)
print('----------------------------------------------')
some_tuple_4 = tuple('internet')
print('some_tuple_4', some_tuple_4)
# ---------------------------------------------------- Методи кортежів
#------------------------------------------------------------------------------------ len()
print(len(some_tuple_4))
print('----------------------------------------------')
#--------------------------------------------------------------перевіряємо  наявність стрічки у кортежі
print('n' in some_tuple_4)
print('----------------------------------------------')
#------------------------------------------------------------рахуємо скільки разів зустрічається
#------------------------------------------------------------------------------ елемент у кортежі------count()
print(some_tuple_4.count('n'))
#------------------------------------------------------------отримуємо індекс потрібного елементу index()
print('----------------------------------------------')
print(some_tuple_4.index('r'))
















