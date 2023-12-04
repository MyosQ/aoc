from utils import get_input_file_path, print_intro

def parse_cards(f):
    cards = []
    for line in f:
        card = {}
        id, nums = line.split(":")
        winning, numbers = nums.split("|")
        id, winning, numbers = ' '.join(id.split()), ' '.join(winning.split()), ' '.join(numbers.split())
        card["id"] = int(id.split(" ")[1])
        card["winning"] = set([int(n) for n in winning.strip().split(" ")])
        card["numbers"] = set([int(n) for n in numbers.strip().split(" ")])
        cards.append(card)
    return cards

def first():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        cards = parse_cards(f)
        sum = 0
        for card in cards:
            intersection = card["winning"].intersection(card["numbers"])
            if len(intersection) > 0:
                sum += 2**(len(intersection)-1)

    print(sum)

def second():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        ...

if __name__ == '__main__':
    first()
    # second()
