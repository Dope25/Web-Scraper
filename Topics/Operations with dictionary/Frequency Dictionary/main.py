# put your python code here

words = input().lower().split()
# words = 'a aa abC aa ac abc bcd a'.lower().split()
result = {word: words.count(word) for word in words}
for key, value in result.items():
    print(key, value)
