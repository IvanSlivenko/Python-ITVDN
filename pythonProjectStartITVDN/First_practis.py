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




# # Корисні функції пр роботі з числами
#
#
# #---------------------------
# #Додаємо знаки після коми
#
# num = 1
# numFloat = float(1)
#
# print("numFloat", numFloat)
# #--------------------------
# #-Позбавляемось (обрізаємо) знаків після коми
# numInt = int(numFloat)
# print("numInt", numInt)
#
#
# #---------------------------
# absolute_n = abs(-5)
# print("absolute_n", absolute_n)
# #--------------------------
#
# rounden_n1: int = round(4.2312121)
# print("rounden_n1", rounden_n1)
#
# rounden_n2: int = round(4.2312121, 2)
# print("rounden_n2", rounden_n2)
#
# #--------------------------------------------
# #--Округляємо до вказаної кількісті знаків після коми
# prise = 7.25545
# prise2 = round(prise, 2)
# print('prise2', prise2)
