import random
my_list = []
num = random.randint(1, 1000)
print(num)
my_list = [random.randint(1, 1000000) for _ in range(num)]
print(my_list)
for temp in my_list:
    count = 0
    for a in range(2, temp):
        if temp % a == 0:
            count += 1
    print(f'У числа {temp} делителей {count}')
