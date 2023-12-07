from utils import get_input_file_path, print_intro

def parse_input_compute_hands(f: list, part: int=1) -> list[tuple]:
    list_of_hands = []
    for line in f:
        hand, bid = line.strip().split()
        type, type_rank = get_hand_type_part2(hand) if part == 2 else get_hand_type(hand)
        card_values = get_card_values(hand, part)
        list_of_hands.append((hand, int(bid), type, type_rank, card_values))
    return list_of_hands

def get_hand_type(hand: str) -> tuple[str, int]:
    if len(set(hand)) == 1 and len(hand) == 5:
        return "five of a kind", 7
    
    for card in set(hand):
        if hand.count(card) == 4:
            return "four of a kind", 6
    
    if len(set(hand)) == 2 and len(hand) == 5:
        return "full house", 5
    
    for card in set(hand):
        if hand.count(card) == 3:
            return "three of a kind", 4
        
    if (len(set(hand)) == 3 and len(hand) == 5) or (len(set(hand)) == 2 and len(hand) == 4):
        return "two pairs", 3
    
    for card in set(hand):
        if hand.count(card) == 2:
            return "one pair", 2
        
    if len(hand) > 0:
        return "high card", 1
    
    return "empty", 0

def upgrade_hand_type(hand_type: str) -> tuple[str, int]:
    if hand_type == "empty":
        return "high card", 1
    elif hand_type == "high card":
        return "one pair", 2
    elif hand_type == "one pair":
        return "three of a kind", 4
    elif hand_type == "two pairs":
        return "full house", 5
    elif hand_type == "three of a kind":
        return "four of a kind", 6
    elif hand_type == "four of a kind":
        return "five of a kind", 7
    else:
        raise Exception(f"Invalid hand type to be upgraded: {hand_type}")

def get_hand_type_part2(hand):
    num_jacks, hand_without_jacks = hand.count("J"), hand.replace("J", "")
    base_hand_type, base_hand_rank  = get_hand_type(hand_without_jacks)
    for _ in range(num_jacks):
        base_hand_type, base_hand_rank = upgrade_hand_type(base_hand_type)

    return base_hand_type, base_hand_rank


def get_card_values(hand: str, part: int=1) -> list:
    mapping = {"T": 10, "J": 11 if part == 1 else 1, "Q": 12, "K": 13, "A": 14}
    return [mapping[card] if card in mapping else int(card) for card in hand]

def first():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        hands = parse_input_compute_hands(f)
        hands.sort(key=lambda x: (x[3], x[4]))
        print(sum([x[1]*(i+1) for i, x in enumerate(hands)]))


def second():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        hands = parse_input_compute_hands(f, part=2)
        hands.sort(key=lambda x: (x[3], x[4]))
        print(sum([x[1]*(i+1) for i, x in enumerate(hands)]))

if __name__ == '__main__':
    first()
    second()
