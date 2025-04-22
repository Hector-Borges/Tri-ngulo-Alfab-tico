n = int(input())
repeat = 1
x = 0

if 1 <= n <= 26:
    while repeat != n + 1:
        letra = chr(65 + x)
        print(letra * repeat)
        x += 1
        repeat += 1