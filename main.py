import time

num = 1
while True:
    sqrt = num ** 0.5
    count = 0
    for i in range(2, int(sqrt + 1)):
        div = num / i
        if div.is_integer():
            count += 1
    if count == 0:
        print(num)
    num += 1
    time.sleep(0.5)