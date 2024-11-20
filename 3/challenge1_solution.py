import random


def gen_random(min_val, max_val):
    """Geerates a random number between min_val and max_val inclusive"""
    r = max_val - min_val + 1
    x = random.randrange(r) + min_val
    return x

def check_duplicate(my_list, val):
    """Checks to see if val is present in my_list, Returns True if present"""
    x = 0
    while x < len(my_list):
        if my_list[x] == val:
            return True
        else:
            x += 1
    return False

def generate_ticket():
    """Generate a sorted list with 6 elements in the range 1 to 50 inclusive"""
    my_list = []
    while len(my_list) < 6:
        x = gen_random(1, 50)
        if check_duplicate(my_list, x) is False:
            my_list.append(x)
    # Sort the list...
    my_list.sort(reverse=False)
    return my_list

def check_ticket(my_ticket, winning_numbers):
    matches = 0
    for x in my_ticket:
        for y in winning_numbers:
            if x == y:
                matches += 1
    if matches == 2:
        return 1
    elif matches == 3:
        return 10
    elif matches == 4:
        return 50
    elif matches == 5:
        return 500
    elif matches == 6:
        return 1000000
    else:
        return 0

def main():
    my_ticket = generate_ticket()
    print(my_ticket)
    winnings = check_ticket(my_ticket, [1, 5, 10, 15, 20, 25])
    print(f'You won: £{winnings}')

if __name__ == "__main__":
    main()
