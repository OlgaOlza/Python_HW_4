# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во 
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = (int(input("Введите число n элементов: ")))
count_list_n = []
for i in range(n):
    num = int(input("Введите число: "))
    count_list_n.append(num)
print(count_list_n)

m = (int(input("Введите число m элементов: ")))
count_list_m = []
for i in range(m):
    num = int(input("Введите число: "))
    count_list_m.append(num)
print(count_list_m)

count_list3 = count_list_n + count_list_m

print(count_list3)
for i in count_list3:
    if count_list3.count(i) > 1:
        print(i)