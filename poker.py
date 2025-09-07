from poker_hands import eval_cards
import random
import itertools

cards = ['2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'Js', 'Qs', 'Ks', 'As',
    '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc', 'Ac',
    '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'Jh', 'Qh', 'Kh', 'Ah',
    '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'Jd', 'Qd', 'Kd', 'Ad']
table = []
hand = []
full_hand = table + hand


pot = 0
status = 0

def get_cards(cards):
    delt_cards = random.sample(cards, 2)
    for card in delt_cards:
        cards.remove(card)
    for card in delt_cards:
        hand.append(card)
        full_hand.append(card)
    print(f"your hand is {hand}.")
    return hand

def flop(cards):
    flop_cards = random.sample(cards, 3)
    for card in flop_cards:
        cards.remove(card)
    for card in flop_cards:
        table.append(card)
        full_hand.append(card)
    print(f"flop: {table}")
    return table

def turn(cards):
    turn_card = random.choice(cards)
    cards.remove(turn_card)
    table.append(turn_card)
    full_hand.append(turn_card)
    print(f"turn: {table}")
    return table

def river(cards):
    river_card = random.choice(cards)
    cards.remove(river_card)
    table.append(river_card)
    full_hand.append(river_card)
    print(f"river: {table}")
    return table

def bet_check_fold():
    global pot
    global status
    loop = True
    
    if status == 1:
        loop =  False
        
    while loop:
        
        bcf = input('do you want to bet, check or fold? enter [b] (bet), [c] (check), or [f] (fold):')
        
        if bcf not in ['b', 'c', 'f']:
            print("Invalid input! Please enter only 'b', 'c', or 'f'.")
            continue
        
        elif bcf == 'b':
            chips = input('how much do you want to bet: ')
            try:
                chips = int(chips)
                print(f"You entered {chips} chips.")
                pot += chips
                break
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue
            
        elif bcf == 'f':
            print('you folded')
            status = 1
            break
        
        else:
            print('you checked')
            break
        
def deal_cards(num_players)

if __name__ == "__main__":
 
    get_cards(cards)
    eval_cards(full_hand)
    bet_check_fold()
    flop(cards)
    eval_cards(full_hand)
    bet_check_fold()
    turn(cards)
    eval_cards(full_hand)
    bet_check_fold()
    river(cards)
    eval_cards(full_hand)
    bet_check_fold()
