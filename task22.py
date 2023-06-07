#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во 
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
from random import randint
number_1 = int(input("Введите колличество чисел 1 множества = "))
number_2 = int(input("Введите колличество чисел 2 множества = "))
one_list = [randint(10, 30) for _ in range(number_1)]
two_list = [randint(10, 30) for _ in range(number_2)]
new_list = []
for item in one_list:
    for temp in two_list:
        if item == temp:
            new_list.append(item)
print(sorted(set(new_list)))


