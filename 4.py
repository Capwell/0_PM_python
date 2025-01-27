test_number = 262144
suspect_greatest_divisor = test_number - 1
print(test_number % suspect_greatest_divisor)
suspect_greatest_divisor = test_number - 2
print(test_number % suspect_greatest_divisor)
# И так 262143 раза, если нам не повезёт
