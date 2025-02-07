# Выносим в переменную
testing_number = 262144
suspect_greatest_divisor = testing_number - 1

while suspect_greatest_divisor > 1:
    if testing_number % suspect_greatest_divisor == 0:
        print(suspect_greatest_divisor)
        break
    suspect_greatest_divisor = suspect_greatest_divisor - 1
