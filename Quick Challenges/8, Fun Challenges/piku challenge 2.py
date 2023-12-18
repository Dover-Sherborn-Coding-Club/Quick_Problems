def colat(n):
    i = 0
    while True:
        if n % 2 == 0:
            n = n / 2
            i+=1
        else:
            n = n*3 + 1
            i+=1
        if n == 1:
            print(i)
            break
colat(int(input("num?\n")))
