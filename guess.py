import random

start = input('請決定隨機數字的開始值')
end = input('請決定隨機數字的結束值')
start = int(start)
end = int(end)

r = random.randint(start,end)
count = 0
while True:
    count += 1
    num = input('請猜數字:')
    num = int(num)
    if num == r:
        print('你猜中了')
        print('這是你猜的第',count,'幾次')
        break
    elif num > r:
        print('猜小一點')
    else:
        print('猜大一點')
    print('這是你猜的第',count,'幾次')