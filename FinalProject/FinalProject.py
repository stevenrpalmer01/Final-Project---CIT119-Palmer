import os
import sys, random, time
import subprocess


#global variables and lists
player = True

card_deck =[]

player_hand = []

computer_hand = []

discard = []

red_cards = ['R-0','R-1','R-1','R-2','R-2','R-3','R-3','R-4','R-4','R-5','R-5','R-6','R-6','R-7','R-7','R-8','R-8',
        'R-9','R-9','R-D2','R-D2','R-D2','R-S','R-R','R-R']

blue_cards = ['B-0','B-1','B-1','B-2','B-2','B-3','B-3','B-4','B-4','B-5','B-5','B-6','B-6','B-7','B-7','B-8','B-8',
        'B-9','B-9','B-D2','B-D2','B-S','B-S','B-R','B-R']

yellow_cards = ['Y-0','Y-1','Y-1','Y-2','Y-2','Y-3','Y-3','Y-4','Y-4','Y-5','Y-5','Y-6','Y-6','Y-7','Y-7','Y-8','Y-8',
        'Y-9','Y-9','Y-D2','Y-D2','Y-S','Y-S','Y-R','Y-R']

green_cards = ['G-0','G-1','G-1','G-2','G-2','G-3','G-3','G-4','G-4','G-5','G-5','G-6','G-6','G-7','G-7','G-8','G-8',
        'G-9','G-9','G-D2','G-D2','G-S','G-S','G-R','G-R']

wild_cards = ['W','W','W','W','W-D4','W-D4','W-D4','W-D4']

def clear_screen():
    subprocess.call('clear' if os.name == 'posix' else 'cls', shell =True)


def create_card_deck():
    card_deck.clear()
    card_deck.extend(red_cards)
    card_deck.extend(blue_cards)
    card_deck.extend(yellow_cards)
    card_deck.extend(green_cards)
    card_deck.extend(wild_cards)


def shuffle_deck(deck):
    print('Computer is shuffling deck...')
    time.sleep(1)
    random.shuffle(deck)


def deal_seven_cards(deck):
    player_hand.clear()
    computer_hand.clear()
    print('Computer is dealing seven cards...')
    time.sleep(1)
    for i in range(7):
        player_hand.append(deck.pop())
        computer_hand.append(deck.pop())


def pick_color():
    color = ['R', 'B', 'G', 'Y']
    try:
        print('Pick your color... (R, B, G, Y)...')
        response = input('> ')
        if ((response.upper()) in color):
            return response.upper()
    except ValueError:
        print('Invalid color...')
        pick_color()


# Description: This function checks the card and returns True if the card is a Wild
# or Wild Draw Four or false
def is_wild_card(card):
    wild = False
    if (card.split('-')[0] == 'W'):
        wild = True
    return wild


def flip_card():
    card_deck
    discard
    color =['R','B','G','Y']

    print('Computer has flipped card to discard pile ...')
    time.sleep(1)
    picked_card = card_deck.pop(0)

    if (is_wild_card(picked_card)):
    #if picked_card.split('-')[0] == 'W':
        try:
            # if first flipped card is a draw 4
            # then card is place back in the deck
            # and another card is picked.
            if (picked_card.split('-')[1] == 'D4'):
                card_deck.append('W-D4')
                picked_card = card_deck.pop(0)
        except IndexError:
            print('Wild...')
            discard.append(random.choice(color))
            print('Player starts first...')
            return True
    if (picked_card.split('-')[1] == 'D2'):
        print('Draw two...')
        draw_two = picked_card.split('-')[1]
        for i in range(int(draw_two[1])):
            player_hand.append(card_deck.pop())
        discard.append(picked_card)
        return False
    elif (picked_card.split('-')[1] == 'S'):
        print('Skip...')
        discard.append(picked_card)
        return False
    elif (picked_card.split('-')[1] == 'R'):
        print('Reverse...')
        discard.append(picked_card)
        return False
    else:
        discard.append(picked_card)
        print('Player starts first...')
        return True


# Description: This function compares card to the facing discard for matching
# color, number or action (Draw Two, Reverse, Skip) and returns a True if
# card matches or
def does_card_match(card):
    if (card.split('-')[0] == discard[0].split('-')[0]):
        return True
    try:
        if (card.split('-')[1] == discard[0].split('-')[1]):
            return True
    except IndexError:
        return False


