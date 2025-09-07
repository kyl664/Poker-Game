from collections import Counter

card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11}

########## poker hand functions ##########

def high_card(hand):
    def get_value(item):
        if item[0].isdigit():
            num = ''.join(filter(str.isdigit, item))
            return int(num)
        else:
            return card_values.get(item[0], 0)
    high = max(hand, key=get_value)
    return f"high card: {high}"
    
def pair(hand):
    ranks, _ = parse_hand(hand)
    rank_counts = Counter(ranks)

    pairs = [rank for rank, count in rank_counts.items() if count == 2]

    if len(pairs) == 1:
        return f"pair: {pairs[0]}'s"
    else:
        return False
    
def two_pair(hand):
    ranks, _ = parse_hand(hand)
    rank_counts = Counter(ranks)

    two_pairs = [rank for rank, count in rank_counts.items() if count == 2]

    if len(two_pairs) == 2:
        return f"two pair: pair of {two_pairs[0]}'s and {two_pairs[1]}'s"
    else:
        return False
    
def three_of_a_kind(hand):
    ranks, _ = parse_hand(hand)
    rank_counts = Counter(ranks)

    three = [rank for rank, count in rank_counts.items() if count == 3]

    if len(three) == 1:
        return f"three of a kind: {three[0]}'s"
    else:
        return False
    
def straight(hand):
    ranks, _ = parse_hand(hand)
    values = sorted(set(rank_to_value(r) for r in ranks))

    for i in range(len(values) - 4):
        window = values[i:i+5]
        if window == list(range(window[0], window[0] + 5)):
            return f"straight: {', '.join(get_cards_by_values(hand, window))}"
    
    return False

def flush(hand):
    _, suits = parse_hand(hand)
    suit_counts = Counter(suits)

    flush_list = [suit for suit, count in suit_counts.items() if count == 5]
    translation = {'s': 'spade', 'c': 'club', 'h': 'heart', 'd': 'diamond'}
    
    if len(flush_list) == 1:
        suit_name = translation[flush_list[0]]
        return f"flush: {suit_name}'s"
    else:
        return False
    
def full_house(hand):
    ranks, _ = parse_hand(hand)
    rank_counts = Counter(ranks)

    has_three = None
    has_pair = None

    for rank, count in rank_counts.items():
        if count >= 3 and not has_three:
            has_three = rank
        elif count >= 2:
            if not has_pair or rank != has_three:
                has_pair = rank

    if has_three and has_pair and has_three != has_pair:
        return f"Full House: {has_three}s full of {has_pair}s"
    else:
        return False
        

def four_of_a_kind(hand):
    ranks, _ = parse_hand(hand)
    rank_counts = Counter(ranks)

    four = [rank for rank, count in rank_counts.items() if count == 4]

    if len(four) == 1:
        return f"four of a kind: {four[0]}'s"
    else:
        return False
    
    
def straight_flush(hand):
    ranks, suits = parse_hand(hand)
    suit_counts = Counter(suits)
    
    flush_suits = [suit for suit, count in suit_counts.items() if count >= 5]
    
    for suit in flush_suits:
        suited_cards = [card for card in hand if card[-1] == suit]
        suited_ranks = [card[:-1] for card in suited_cards]
        values = sorted(set(rank_to_value(r) for r in suited_ranks))

        for i in range(len(values) - 4):
            window = values[i:i+5]
            if window == list(range(window[0], window[0] + 5)):
                straight_flush_cards = get_cards_by_values(suited_cards, window)
                return f"Straight Flush: {', '.join(straight_flush_cards)}"

    return False

    
    
def royal_flush(hand):
    ranks, suits = parse_hand(hand)
    suit_counts = Counter(suits)

    flush_suits = [suit for suit, count in suit_counts.items() if count >= 5]

    for suit in flush_suits:
        suited_cards = [card for card in hand if card[-1] == suit]
        suited_ranks = [card[:-1] for card in suited_cards]
        values = sorted(set(rank_to_value(r) for r in suited_ranks))

        for i in range(len(values) - 4):
            window = values[i:i+5]
            if window == list(range(window[0], window[0] + 5)):
                straight_flush_cards = get_cards_by_values(suited_cards, window)
                if window == [10, 11, 12, 13, 14]:
                    return f"Royal Flush: {', '.join(straight_flush_cards)}"
                return False

    return False

########## helper functions ##########
    
def parse_hand(hand):
    ranks = []
    suits = []
    for card in hand:
        rank = card[:-1]
        suit = card[-1]
        ranks.append(rank)
        suits.append(suit)
    return ranks, suits

def rank_to_value(rank):
    if rank in ['J', 'Q', 'K', 'A']:
        return {'J': 11, 'Q': 12, 'K': 13, 'A': 14}[rank]
    return int(rank)

def value_to_rank(value):
    return {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}.get(value, str(value))

def get_cards_by_values(hand, values):
    value_set = set(values)
    result = []
    used = set()
    for val in values:
        for card in hand:
            rank = card[:-1]
            if rank_to_value(rank) == val and card not in used:
                result.append(card)
                used.add(card)
                break
    return result
                                                    

def eval_cards(hand):
    if royal_flush(hand):
        print(royal_flush(hand))
        return 10
    if straight_flush(hand):
        print(straight_flush(hand))
        return 9
    if four_of_a_kind(hand):
        print(four_of_a_kind(hand))
        return 8
    if full_house(hand):
        print(full_house(hand))
        return 7
    if flush(hand):
        print(flush(hand))
        return 6
    if straight(hand):
        print(straight(hand))
        return 5
    if three_of_a_kind(hand):
        print(three_of_a_kind(hand))
        return 4
    if two_pair(hand):
        print(two_pair(hand))
        return 3
    if pair(hand):
        print(pair(hand))
        return 2
    if high_card(hand):
        print(high_card(hand))
        return 1
