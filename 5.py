suspect_greatest_divisor = 262144 - 1
if 262144 % suspect_greatest_divisor == 0:
    print(suspect_greatest_divisor)
suspect_greatest_divisor = 262144 - 2
if 262144 % suspect_greatest_divisor == 0:
    print(suspect_greatest_divisor)
# И так 262143 раза, если нам не повезёт
# Есть повторяемые кусочки кода
