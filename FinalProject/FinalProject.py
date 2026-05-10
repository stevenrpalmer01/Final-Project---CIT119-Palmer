# Steven R Palmer
# CIT-119
# Final Project

'''
    Description: This application is simulating playing the card game UNO.


'''

import sys, random, time

#global variables and lists
player = True
card_deck =[]
player_hand = []
computer_hand = []
discard = []

# card lists for card deck
red_cards = ['R-0','R-1','R-1','R-2','R-2','R-3','R-3','R-4','R-4','R-5','R-5','R-6','R-6','R-7','R-7','R-8','R-8',
        'R-9','R-9','R-D2','R-D2','R-D2','R-S','R-R','R-R']

blue_cards = ['B-0','B-1','B-1','B-2','B-2','B-3','B-3','B-4','B-4','B-5','B-5','B-6','B-6','B-7','B-7','B-8','B-8',
       'B-9','B-9','B-D2','B-D2','B-S','B-S','B-R','B-R']

yellow_cards = ['Y-0','Y-1','Y-1','Y-2','Y-2','Y-3','Y-3','Y-4','Y-4','Y-5','Y-5','Y-6','Y-6','Y-7','Y-7','Y-8','Y-8',
        'Y-9','Y-9','Y-D2','Y-D2','Y-S','Y-S','Y-R','Y-R']

green_cards = ['G-0','G-1','G-1','G-2','G-2','G-3','G-3','G-4','G-4','G-5','G-5','G-6','G-6','G-7','G-7','G-8','G-8',
        'G-9','G-9','G-D2','G-D2','G-S','G-S','G-R','G-R']

wild_cards = ['W','W','W','W','W-D4','W-D4','W-D4','W-D4']


'''
    Description: This function displays the game heading.
'''
def heading():
    print('Welcome to UNO.')
    print("The first to discard all cards in their hand, wins.")
    print('Card colors are B = Blue, G = Green, R = Red, Y = Yellow')
    print('Card actions are D2 = Draw two, R = Reverse, S = Skip, W = Wild, D4 = Draw four')
    print()

''' 
    Description: This function creates the card card.
'''
def create_card_deck():
    card_deck.clear()
    card_deck.extend(red_cards)
    card_deck.extend(blue_cards)
    card_deck.extend(yellow_cards)
    card_deck.extend(green_cards)
    card_deck.extend(wild_cards)

''' 
    Description: This function shuffles the card deck by randomizing.
'''
def shuffle_deck(deck):
    print('Computer is shuffling deck...')
    time.sleep(1)
    random.shuffle(deck)

''' 
    Description: This function clears the player and computer playing hand then appends 7 cards to each
    hand.
'''
def deal_seven_cards(deck):
    player_hand.clear()
    computer_hand.clear()
    print('Computer is dealing seven cards...')
    time.sleep(1)
    for i in range(7):
        player_hand.append(deck.pop())
        computer_hand.append(deck.pop())

'''
    Description: This function allows the user to select a card color and returns 
    R, B, G or Y.
'''
def pick_color():
    color = ['R', 'B', 'G', 'Y']
    try:
        print('Wild...')
        print('Pick your color... (R, B, G, Y)...')
        response = input('> ')
        if ((response.upper()) in color):
            return response.upper()
    except ValueError:
        print('Invalid color...')
        pick_color()

''' 
    Description: This function checks the card and returns True if the card is a Wild
    or Wild Draw Four.
'''
def is_card_wild(card):
    wild = False
    if (card.split('-')[0] == 'W'):
        wild = True
    return wild