# Description: This function checks the playing hand and returns all valid cards
# that can be discarded.
def is_valid_card(hand):
    valid_cards = []
    for card in hand:
        if (does_card_match(card)):
            valid_cards.insert(0, card)
        if (is_wild_card(card)):
            valid_cards.append(card)
    return valid_cards


# Description:
def sort_cards(cards):
    color_cards = []
    number_cards = []
    wild_cards = []

    for card in cards:
        # if card color matched then put card into color list
        if card.split('-')[0] == discard[0].split('-')[0]:
            color_cards.append(card)
        # if card color does not match then put card into number/action list
        if card.split('-')[0] != discard[0].split('-')[0]:
            number_cards.append(card)
        # if card is wild or wild draw 4 then put card into wild list
        if card.split('-')[0] == "W":
            wild_cards.append(card)


    # return matching color, then matching number/action, then wild/wild draw four
    if len(color_cards) > 0:
        return color_cards
    elif len(number_cards) > 0:
        return number_cards
    elif len(wild_cards) > 0:
        return wild_cards


def discard_to_pile(player):
    discard
    player_hand
    computer_hand

    # count the number of cards picked up
    picked_card_count = 0

    color = ['R', 'B', 'G', 'Y']

    while (player):
        print('Starting from left card as number 1 to the right card as number ' + str(len(player_hand)))
        response = input('which card number do you wish to discard? : ')
        print()
        index = int(response) - 1
        try:
            if (does_card_match(player_hand[index])):
                try:
                    if (player_hand[index].split('-')[1] == 'D2'):
                        print('Draw two...')
                        draw_two = player_hand[index].split('-')[1]
                        for i in range(int(draw_two[1])):
                            computer_hand.append(card_deck.pop())
                        discard.insert(0, player_hand.pop(index))
                        return True
                    elif (player_hand[index].split('-')[1] == 'R'):
                        print('Reverse...')
                        discard.insert(0, player_hand.pop(index))
                        return True
                    elif (player_hand[index].split('-')[1] == 'S'):
                        print('Skip...')
                        discard.insert(0, player_hand.pop(index))
                        return True
                    else:
                        print('Player discard...' + player_hand[index] +'\n')
                        discard.insert(0, player_hand.pop(index))
                        return False
                except IndexError:
                    discard.insert(0, player_hand.pop(index))
                    return False
            # if card is a wild or draw four
            elif (is_wild_card(player_hand[index])):
                print('Wild...')
                color = pick_color()
                discard.insert(0, (color))
                try:
                    if (player_hand[index].split('-')[1] == 'D4'):
                        print('Draw four...')
                        draw_four = player_hand[index].split('-')[1]
                        for i in range(int(draw_four[1])):
                            computer_hand.append(card_deck.pop())
                        player_hand.pop(index)
                        return True
                except IndexError:
                    player_hand.pop(index)
                    return False
            else:
                print('Invalid card')
                return True
        except IndexError:
            print('There are only ' + str(len(player_hand)) +' cards. Pick again...')
            return True

    # action when it is the computers turn
    while (not player):
        computer_valid_cards = []

        # compares the cards in the computer hand to the facing discard pile
        # determines which cards are valid to discard.
        computer_valid_cards = is_valid_card(computer_hand)

        # computer has no valid card to discard and must pickup
        if (len(computer_valid_cards) == 0):
            time.sleep(1)
            picked_card_count += 1

            if (picked_card_count == 1):

                if (len(card_deck) == 0):
                    print("Pickup pile is empty")
                    print(discard)
                    restart()

                else:
                    print('No card... picking up card')
                    computer_hand.append(card_deck.pop())
                    continue

            # computer has picked a card but still cannot discard so turn is ended
            elif (picked_card_count > 1):
                print('Still no card... ending turn')
                return True

        # computer has a least one valid card to discard
        elif (len(computer_valid_cards) >= 1):

            sorted_card = sort_cards((computer_valid_cards))
            print('Computer discard... '+ sorted_card[0])
            time.sleep(1)

            if (is_wild_card(sorted_card[0])):
                print('Wild...')
                discard.insert(0, (random.choice(color)))
                try:
                    if (sorted_card[0].split('-')[1] == 'D4'):
                        print('Draw four...')
                        draw_four = sorted_card[0].split('-')[1]
                        for i in range(int(draw_four[1])):
                            player_hand.append(card_deck.pop())
                    computer_hand.remove(sorted_card[0])
                    return False
                except IndexError:
                    computer_hand.remove(sorted_card[0])
                    return True
            elif sorted_card[0].split('-')[1] == 'D2':
                print('Draw two...')
                draw_two = sorted_card[0].split('-')[1]
                for i in range(int(draw_two[1])):
                    player_hand.append(card_deck.pop())
                computer_hand.remove(sorted_card[0])
                discard.insert(0, sorted_card[0])
                return False
            elif sorted_card[0].split('-')[1] == 'R':
                print('Reverse...')
                computer_hand.remove(sorted_card[0])
                discard.insert(0, sorted_card[0])
                return False
            elif sorted_card[0].split('-')[1] == 'S':
                print('Skip...')
                computer_hand.remove(sorted_card[0])
                discard.insert(0, sorted_card[0])
                return False
            else:
                computer_hand.remove(sorted_card[0])
                discard.insert(0,sorted_card[0])
                return True


