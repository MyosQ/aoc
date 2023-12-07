from utils import get_input_file_path, print_intro

def parse_input_compute_hands(f):
    l = []
    for line in f:
        hand, bid = line.strip().split()
        type, type_rank = get_hand_type(hand)
        card_values = get_card_values(hand)
        l.append((hand, int(bid), type, type_rank, card_values))
    return l

def get_hand_type(hand):
    if len(set(hand)) == 1:
        return "five of a kind", 7
    
    for card in set(hand):
        if hand.count(card) == 4:
            return "four of a kind", 6
    
    if len(set(hand)) == 2:
        return "full house", 5
    
    for card in set(hand):
        if hand.count(card) == 3:
            return "three of a kind", 4
        
    if len(set(hand)) == 3:
        return "two pairs", 3
    
    for card in set(hand):
        if hand.count(card) == 2:
            return "one pair", 2
        
    return "high card", 1

def get_card_values(hand):
    card_values = []
    for card in hand:
        if card == "T":
            card_values.append(10)
        elif card == "J":
            card_values.append(11)
        elif card == "Q":
            card_values.append(12)
        elif card == "K":
            card_values.append(13)
        elif card == "A":
            card_values.append(14)
        else:
            card_values.append(int(card))

    return card_values

def first():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        hands = parse_input_compute_hands(f)
        hands.sort(key=lambda x: (x[3], x[4]))
        print(sum([x[1]*(i+1) for i, x in enumerate(hands)]))


def second():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        ...

if __name__ == '__main__':
    first()
    # second()
