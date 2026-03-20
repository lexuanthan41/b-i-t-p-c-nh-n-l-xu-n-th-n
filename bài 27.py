n = int(input("Nhap n: "))

i = 2
while i * i <= n:
    while n % i == 0:
        print(i, end="")
        n //= i
        if n > 1:
            print(" * ", end="")
    i += 1

if n > 1:
    print(n, end="")
