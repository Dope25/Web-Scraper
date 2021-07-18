# put your python code here
three_digit = int(input())
first = three_digit // 100
three_digit %= 100
second = three_digit // 10
three_digit %= 10
third = three_digit
print(first + second + third)
