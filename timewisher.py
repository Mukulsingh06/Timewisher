import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp1 = int(time.strftime('%H'))
print(timestamp1)
timestamp2 = int(time.strftime('%M'))
print(timestamp2)
timestamp3 = int(time.strftime('%S'))
print(timestamp3)
if timestamp1 < 12 and timestamp1 > 6:
    print("Good Morning")
elif timestamp1 == 12:
    if timestamp2 > 0:
        print(" Good Afternoon")
elif timestamp1 > 12 and timestamp1 < 16:
    print("Good Afternoon")
elif timestamp1 > 16 and timestamp1 < 20:
    print("Good Evening")
else:
    print("Good Night")