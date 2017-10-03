decimals = list([p/10 for p in range(0, 10)])

for number in decimals:
    print(1 / (number + 0.0000000001))