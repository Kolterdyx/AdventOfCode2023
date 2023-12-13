

with open('input.txt') as f:
    data = f.read().strip()

test_data = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip()


gears = {}


def check_around(x, y, engine):
    global gears
    kernel = [
        (-1, -1), (0, -1), (1, -1),
        (-1,  0), (0,  0), (1,  0),
        (-1,  1), (0,  1), (1,  1),
    ]
    res = (False, None)
    for k in kernel:
        x_ = x + k[0]
        y_ = y + k[1]
        c = engine[min(max(y_, 0), len(engine)-1)][min(max(x_, 0), len(engine[0])-1)]
        if c == '*':
            gears[(x_, y_)] = [] if (x_, y_) not in gears else gears[(x_, y_)]
            return True, (x_, y_)
        elif not c.isdigit() and c != '.':
            res = (True, None)
    return res


def extract_num(x, y, engine):
    global gears
    # Keep walking x until no longer digit:
    s = ''
    c = engine[y][x]
    fs = False
    gear = None
    while c.isdigit() and x < len(engine[0]):
        if not fs:
            fs, gear = check_around(x, y, engine)
        s += c
        x += 1
        if x >= len(engine[0]):
            break
        c = engine[y][x]
    if fs and gear:
        gears[gear].append(int(s))
    return (int(s), x) if fs else (0, x)


def main():
    global gears
    engine = [list(l) for l in data.split('\n')]
    n = 0
    for y in range(len(engine)):
        x = 0
        while x < len(engine[0]):
            c = engine[y][x]
            a = 0
            if c.isdigit():
                a, x = extract_num(x, y, engine)
            x += 1

    for gear in gears.values():
        if len(gear) == 2:
            n += gear[0] * gear[1]

    print(n)


if __name__ == '__main__':
    main()
