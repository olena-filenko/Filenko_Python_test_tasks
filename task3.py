numbers = input('Введите числа через пробел ').split()
list_3 = []
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
    if numbers[i] % 3 == 0:
        list_3.append(numbers[i])
print('Числа кратные трем:', *list_3, sep=' ')