import sys
# numbers - последовательность чисел полученная от пользователя #3 6 5 2 4 1
# digit - число полученное от пользователя

numbers = list(map(int,input("Введите числа через пробел \n").split()))
print(numbers)

def sort_number(a):                 #Функция сортировки
    for i in range(1, len(a)):
        x = a[i]
        idx = i
        while idx > 0 and a[idx-1] > x:
            a[idx] = a[idx-1]
            idx -= 1
        a[idx] = x
    return a


sort_number(numbers)
print(numbers)                  #отсортированный список

digit = int(input("Введите число \n"))
print(digit)

def control_digit(a): #проверка переменной digit 
    count = 0
    for d in a:
        if d != digit:
            count += 1
    if count == len(a):
        print("Число которое Вы ввели отсутствует в последовательности")
        sys.exit()  # Для завершения программы
    else:
        pass
control_digit(numbers)

def search(numbers, digit, left, right):
    # if left > right: # если левая граница превысила правую,
    #     return False # значит элемент отсутствует

    middle = (right+left) // 2 # находим середину
    if numbers[middle] == digit: # если элемент в середине,
        if digit == numbers[0]:
            return str(digit) + " - самое маленькое число в последовательности", str(numbers.index(digit + 1)) + " - индекс числа больше"
        elif digit == numbers[-1]:
            return str(digit) + " - самое большое число в последовательности", str(numbers.index(digit - 1)) + " - индекс числа меньше"
        return str(middle -1) + " - индекс числа меньше ",str(middle + 1) + " - индекс числа больше " # возвращаем этот индекс
         # print("индекс числа меньше" + str(middle -1), "Индекс числа больше" + str(middle +1))
    elif digit < numbers[middle]: # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return search(numbers, digit, left, middle-1)

    else: # иначе в правой
        return search(numbers, digit, middle+1, right)

print(search(numbers, digit,numbers[0],numbers[-1]))

