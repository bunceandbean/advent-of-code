answer = 0
# Open file and compress lines into an array
with open("input.txt") as f:
    content = f.read()

def day12(inp):
    lines = inp.splitlines()
    lines = [(l[0], int(l[1:])) for l in lines]

    p = 0+0j
    f = 1+0j
    for d,n in lines:
        ds = {'N':1j,'S':-1j,'W':-1,'E':1,'F':f}
        if d == 'L':
            f *= 1j ** (n//90)
        elif d=='R':
            f *= 1j ** (-n//90)
        else:
            p += ds[d]*n

    print('p1:', abs(p.imag)+abs(p.real))

    w = 10+1j
    p = 0+0j
    for d,n in lines:
        ds = {'N':1j,'S':-1j,'W':-1,'E':1}
        if d =='F':
            p += w * n
        elif d == 'L':
            w *= 1j ** (n//90)
        elif d=='R':
            w *= 1j ** (-n//90)
        else:
            w += ds[d]*n

    print('p2:', abs(p.imag)+abs(p.real))

    return
day12(content)
