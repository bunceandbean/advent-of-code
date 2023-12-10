with open("input.txt") as f:
    content = [x.split(" ") for x in f.read().split("\n")[:~0]]
    hands = [(x[0], int(x[1])) for x in content]

card_priority = list(reversed(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]))
card_priority_J = list(reversed(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]))

def get_type(hand: str):
    set_hand = set(hand)
    if len(set_hand) == 1:
        return 6
    elif len(set_hand) == 2:
        if hand.count(hand[0]) in (1,4):
            return 5
        return 4
    elif len(set_hand) == 3:
        if hand.count(hand[0]) == 2 or hand.count(hand[1]) == 2:
            return 2
        return 3
    elif len(set_hand) == 4:
        return 1
    return 0

def type_sort(arr: list, card_priority: list):
    sorted_arr = arr
    for i in range(4,-1,-1):
        sorted_arr.sort(key=lambda x: card_priority.index(x[0][i]))
    return sorted_arr

def joker_type(hand: str):
    hand_set = set(hand)
    best_type = -1
    for ch in hand_set:
        if ch != 'J':
            j_hand = hand.replace('J', ch)
            if (num := get_type(j_hand)) > best_type:
                best_type = num
    return best_type

def day07(part2: bool, card_priority: list):
    types = [list() for _ in range(7)]

    for hand in hands:
        if part2:
            types[joker_type(hand[0])].append(hand)
        else:
            types[get_type(hand[0])].append(hand)

    rank = 1
    total = 0
    for type in types:
        sorted_type = type_sort(type, card_priority)
        while sorted_type:
            total += sorted_type.pop(0)[1] * rank
            rank += 1
    return total

print("p1:", day07(False, card_priority))
print("p2:", day07(True, card_priority_J))