''' 
    Description: This function executes the actions taken with the first flipped discard.
    -  If the first flipped card is a Wild Draw Four, then the card is placed back into the deck,
    another card is flipped.
    -  If the first flipped card is a Wild, then the player selects the color.")
    -  If the first flipped card is a Draw 2, Reverse or Skip then the card is played against the
    the next player and player loses a turn.    
'''
def flip_card() :
    global card_deck
    global discard
    print('Computer has flipped card to discard pile ...')
    time.sleep(1)
    flipped_card = card_deck.pop(0)

    if (is_card_wild(flipped_card )):
        try:
            # if first flipped card is a draw 4
            # then card is place back in the deck
            # and another card is picked.
            if (flipped_card .split('-')[1] == 'D4'):
                print('Wild Draw Four...')
                print('Placing card back into deck...')
                card_deck.append('W-D4')
                flip_card()
        except IndexError:
            discard.append(pick_color())
            print('Player starts first...')
        return True
    elif (flipped_card.split('-')[1] == 'D2'):
        print('Draw two...')
        draw_two = flipped_card.split('-')[1]
        for i in range(int(draw_two[1])):
            player_hand.append(card_deck.pop())
        discard.append(flipped_card)
        return False
    elif (flipped_card.split('-')[1] == 'S'):
        print('Skip...')
        discard.append(flipped_card)
        return False
    elif (flipped_card.split('-')[1] == 'R'):
        print('Reverse...')
        discard.append(flipped_card)
        return False
    else:
        discard.append(flipped_card)
        print('Player starts first...')
        return True

'''
    Description: This function compares card to the facing discard for matching
    color, number or action (Draw Two, Reverse, Skip) and returns a True if
    the card is a match to the facing discard. 
'''
def does_card_match_discard(card):
    if (card.split('-')[0] == discard[0].split('-')[0]):
        return True
    try:
        if (card.split('-')[1] == discard[0].split('-')[1]):
            return True
    except IndexError:
        return False


'''
    Description: This function checks the playing hand and returns all valid cards
    that can be discarded.
'''
def valid_cards_in_hand(hand):
    valid_cards = []
    for card in hand:
        if (does_card_match_discard(card)):
            valid_cards.insert(0, card)
        if (is_card_wild(card)):
            valid_cards.append(card)
    return valid_cards


'''
    Description: This function compares the cards in hand and returns in the following order: 
    matching colors, matching number or action, then wild/wild draw four.
'''
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

'''
Description: This function picks the card from the card deck and appends it to 
player or computer hand.
'''
def pickup_card(player):
    global card_deck
    global player_hand
    global computer_hand
    try:
        if player:
            player_hand.append(card_deck.pop())
        else:
            computer_hand.append(card_deck.pop())
    except IndexError:
        print("Pickup pile is empty")
        print("Game Completed...")
        restart()


'''
Description: This function displays the player hand, computer hand and face-up discard
in a table format in the terminal output.
'''
def display_cards():
    time.sleep(1)
    card_number = []
    hidden_computer_hand = []
    player_hand_display = []

    # formatting the output to align in a table
    for i in range(len(computer_hand)):
         hidden_computer_hand.append('[X]'.center(5))

    for i in range(max(len(player_hand), len(computer_hand))):
        card_number.append(str(i+1).center(5))

    for card in player_hand:
        player_hand_display.append(str(card).center(5))

    print()
    print('Card Number: '.ljust(15) + str(card_number))
    print('Computer Hand: '.ljust(15) + str(hidden_computer_hand))
    print('Player Hand: '.ljust(15) + str(player_hand_display))
    print('Discard pile: '.ljust(15) + '[' + str(discard[0]).center(5) + ']')
    print('Draw pile: ' + str(len(card_deck)) + ' cards left.')
    print()

'''
    Description: This function displays the player menu for specific actions.
'''
def display_player_menu(player, picked_card_count):
    response = " "
    print("Player move: ")
    print("Do you want to:")
    print("     (d)iscard from hand")
    print("     (p)ick up card")
    print("     (e)nd turn")
    print("     (q)uit game")
    print("     (h)elp")

    try:
        response = input('> ').lower()
        if response.startswith('d' or 'D'):
            player = discard_to_pile(player)
            if len(player_hand) == 1:
                print('Player Uno...')
            if len(player_hand) == 0:
                print('Game Complete...')
                print('Player Wins!')
                restart()
        elif response.startswith('p' or 'P'):
            if picked_card_count == 0:
                pickup_card(player)
                display_cards()
                picked_card_count += 1
                player = display_player_menu(player, picked_card_count)
            else:
                print('Can only pick up one card')
        elif response.startswith('e' or 'E'):
            if picked_card_count >= 1:
                return False
            else:
                print('Must either pick up one card or discard.')
        elif response.startswith('q' or 'Q'):
            print('Exiting...')
            sys.exit()
        elif response.startswith('h' or 'H'):
            rules()
        else:
            print('Invalid input. Try again...')
    except KeyboardInterrupt:
        sys.exit()

    return player


