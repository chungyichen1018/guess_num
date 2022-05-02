import random
r = random.randint(1,100)
count = 0
while True:
    count += 1
    num = input('請猜數字:')
    num = int(num)
    if num == r:
        print('你猜中了')
        break
    elif num > r:
        print('猜小一點')
    else:
        print('猜大一點')
    print('這是你猜的第',count,'幾次')