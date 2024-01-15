# listOun = [1,2,3,4,5,6]
# print(listOun)
#
# listTwo = []
# print(listTwo)
#
# listThry = list('amsterdam')
# print(listThry)
#
# listFour = list()
# print(listFour)
#
# listfive = ['Ivan', 'David', 'Robert', 'Viktor', 'Olexandr']
# print(listfive[4])
# print(len(listfive))
# print(listfive[len(listfive)-1])
# print(listfive[-1])
# print(id(listfive))
#
# print(listfive)
# #------------------------------------------------- segment list
# print(listfive[1::2])

#----------------------------------------------- Методи списків -----------------------
# print(help([]))
# print(dir(list))

#-------------------------------------------------- append() ------- додаємо у кінець списку
shopping_list = []
shopping_list.append('banana')
shopping_list.append('Orange')
shopping_list.append('apple')
shopping_list.append('milk')
shopping_list.append('egs')

print(shopping_list)
shopping_list_complit = []
for i in shopping_list:
    shopping_list_complit.append(i)
print(shopping_list_complit)
#------------------------------------------------- clear() ----------- очищаємо список
shopping_list_complit.clear()
print(shopping_list_complit)

#------------------------------------------------extend() ------------ додаємо до одного списка інший список (приклеює)
list_number_oun = [1, 2, 3, 4, 5]
list_number_two = [1, 3, 5, 6, 7, 8]

list_number_oun.extend(list_number_two)

print(list_number_oun)
#------------------------------------------------index() ------------ шукаємо індекс вказанного елемента
print(list_number_oun.index(8))

print(shopping_list.index('milk'))
#------------------------------------------------pop() ------------- видаляє останній елемент списку (можемо його отримати)
print(shopping_list)
last_element = shopping_list.pop()
print(last_element)
print(shopping_list)
dell_element = shopping_list.pop(1) # - вказуємо індекс елементу, що хочемо видалити
print(dell_element)
print(shopping_list)
#---------------------------------------------reverse()------------- дзеркально перевертає список
print('----------------------------------------reverse()')
shopping_list.reverse()
print(shopping_list)
#---------------------------------------------sort()----------------сортуємо список
print('------------------------------------------- sort()')
data_list = [1, 2, 3, 4, 6, 10, 12, 17, 21, 14, 15, 18]
data_list.sort()
print(data_list)
data_list.sort(reverse=True)
print(data_list)
print('---------------------------------------------')
words = ['Ivan', 'Mykola', 'Oleg', 'Viktor', 'Sergiy']
print(words)
words.sort()
print(words)
words.reverse()
print(words)
words.reverse()
words.sort()
print(words)
words.sort(reverse=True)
print(words)
#----------------------------------------for in list
print('------------------------------------')
for i in words:
    print(i)
#----------------------------------------
print("-----------------------------------")
words.sort(reverse=True)

for i in words:
    print(i)
#----------------------------------------
print("-----------------------------------")

words.sort(reverse=True)
counter=1
for i in words:
    print(f'{counter} : {i}')
    counter +=1
#-----------------------------------------------------
print('------------------------------------')
list_telefones = [1123, 3232, 4444, 8888]
for i in list_telefones:
    print(f'+{i}')
print('-----------------------------')
index= 0
while True:
        if index == len(list_telefones):
            break
        else:
            print(f'{list_telefones[index]}')
        index += 1
#-----------------------------------------------------
print('--------------------------------------')
#-------------------------------Видяляємо всі парні елементи списку
data_listTwo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(data_listTwo)
for i in data_listTwo:
    if i % 2 == 0:
        currentIndex = data_listTwo.index(i)
        # data_listTwo.pop(currentIndex)
        data_listTwo.remove(currentIndex)
        print(f'видаляємо : {i} ')
print(data_listTwo)
# -------------------------------- Підносимо всі елементи списку до степені 2
print('-----------------------------------------------------')
data_listThree = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(data_listThree)
data_listFour = []
for i in data_listThree:
    i = i ** 2
    data_listFour.append(i)
print(data_listFour)
#---------------------------------Знаходимо максиммальний елемент списку
print('-----------------------------------------------------------------')
data_list_five = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i_max = data_list_five[0]
for i in data_list_five:
    if i > i_max:
        i_max = i
print('i_max var 1:', i_max)
print('-----------------------------------------------------------------')
print('i_max var 2:',max(data_list_five))
print('------------------------------------------------------')
#------------------------------------------------------ copy() ------------------копіюємо список
data_list_six = data_list_five.copy()
print(data_list_six)
print("------------------------------------------------------------")
# -------------------------------- Підносимо всі елементи списку до степені 3
for i in range(len(data_list_six)):
    data_list_six[i] = data_list_six[i] ** 3
print(data_list_six)
print('-------------------------------------------------------------')

