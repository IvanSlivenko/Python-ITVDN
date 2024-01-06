# name = 'Ivan'
# print('Hello', 'Ivan', 'Slivenko')
# print('Hello', name, 'Slivenko')
# print("\n")
# name = 'Anna'
# print('Hello', 'Anna', 'Slivenko')
# print('Hello', name, 'Slivenko')
# print("\n")

# from keyword import kwlist
# for i in kwlist:
#     print(i)
# # -----------------Знаходимо унікальний ідентифікатор  перебування змінної
# name = 'Mark'
# print(id(name))
#
# #------------------------ Шукаємо інформацію про методи
# help(print)
#
# # //////////////////////// Рядки ////////////////////

# ------------------------------------------------------------Послідовні рядки склеюються
text_1 = 'python'
text_2 = 'developer'
text_3 = "I am " + text_1 + " " + text_2
print(text_3)

#-------------------------------------------------------------- Повторення рядків
repeid_text='a'
res_text=repeid_text*10
print(res_text)

#---------------------------------------------------------------Довжина рядка
text_4 = "developer"
print("text_4:", text_4)
LenText_4 = len(text_4)
print("LenText_4", LenText_4)

#--------------------------------------------------------------Зміна регістрів
text_5 = "developer"
print("text_5:", text_5)
Lower_text_5 = text_5.lower()
print("Lower_text_5:",Lower_text_5)

Upper_text_5 = text_5.upper()
print("Upper_text_5:",Upper_text_5)

Capitalize_text_5 = text_5.capitalize()
print("Capitalize_text_5:",Capitalize_text_5 )

#---------------------------------------------------------- Екранування

# \t - символ горизонтальної табуляції
# \n - символ переноса  строки
# \ -  екранування символів

text_6 = 'Ivan, Віктор, Олександр'
print("text_6:", text_6)

text_7 = "Ivan, \t Віктор, \t Олександр"
print("text_7:", text_7)

text_8 = "Іван,\n Віктор,\n Олександр"
print("text_8:", text_8)

text_9 = " \"Іван\", \"Віктор\", \"Олександр\" "
print("text_9:", text_9)

#----------------------------------------------------------Сирі рядки

print(r'https://docs.python.org/3/library/functions.html#id') # r'

#----------------------------------------------------------- Робота з Юнікодом
text_10 = ord('a') # переводимо в юнікод
print('text_10:', text_10)

text_11 = chr(97) # переводимо з юнікода
print("text_11", text_11)

text_12 = "test"
print("text_12", text_12)
print("text_12.title()",text_12.title())
print("text_12.count('t'):", text_12.count('t'))
#--------------------------------------------------------- Пошук та заміна
print("text_12:", text_12)
print("text_12.replace('x','s'):", text_12.replace('x','s'))

#------------------------------------------------------------Методи вирівнювання
text_13 = "test21"
print("text_13:", text_13)
print(text_13.ljust(20,"#"))
print(text_13.rjust(20,"#"))
print(text_13.center(20,"#"))

# ----------------------------------------------------------Методи видалення
text_14 = "########test_22"
print("text_14", text_14)
print(text_14.lstrip("#"))

text_15 = "test_23############"
print("text_15:", text_15)
print(text_15.rstrip('#'))

# -------------------------------------------------------- Методи розділення
text_16 = "file.name.zip"
print("text_16:", text_16)
print(text_16.rsplit('.',1))
print(text_16.rsplit('.',1)[0])
print(text_16.partition('.'))
print(text_16.rpartition('.'))

#--------------------------------------------------------- Метод join з'єднує елементи списку через розділювач
res_1 = "--".join([text_14, text_15, text_16])
print("res_1:", res_1)

# --------------------------------------------------------- Пошук підрядка
text_17 = "Один два три чотири п'ять шість сім вісім дев'ять десять"
res_2 = text_17.find('три')
print("res_2", res_2) # --Отримуємо індекс знайденого рядка

name = 'Ivan'
surname = 'Slivenko'
age = 42

# var 1
print('Hello dear %s %s your age is %d' % (name, surname, age))

# var 2
print('Hello dear {0} {1} your age is {2}'.format(name, surname, age))

# var 3
print(f"Hello dear {name} {surname} your age is {age}")




# ---------------------------------------------------------Корисні функції пр роботі з числами
res_3 = 5/2 # --------------Ділення з остачею
print('res_3', res_3)
res_4 = 5 // 2 #------------Ділення без остачі
print('res_4', res_4)
res_5 = 5 % 2 # ------------Обчислення остачі
print('res_5', res_5)

#---------------------------------------------------------Float

res_6 = 0.4 + 0.2
print('res_6', res_6)
print('res_6', round(res_6, 2))

# #---------------------------
#Додаємо знаки після коми

num = 1
print("num", num)
numFloat = float(1)

print("numFloat", numFloat)
#--------------------------
#-Позбавляемось (обрізаємо) знаків після коми
numInt = int(numFloat)
print("numInt", numInt)


#---------------------------
absolute_n = abs(-5)
print("absolute_n", absolute_n)

#-------------------------- Округляємо до вказаної кількісті знаків після коми
n_1 = 4.2312121
print("n_1 : ",n_1)
rounden_n_1 = round(n_1)
print("rounden_n_1 :", rounden_n_1)

rounden_n_1_2 = round(4.2312121, 2)
print("rounden_n_1_2 :", rounden_n_1_2)

#--------------------------------------------
#--Округляємо до вказаної кількісті знаків після коми
prise = 7.55545
print('prise', prise)
prise_2 = round(prise, 2)
print('prise_2', prise_2)
# --------------------------Обрізаємо до цілого числа ( без округлення)
prise_3 = int(prise)
print('prise_3:', prise_3)
# -------------------------------------------type
i = 1
print('i :', i)
print('type i:', type(i))

f = 1.23
print('f', f)
print('type f:', type(f))

s = 'test_23'
print('s', s)
print('type s:', type(s))

# ------------------------------------------True and False
a = True
print('a :', a)
b = False
print('b:', b)
# -------------------------------------------and (i)
print('a and b :', a and b)
# -------------------------------------------or (або)
print('a or b :', a or b)
print('a or b :', b or a)

# -------------------------------------------not (ні)
print('a and b :', not b)

#------------------------------------------- is ( дорівнює )
#------------------------------------------- is not ( не дорівнює )
print('a is b:', a is b)
print('a is not b:', a is not b)

# --------------------------------------------- in (належить)
print ("ITVDN' in 'Best  inline course is ITVDN:",'ITVDN' in 'Best  inline course is ITVDN')

#----------------------------------------------- not in (не належить)
print ("ITVDN' not in 'Best  inline course is ITVDN:",'ITVDN' not in 'Best  inline course is ITVDN')

