#-------------------------------------------------------- while
# counter = 10
# while counter > 0:
#     # counter = counter - 1
#     counter -= 1
#     print(counter)
#--------------------------------------------------------------------------------

# counter = 50
# while counter > 0:
#     counter -= 1
#     print(f'залишилось посадити {counter} рядків')
# print(' за лічильником')
# print(f'Вся картопля посаджена. {counter}')

#-----------------------------------------------------for
# data = ['Ivan', 'Volodymyr', 'Olexandr', 'Victor' ]
# print(type(data))
#
# dataTwo = ('Ivan', 'Volodymyr', 'Olexandr', 'Victor')
# print(type(dataTwo))
#
# dataThree = {'Ivan', 'Volodymyr', 'Olexandr', 'Victor'}
# print(type(dataThree))
# print("----------------------------------------------------- list []")
# for i in data:
#     print(i)
#
# print("----------------------------------------------------- tuple ()")
# for i in dataTwo:
#     print(i)
#
# print("----------------------------------------------------- set {}")
# for i in dataThree:
#     print(i)

# ----------------------------------------------------------------------------- range

# # listOun = [1,2,3,4,5,6]
# # for i in range(11):
# #     print(f' Hello Python develouper {i}')
# # #---------------------------------------------range()
# listTwo = [1,2,3,4,5,6]
# for i in range(1, 11):
#     print(f' Hello Python develouper {i}')
# #-------------------------------------------- range(1, 10)

# ----------------------------------------------------------------------------- break

# start = int(input('Вкажіть точку початку: \n'))
# finish = int(input('Вкажіть точку завершення: \n'))
# counter = start
# while True:
#     counter += 1
#     print(counter)
#     if counter == finish:
#         print(f'обробку припинено на {finish}')
#         break

# # ---------------------------------------------------

# for i in range(11):
#     if i == 5:
#         print(f'Обробку зупиенно на значені {i-1}')
#         break
#     print(i)
#-----------------------------------------------------continue
# counter = 0
# while counter < 10:
#     counter += 1
#     if(counter % 2) == 0: # - перевіряємо чи  дробова частина результату від ділення дорівнює  " 0 "
#         continue # - продовжити
#     print(counter)
#-------------------------------------------------
# for e in range(4):
#     if e == 3:
#         break # - Припиняємо
#     print(e)
#-------------------------------------------------
# for i in range(6):
#     if i == 3:
#         continue # - пропускаємо
#     print(i)
#-------------------------------------------------
# for i in range(101):
#     if i = 0 and  i % 2 == 1:
#         continue # - пропускаємо
#     print(i)
# #-------------------------------------------------
# string = 'Hello'
# answer = ''
# for i in string:
#     if i == 'l':
#         answer = answer + 's'
#     else:
#         answer = answer + i
# print(answer)
#----------------------------------------------------

# stringOun = 'amsterdam'
# print('stringOun', stringOun)
# # stringTwo = ''
# #
# # for i in stringOun:
# #     if i == 't':
# #         stringTwo  += 'f'
# #     else:
# #         stringTwo  += i
# #
# # print('stringTwo',stringTwo)

#---------------------------------------------------
# print(stringOun.replace('t','f'))
# #
#----------------------------------------------------
# print(help(str))
#----------------------------------------------------
# for i in range(100):
#     if i % 5 == 0:
#         print(i)
#---------------------------------------------------- reversed

list = reversed(range(100)) # --перевертаємо у зворотньому напрямку
for i in list:
    if i % 5 == 0:
        print(i)
        break
# ------------------------------------------------------------
for i in range(-99, 0): # - створюємо  зворотній діапазон від 99 до 0
    if i % 5 == 0:
        print(abs(i)) # - приводимо до модуля число
        break
#--------------------------------------------------------------------


