# from calendar import*
# year=int(input('Enter Year'))
# print(calendar(year,2,1,8,4))
# from threading import local
#
x = 1
def print_x():
    print(x)

print_x()
def print_name_spase():
    print('-----------------------------------------------')
    print('locals 1 :',locals())
    data_founding_kiev = 482
    print('locals 2 :',locals())
    age = 2024 - 482
    print('locals 3 :',locals())
    print('-----------------------------------------------')
    print('globals:',globals())
    print('---------------------------------------------------')
#-----------------------------------------locals()


#---------------------------------------------------globals()
print_name_spase()



def external():
    def internal(): #---------- Створюємо функцію
        return 1
    return internal() #-------- Викликаємо функцію

print(external())
print('----------------------------------------------------')
#------------------------------------- Іменована фунція
def foo(x):
    return x**2

print(foo(5))
print('------------------------------')
#-------------------------------------- Анонімна функція
l = lambda x: x ** 2
print(l(7))
print('---------------------------------------------')

