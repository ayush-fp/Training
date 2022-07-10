def round_off(num):
    round = int(num-0.5) + 1
    return round

num = float(input("Enter a single decimal number: "))
print("Round off: ", round_off(num))