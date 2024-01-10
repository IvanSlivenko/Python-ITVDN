# counter = 11
# if counter < 10:
#     counter += 1
#     print(counter)
# else:
#     counter +=10
#     print(counter)
#-------------------------------------------------

# temperature = 10
# if temperature >= 10:
#     print('На дворі тепло')
# else:
#     print('На дворі холодно')
# #------------------------------------------------
# animal = input('Вкажіть назву тварини')
#
# print(animal)
# if animal == 'cat':
#     print('Meo')
# elif animal == 'dog':
#     print('Wof')
# elif animal == 'bee':
#     print('Dzzz')
# else:
#     print('I don`t  know this animal')
#-------------------------------------------------
#------------------------------------------------- if     elif    else
# user_name = input('Введіть логін \n')
# user_age = int(input('Введіть ваш вік \n'))
#
# if user_name == 'Mark':
#     print('Hello Mark вітаю у вашому кабінеті')
# elif user_age >= 21:
#     print('Your age is more then 21')
# elif user_name == 'Ivan':
#     print('Hello Ivan вітаю у вашому кабінеті')
# else:
#     print(f'Hello {user_name} чи бажаєте зареєструватись ?')


# ------------------------------------------------and    or
# user_login = 'Ivan'
# user_name = input('Введіть логін \n')
# user_age = int(input('Введіть ваш вік \n'))
#
# if user_name == user_login and user_age >= 18:
#     print(f'Hello {user_name} вітаю у вашому кабінеті')
# elif user_age < 18:
#     print(f'Hello {user_name} ваш вік не дозволяє вам зареєструватись ')
# else:
#     print(f'Користувача {user_name} не знайдено у списку користувачів ')

# ---------------------------------------------------------------------------------- len
# user_name = input('Введіть логін \n')
# user_name_len = len(user_name)
# if user_name_len <= 10:
#     print(f'Welcome {user_name}')
# else:
#     print('Ви ввели ім\'я що більше 10 символів',)


#-------------------------------------------------Тернарні оператори
# a = 1
# b = 2
#
# # if a > b:
# #     result = a
# # else:
# #     result = b
# # print('result', result)
#
# result = a if a > b else b # --------------------тернарний оператор
# print('result', result)

# resultbooks = 2
# if books >1:
#     print('You have', books, 'books')
# else:
#     print('You have', books, 'book')
# # -------------------------------------- використаємо скорочений запис
# print('You have', books, ('books' if books > 1 else 'book'))
#-------------------------------------------------------------------------------------------------------------------------------------------

# currency ='грн.'
# costOun = int(input('Введіть сумму товару\n'))
# if costOun >= 100 and costOun < 500:
#     discont = costOun / 100 * 3
#     cost = costOun - discont
#     print('Від вашої суми :', costOun, currency, ' буде відмінусовано ', discont, currency, ' та розраховано суму до оплати :', cost, currency)
#
# elif costOun >= 500 and costOun < 1000:
#     discont = costOun / 100 * 5
#     cost = costOun - discont
#     print('Від вашої суми :', costOun, currency, ' буде відмінусовано ', discont, currency, ' та розраховано суму до оплати :', cost, currency)
#
# elif costOun >= 1000:
#     discont = costOun / 100 * 10
#     cost = costOun - discont
#     print('Від вашої суми :', costOun, currency, ' буде відмінусовано ', discont, currency, ' та розраховано суму до оплати :', cost, currency)
# else:
#     print('Радимо вам збільшити суму придбань хоча б  до 100', currency,'для отримання знижки')
#------------------------------------------------------------------------------------------------------------------------------------------------
#
# line = input('any line')
#
# if line == '':
#     print(None)
# else:
#     print(line)

# ---------------------------------------------------------------


# line = input('any line')
#
# if bool(line):
#     print(line)
# else:
#     print(None)

# ---------------------------------------------------- None - нічого

# line = input('any line')
#
# if line:
#     print(line)
# else:
#     print(None)
#
# # --------------------------------------------------ternarhy operator

line = input('any line \n')
# print(line if bool(line) else None)
print(line if line else None)