def pickup_card(player):
    card_deck
    player_hand
    computer_hand
    if (player):
        player_hand.append(card_deck.pop())
    else:
        computer_hand.append(card_deck.pop())


def display_cards():
    time.sleep(1)
    print()
    print('Computer Hand: ' + str(computer_hand))
    print('Player Hand: ' + str(player_hand))
    print('Discard pile: ' + '[ ' + str(discard[0]) + ' ]')
    print('Draw pile: ' + str(len(card_deck)) + ' cards left.')
    print()


def rules():
    print('Rules:')
    print()
    print("Rule 1: A color or number match must be played before a Wild or Wild Draw Four.")
    print("Rule 2: Colors are auto-selected when a Wild or Wild Draw Four card is played. ")
    print("Rule 3: If the first card flipped in an action, then the action is played against a player. ")
    print("Reverse: Reverses the play .")
    print("Skip: Skips the next player.")
    print("Draw Four: The next player picks up four cards and loses turn.")
    print("Draw Two: The next player picks up two cards and loses turn.")
    print()
    time.sleep(1)


def restart():
    print("Do you want to:")
    print("     (p)lay another game.")
    print("     (q)uit game")
    response = input('> ').lower()
    if response.startswith('p' or 'P'):
        print('Restarting game...')
        time.sleep(1)
        main()
    elif response.startswith('q' or 'Q'):
        quit = True
        print('Exiting...')
        sys.exit()


def main():
    quit = False

    clear_screen()

    print('Welcome to UNO.')
    print("The first to discard all cards in their hand, wins.")
    print('Card colors are B = Blue, G = Green, R = Red, Y = Yellow')
    print('Card actions are D2 = Draw two, R = Reverse, S = Skip, W = Wild, D4 = Draw four')
    print()

    create_card_deck()
    shuffle_deck(card_deck)
    deal_seven_cards(card_deck)
    player = flip_card()

    while (len(player_hand) > 0 and len(computer_hand) > 0) and not quit :
        picked_card_count = 0
        while player:
            try:
                display_cards()
                print("Player move: ")
                print("Do you want to:")
                print("     (d)iscard from hand")
                print("     (p)ick up card")
                print("     (e)nd turn")
                print("     (q)uit game")
                print("     (h)elp")
                response = input('> ').lower()
                if response.startswith('d' or 'D'):
                    player = discard_to_pile(player)

                    if len(player_hand) == 1:
                        print('Player Uno...')
                    if len(player_hand) == 0:
                        print('Game Complete...')
                        print('Player Wins!')
                        restart()
                    break
                elif response.startswith('p' or 'P'):
                    if picked_card_count == 0:
                        pickup_card(player)
                        picked_card_count += 1
                    else:
                        print('Can only pick up one card')
                        break
                elif response.startswith('e' or 'E'):
                    if picked_card_count >= 1:
                        player = False
                    else:
                        print('Must either pick up one card or discard one')
                        break
                elif response.startswith('q' or 'Q'):
                    quit = True
                    print('Exiting...')
                    break
                elif response.startswith('h' or 'H'):
                    rules()
            except ValueError:
                print("Invalid input.")
                continue
            except KeyboardInterrupt:
                sys.exit()

        #computer logic
        while not player:
            display_cards()
            print('Computer move: ')

            player = discard_to_pile(player)

            if (len(computer_hand)) == 1:
                print('Computer Uno...')


    if len(computer_hand) == 0:
        print('Game Complete...')
        print('Computer Wins!')

    restart()







main()
