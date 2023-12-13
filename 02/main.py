
with open('input.txt') as f:
    data = f.read().strip()

test_data = '''
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''.strip()

red = 12
green = 13
blue = 14


def main():
    global data, red, green, blue

    games = {}
    n = 0

    for line in data.split('\n'):
        if line:
            game, results = line.split(':')
            game = int(game.strip().split(' ')[1])
            games[game] = [a.strip() for a in results.split(';')]

    for game in games:
        results = games[game]
        games[game] = []
        for result in results:
            if result:
                r = {}
                a = [s.strip() for s in result.split(',')]
                for x in a:
                    if 'red' in x:
                        r['red'] = int(x.split(' ')[0])
                    elif 'green' in x:
                        r['green'] = int(x.split(' ')[0])
                    elif 'blue' in x:
                        r['blue'] = int(x.split(' ')[0])
                games[game].append(r)
        possible = True
        for r in games[game]:
            if 'red' not in r:
                r['red'] = 0
            if 'green' not in r:
                r['green'] = 0
            if 'blue' not in r:
                r['blue'] = 0

            if r['red'] > red or r['green'] > green or r['blue'] > blue:
                possible = False
        if possible:
            n += game

    t = 0
    for game in games:
        max_red = 0
        max_green = 0
        max_blue = 0
        results = games[game]
        for r in results:
            if r['red'] > max_red:
                max_red = r['red']
            if r['green'] > max_green:
                max_green = r['green']
            if r['blue'] > max_blue:
                max_blue = r['blue']

        m = max_red * max_green * max_blue
        t += m
    print(t)


if __name__ == '__main__':
    main()
