(x1, y1,) =map(int, input().split())
(x2, y2) = map(int, input().split())


color1 = (x1 + y1) % 2 == 0
color2 = (x2 + y2) % 2 == 0

if color1 == color2:
    print("YES");
    print("White" if color1 else "Black");
else:
    print("NO")