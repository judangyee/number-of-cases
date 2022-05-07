a=0
b=0
c=0
d=0
e=0
f=0
t=0

for i0 in range(5):
    a += 1
    for i1 in range(5):
        b += 1
        for i2 in range(5):
            c += 1
            for i3 in range(5):
                d += 1
                for i4 in range(5):
                    e += 1
                    print("a=" + str(a) + " b=" + str(b) + " c=" + str(c) + " d=" + str(d) + " e=" + str(e))
                    if a==b or a==c or a==d or a==e or b==c or c==d or d==e:
                        f += 1
                    else:
                        t += 1
                e = 0
            d = 0
            e = 0
        c = 0
        d = 0
        e = 0
    b = 0
    c = 0
    d = 0
    e = 0

print("t=" + str(t) + " f=" + str(f))
print("전체 경우의 수: " + str(t+f) + "\n조건과 일치하는 경우의 수: " + str(t))
print("답: " + str(t))
