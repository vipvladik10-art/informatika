numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers_without_None = numbers[:4]+numbers[5:] #Создаём новый список, без индекса - 4, с помощью суммы 2-x срезов
sum_numbers_without_None = sum(numbers_without_None) #Находим сумму значений нового список
len_numbers = len(numbers) #Находим количество элементов в спике, который был предоставлен для задачи
average = sum_numbers_without_None/len_numbers #Находим среднее
numbers[4] = average #Заменяем 4 индекс в списке на среднее значение
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
