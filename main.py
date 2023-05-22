
# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

count = int(input('Введите трехзначное число: '))
count2 = count % 10
count = count // 10
count1 = count % 10
count = count // 10
print (count, ' + ', count1, ' + ', count2, ' = ', count + count1 + count2)