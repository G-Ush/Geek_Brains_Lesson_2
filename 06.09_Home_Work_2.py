import random

'''1. Выяснить тип результата выражений:'''
# print(type(15 * 3))
# print(type(15 / 3))
# print(type(15 // 2))
# print(type(15 ** 2))

'''2. Дан список:'''

first_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
num_index_list = []
empty_list = []
'''Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
и дополнить нулём до двух целочисленных разрядов:'''
for i in first_list:
    if i[0].isdigit():
        num_index_list.append(first_list.index(i))
        first_list[first_list.index(i)] = '{:02d}'.format(int(i))
    elif i[-1].isdigit():
        num_index_list.append(first_list.index(i))
        first_list[first_list.index(i)] = f'{i[:1]}0{i[1:]}'
for numbers in range(len(num_index_list)):
    first_list[num_index_list[numbers]] = ['"'] + first_list[num_index_list[numbers]].split(' ') + ['"']
for el in first_list:
    if isinstance(el, str):
        empty_list.append(el)
    else:
        empty_list.extend(list(el))
# print(empty_list)
'''Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов'''
first_list[:] = [''.join(i) for i in first_list]
# print(' '.join(first_list))

'''4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:

Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида:
'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка, 
как привести их к корректному виду. Можно ли при этом не создавать новый список?'''

worker_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
               'токарь высшего разряда нИКОЛАй', 'директор аэлита']
worker_list[:] = [i.split(' ') for i in worker_list]
for worker in worker_list:
    print(f'Hello, {worker[-1].capitalize()}!')

'''5. Создать список, содержащий цены на товары (10–20 товаров)'''

price_list = [random.randint(1000, 9999) / 100 for i in range(20)]
'''Вывести на экран эти цены через запятую в одну строку, 
цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).'''
price_list[:] = [str(i).split('.') for i in price_list]
new_list = []
for el in range(len(price_list)):
    new_list.append('{:0>2} руб {:0>2} коп'.format(price_list[el][0], price_list[el][1]))
# print(', '.join(new_list))
'''Вывести цены, отсортированные по возрастанию, новый список не создавать
(доказать, что объект списка после сортировки остался тот же).'''
# print(id(new_list))
new_list.sort()
# print(new_list, id(new_list))
'''Создать новый список, содержащий те же цены, но отсортированные по убыванию.'''
new_list_s = sorted(new_list, reverse=True)
# print(new_list_s, id(new_list_s))
'''Вывести цены пяти самых дорогих товаров. 
Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?'''
# print(sorted(new_list_s[0:5]))
