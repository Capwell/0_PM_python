def greatest_divisor(testing_number):
    suspect_greatest_divisor = testing_number - 1
    while suspect_greatest_divisor > 1:
        if testing_number % suspect_greatest_divisor == 0:
            return suspect_greatest_divisor
        suspect_greatest_divisor = suspect_greatest_divisor - 1


assert greatest_divisor(262144) == 131072, "не работает на числе 262144"
