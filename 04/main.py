
with open('input.txt') as f:
    data = f.read().strip()

test_data = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip()


def sanitize(string):
    res = string
    while "  " in res:
        res = res.replace("  ", " ")
    return res


def main():
    global data, test_data
    cards = {}
    n = 0
    d = sanitize(data)
    for line in d.split('\n'):
        card_name, nums = [l.strip() for l in line.split(':')]
        _, card_id = [l.strip() for l in card_name.split(' ')]
        card_id = int(card_id)
        cards[card_id] = {}
        winning_set, number_set = (set(l.strip().split(' ')) for l in nums.split('|'))
        cards[card_id]['ws'] = winning_set
        cards[card_id]['ns'] = number_set
        inter = winning_set.intersection(number_set)
        cards[card_id]['p'] = len(inter)
        cards[card_id]['c'] = 1

    for cid, card in cards.items():
        if card['p']:
            for x in range(card['c']):
                for i in range(cid + 1, cid + card['p'] + 1):
                    cards[i]['c'] += 1
    for card in cards.values():
        n += card['c']

    print(n)


if __name__ == '__main__':
    main()
