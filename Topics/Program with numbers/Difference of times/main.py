# put your python code here
megan_time = 0
megan_time += 60 * 60 * int(input())
megan_time += 60 * int(input())
megan_time += int(input())

rain_time = 0
rain_time += 60 * 60 * int(input())
rain_time += 60 * int(input())
rain_time += int(input())
print(rain_time - megan_time)
