number_dec = int(input())
while number_dec > 0:
    remainder = number_dec % 5
    number_dec //= 5
print(remainder)
