from collections import Counter
import pandas as pd

# part 1 #
card_rank = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
type_rank = ['five_of_a_kind', 'four_of_a_kind', 'full_house', 'three_of_a_kind', 'two_pairs', 'one_pair', 'high_card']
def get_type(hand):
    cntr = Counter(hand).most_common()
    if cntr[0][1] == 5:
        type = type_rank[0]
    if cntr[0][1] == 4:
        type = type_rank[1]
    if cntr[0][1] == 3:
        if cntr[1][1] == 2:
            type = type_rank[2]
        else:
            type = type_rank[3]
    if cntr[0][1] == 2:
        if cntr[1][1] == 2:
            type = type_rank[4]
        else:
            type = type_rank[5]
    if cntr[0][1] == 1:
        type = type_rank[6]
    return type

def get_card_from_hand(hand, position):
    return hand[position]


cc = pd.read_csv('2023/input07', sep=' ', header=None, names=['hand', 'bid'])
cc['type'] = pd.Categorical(cc['hand'].apply(get_type), categories=type_rank, ordered=True)

for i in range(5):
    cc[f"{i+1}C"] = pd.Categorical(cc['hand'].apply(get_card_from_hand, args=(i,)), categories=card_rank, ordered=True)

cc = cc.sort_values(by=['type', '1C', '2C', '3C', '4C', '5C'], ascending=[True]*6)
cc['rank'] = list(range(len(cc), 0, -1))
cc['winning'] = cc['bid'] * cc['rank']

cc['winning'].sum()

# part 2 #
card_rank = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
type_rank = ['five_of_a_kind', 'four_of_a_kind', 'full_house', 'three_of_a_kind', 'two_pairs', 'one_pair', 'high_card']
def get_best_type(hand, jokers):
    cntr = Counter(hand).most_common()
    if jokers == 5:
        hand = 'AAAAA'
        cntr = Counter(hand).most_common()
    elif jokers > 0:
        if cntr[0][0] == 'J':
            new = cntr[1][0]
        else:
            new = cntr[0][0]
        hand = hand.replace('J', new)
        cntr = Counter(hand).most_common()
    if cntr[0][1] == 5:
        type = type_rank[0]
    if cntr[0][1] == 4:
        type = type_rank[1]
    if cntr[0][1] == 3:
        if cntr[1][1] == 2:
            type = type_rank[2]
        else:
            type = type_rank[3]
    if cntr[0][1] == 2:
        if cntr[1][1] == 2:
            type = type_rank[4]
        else:
            type = type_rank[5]
    if cntr[0][1] == 1:
        type = type_rank[6]
    return type

def get_card_from_hand(hand, position):
    return hand[position]


cc = pd.read_csv('2023/input07', sep=' ', header=None, names=['hand', 'bid'])
cc['jokers'] = cc['hand'].apply(lambda x: x.count('J'))
cc['type'] = pd.Categorical(cc.apply(lambda x: get_best_type(x.hand, x.jokers), axis=1), categories=type_rank, ordered=True)

for i in range(5):
    cc[f"{i+1}C"] = pd.Categorical(cc['hand'].apply(get_card_from_hand, args=(i,)), categories=card_rank, ordered=True)

cc = cc.sort_values(by=['type', '1C', '2C', '3C', '4C', '5C'], ascending=[True]*6)
cc['rank'] = list(range(len(cc), 0, -1))
cc['winning'] = cc['bid'] * cc['rank']

cc['winning'].sum()
