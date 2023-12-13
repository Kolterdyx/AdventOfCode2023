
with open('input.txt', 'r') as f:
    data = f.read().strip()

num_map = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}


def find_num_name(string, pos):
    global num_map

    for num, name in num_map.items():
        if string[pos:pos+len(name)] == name:
            return num
    return None


def main():
    global data

    data = data.split('\n')
    data = [x.strip() for x in data]
    data = [x for x in data if x != '']

    n = 0
    for string in data:
        num = ''
        for i, c in enumerate(string):
            if c.isdigit():
                num += c
            elif x := find_num_name(string, i):
                num += str(x)
            else:
                continue
        if num != '':
            num = num[0] + num[-1]
            n += int(num)

    print(n)


if __name__ == '__main__':
    main()
