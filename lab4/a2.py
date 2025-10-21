
def rect(rows, cols, ch):
    for i in range(rows):
        for j in range(cols):
            print(ch, end="")
        print()

def triangle(n, ch):
    for i in range(1, n + 1):
        print(ch * i)

def frame(rows, cols, ch):
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows-1 or j == 0 or j == cols-1:
                print(ch, end="")
            else:
                print(" ", end="")
        print()

n = int(input("Строки: "))
m = int(input("Столбцы: "))
ch = input("Символ: ") or "#"

print("\nПрямоугольник:")
rect(n, m, ch)

print("\nТреугольник:")
triangle(n, ch)

print("\nРамка:")
frame(n, m, ch)