'''
    Description: This function displays the game rule for UNO.
'''
def rules():
    print('Rules:')
    print()
    print("Rule 1: If the first flipped card is a Wild Draw Four, then the card is placed back into the deck, ")
    print("another card is flipped.")
    print("Rule 2: If the first flipped card is a Wild, then the next player selects the color.")
    print("Rule 3: If the first flipped card is a Draw 2, Reverse or Skip then the card is played against the  ")
    print("the next player.")
    print("Rule 4: A player cannot discard a Wild or a Wild Draw Four, if the matching card color, number, or ")
    print("action is the players hand.")
    print("Rule 5: The player discards a Wild or Wild Draw Four card, selects the card color.")
    print("Rule 6: The Reverse card reverses the direction of play .")
    print("Rule 7: The Skip card skips the next player's turn.")
    print("Rule 8: The Draw Four card, the next player picks up four cards and loses turn.")
    print("Rule 9: The Draw Two card, the next player picks up two cards and loses turn.")
    print("Rule 10: The first player to discard all cards in their hand, wins...")
    print()
    time.sleep(1)

'''
    Description: This function displays the menu to play again or quit when game is complete
'''
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
        print('Exiting...')
        sys.exit()

'''
    Description: This function executes the action required
'''
def discard_to_pile(player):
    global discard
    global player_hand
    global computer_hand

    # count the number of cards picked up
    picked_card_count = 0

    color = ['R', 'B', 'G', 'Y']

    while player:
        print('Starting from left card as number 1 to the right card as number ' + str(len(player_hand)))
        response = input('which card number do you wish to discard? : ')
        print()
        index = int(response) - 1
        try:
            if does_card_match_discard(player_hand[index]):
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
            elif is_card_wild(player_hand[index]):
                color = pick_color()
                discard.insert(0, (color))
                try:
                    if player_hand[index].split('-')[1] == 'D4':
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
                print('Invalid card. Please play another card.')
                return True
        except IndexError:
            print('There are only ' + str(len(player_hand)) +' cards. Pick again...')
            return True

    # action when it is the computers turn
    while not player:
        computer_valid_cards = []

        # compares the cards in the computer hand to the facing discard pile
        # determines which cards are valid to discard.
        computer_valid_cards = valid_cards_in_hand(computer_hand)
        try:
            # computer has no valid card to discard and must pickup
            if len(computer_valid_cards) == 0:
                time.sleep(1)
                picked_card_count += 1

                if picked_card_count == 1:
                    if len(card_deck) == 0:
                        print("Pickup pile is empty")
                        print("Game Completed...")
                        restart()
                    else:
                        print('No card... picking up card')
                        computer_hand.append(card_deck.pop())
                        continue

                # computer has picked a card but still cannot discard so turn is ended
                elif picked_card_count > 1:
                    print('Still no card... ending turn')
                    return True

            # computer has a least one valid card to discard
            elif len(computer_valid_cards) >= 1:

                sorted_card = sort_cards(computer_valid_cards)
                print('Computer discard... '+ sorted_card[0])
                time.sleep(1)

                if is_card_wild(sorted_card[0]):
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
        except IndexError:
            print("Pickup pile is empty")
            print('Game Complete...')
            restart()

def main():
    heading()
    create_card_deck()
    shuffle_deck(card_deck)
    deal_seven_cards(card_deck)
    player = flip_card()

    while len(player_hand) > 0 and len(computer_hand) > 0:
        picked_card_count = 0
        #player logic
        while player:
            display_cards()
            player = display_player_menu(player, picked_card_count)

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
