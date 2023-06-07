number = int(input("Введите колличество кустов = "))
my_list = []
for temp in range(number):
    my_list.append(int(input("Введите колличество ягод на одном кусте = ")))
print(my_list)
new_list = []
for temp in range(len(my_list) - 1):
    new_list.append(my_list[temp] + my_list[temp-1] + my_list[temp-2])
print(new_list)
print(max(new_list))