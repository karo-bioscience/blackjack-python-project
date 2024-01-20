import random

def deck():
    value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_type = ['♠', '♥', '♣', '♦']
    new_deck = [{'Value': x, 'Type': y} for x in value for y in card_type]
    random.shuffle(new_deck)
    return new_deck

def card_value(x):
    value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}
    return value[x]

def amount(player):
    return sum(card_value(card['Value']) for card in player) + 10 if 'A' in [card['Value'] for card in player] and sum(card_value(card['Value']) for card in player) <= 11 else sum(card_value(card['Value']) for card in player)

def draw_card(pvalue, player):
    card = pvalue.pop()
    player.append(card)
    print('\nDrawing card...\n')

def croupier_draw_card(pvalue, croupier):
    while amount(croupier) < 17:
        card = pvalue.pop()
        croupier.append(card)

#Wynik remisowy gry
def remis(player, croupier):
    return amount(player) == amount(croupier)
     
def interface(player, croupier, show_cards=False):
    print('\nPlayers deck:', player, '\nTotal value:', amount(player))
    if show_cards:
        print('\nCroupiers deck:', croupier, '\nTotal value:', amount(croupier))
    else:
        print('\nCroupiers deck:', [croupier[0], 'X'])

def play_again():
    return input('Play again? (Y/N)\n').strip().lower() == 'y'

def root():
    while True:
        pvalue = deck()
        player = [pvalue.pop(), pvalue.pop()]
        croupier = [pvalue.pop(), pvalue.pop()]
        while True:
            if amount(player) == 21:
                interface(player, croupier, show_cards=True)
                print('\nBlackjack! You\'ve got a total of 21 points. You won.')
                break
            interface(player, croupier)
            choice = input('\nDraw a card? (Y/N)\n').upper()
            if choice == 'Y':
                draw_card(pvalue, player)
                if amount(player) > 21:
                    interface(player, croupier, show_cards=True)
                    print('\nYour total points exceeded the limit. Croupier wins.')
                    break
            elif choice == 'N':
                croupier_draw_card(pvalue, croupier)
                interface(player, croupier, show_cards=True)
                if remis(player, croupier):
                    print('\nDraw. Your total points are equal to croupiers total points.')
                else:
                    winner = '\nPlayer' if amount(player) > amount(croupier) or amount(croupier) > 21 else '\nCroupier'
                    print(winner, 'wins.')
                break
            else:
                print('\nInvalid value. Try again.\n')
        if not play_again():
            break

if __name__ == '__main__':
    root()