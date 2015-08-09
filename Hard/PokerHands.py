__author__ = 'Gabriel Fishman'
"""POKER HANDS
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/86/

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

* High Card: Highest value card.
* One Pair: Two cards of the same value.
* Two Pairs: Two different pairs.
* Three of a Kind: Three cards of the same value.
* Straight: All cards are consecutive values.
* Flush: All cards of the same suit.
* Full House: Three of a kind and a pair.
* Four of a Kind: Four cards of the same value.
* Straight Flush: All cards are consecutive values of same suit.
* Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
* The cards are valued in the order:
* 2, 3, 4, 5, 6, 7, 8, 9, Ten, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights
beats a pair of fives. But if two ranks tie, for example, both players have a pair of queens, then highest cards in each
hand are compared; if the highest cards tie then the next highest cards are compared, and so on.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file contains 2 hands
(left and right). Cards and hands are separated by space. E.g.

* 6D 7H AH 7S QC 6H 2D TD JD AS
* JH 5D 7H TC JS JD JC TS 5S 7S
* 2H 8C AD TH 6H QD KD 9H 6S 6C
* JS JH 4H 2C 9H QH KC 9D 4D 3S
* TC 7H KH 4H JC 7D 9S 3H QS 7S

OUTPUT SAMPLE:

Print out the name of the winning hand or "none" in case the hands are equal. E.g.

* left
* none
* right
* left
* right
"""

import sys


class Card:
    def __init__(self, card_str):
        self.value = card_str[0]
        self.value_num = self._get_card_value(card_str[0])
        self.face = card_str[1]

    @staticmethod
    def _get_card_value(card_value):
        if card_value.isdigit():
            return int(card_value)
        elif card_value == 'T':
            return 10
        elif card_value == 'J':
            return 11
        elif card_value == 'Q':
            return 12
        elif card_value == 'K':
            return 13
        elif card_value == 'A':
            return 14

    def __str__(self):
        return self.value + self.face

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.value_num < other.value_num

    def __eq__(self, other):
        return self.value_num == other.value_num


class PokerHand:
    def __init__(self, cards):
        self.cards = list()
        for card_str in cards:
            self.cards.append(Card(card_str))
        self.cards.sort(reverse=True)
        self.value_freqs = dict()
        for card in self.cards:
            if card.value_num in self.value_freqs:
                self.value_freqs[card.value_num] += 1
            else:
                self.value_freqs[card.value_num] = 1

    def get_nth_highest_card(self, n):
        return self.cards[n]

    def num_n_of_a_kind(self, n):
        retval = 0
        for value in self.value_freqs.itervalues():
            if value == n:
                retval += 1
        return retval

    def get_nth_n_of_a_kind(self, group_size, nth_highest):
        """
        :param group_size: how many cards in the group? (e.g. pair, three of a kind, etc.)
        :param nth_highest: highest pair or second highest?
        :return:
        """
        # get a list of the n-tuples
        values = [x for x in self.value_freqs.iterkeys() if self.value_freqs.get(x) == group_size]
        values = sorted(values, reverse=True)
        return values[nth_highest - 1]

    def has_flush(self):
        faces = [x.face for x in self.cards]
        return len(set(faces)) == 1

    def has_straight(self):
        values = [x.value_num for x in self.cards]
        if values.count(14) == 1:
            is_straight_ace_high = self._has_straight(values)
            values[values.index(14)] = 1
            is_straight_ace_low = self._has_straight(values)
            return is_straight_ace_high or is_straight_ace_low
        else:
            return self._has_straight(values)

    @staticmethod
    def _has_straight(values):
        values = sorted(values)
        last = values[0]
        for value in values[1:]:
            if value - last == 1:
                last = value
            else:
                return False
        return True

    def _compare_to(self, other):
        # straight flush
        if self.has_straight() and self.has_flush():
            if other.has_straight() and other.has_flush():
                if self.get_nth_highest_card(0) == other.get_nth_highest_card(0):
                    return 0
                elif self.get_nth_highest_card(0) > other.get_nth_highest_card(0):
                    return 1
                else:
                    return -1
            else:
                return 1
        elif other.has_straight() and other.has_flush():
            return -1

        # four of a kind
        if self.num_n_of_a_kind(4) == 1:
            if other.num_n_of_a_kind(4) == 1:
                if self.get_nth_n_of_a_kind(4, 1) > other.get_nth_n_of_a_kind(4, 1):
                    return 1
                elif self.get_nth_n_of_a_kind(4, 1) == other.get_nth_n_of_a_kind(4, 1):
                    return 0
                else:
                    return -1
            else:
                return 1
        elif other.num_n_of_a_kind(4) == 1:
            return -1

        # full house - note that the rules are different for games like Hold'Em where there are community cards
        if self.num_n_of_a_kind(3) == 1 and self.num_n_of_a_kind(2) == 1:
            if other.num_n_of_a_kind(3) == 1 and other.num_n_of_a_kind(2) == 1:
                if self.get_nth_n_of_a_kind(3, 1) > other.get_nth_n_of_a_kind(3, 1):
                    return 1
                elif self.get_nth_n_of_a_kind(3, 1) == other.get_nth_n_of_a_kind(3, 1):
                    return 0
                else:
                    return -1
            else:
                return 1
        elif other.num_n_of_a_kind(3) == 1 and other.num_n_of_a_kind(2) == 1:
            return -1

        # flush, if both have a flush, see who has the highest card, if that's a tie go to the 2nd highest, etc.
        if self.has_flush():
            if other.has_flush():
                for i in range(0, 5):
                    if self.get_nth_highest_card(i) > other.get_nth_highest_card(i):
                        return 1
                    elif self.get_nth_highest_card(i) < other.get_nth_highest_card(i):
                        return -1
                return 0
            else:
                return 1
        elif other.has_flush():
            return -1

        # straight
        if self.has_straight():
            if other.has_straight():
                self_highest_card = other_highest_card = 0
                if self.get_nth_highest_card(0).value_num == 14 and self.get_nth_highest_card(1).value_num == 5:
                    self_highest_card = 5    # aces are low, this is a 5-high straight
                else:
                    self_highest_card = self.get_nth_highest_card(0).value_num
                if other.get_nth_highest_card(0).value_num == 14 and other.get_nth_highest_card(1).value_num == 5:
                    other_highest_card = 5
                else:
                    other_highest_card = other.get_nth_highest_card(0).value_num

                if self_highest_card > other_highest_card:
                    return 1
                elif self_highest_card == other_highest_card:
                    return 0
                else:
                    return -1
            else:
                return 1
        elif other.has_straight():
            return -1

        # three of a kind, rules are different if there are community cards (and it's possible for two players to have
        # the same three of a kind)
        if self.num_n_of_a_kind(3) == 1:
            if other.num_n_of_a_kind(3) == 1:
                if self.get_nth_n_of_a_kind(3, 1) > other.get_nth_n_of_a_kind(3, 1):
                    return 1
                else:
                    return -1
            else:
                return 1
        elif other.num_n_of_a_kind(3) == 1:
            return -1

        # two pair
        if self.num_n_of_a_kind(2) == 2:
            if other.num_n_of_a_kind(2) == 2:
                if self.get_nth_n_of_a_kind(2, 1) > other.get_nth_n_of_a_kind(2, 1):
                    return 1
                elif self.get_nth_n_of_a_kind(2, 1) == other.get_nth_n_of_a_kind(2, 1):
                    if self.get_nth_n_of_a_kind(2, 2) > other.get_nth_n_of_a_kind(2, 2):
                        return 1
                    elif self.get_nth_n_of_a_kind(2, 2) == other.get_nth_n_of_a_kind(2, 2):
                        if self.get_nth_highest_card(4) > other.get_nth_highest_card(4):
                            return 1
                        elif self.get_nth_highest_card(4) == other.get_nth_highest_card(4):
                            return 0
                        else:
                            return -1
                    else:
                        return -1
                else:
                    return -1
            else:
                return 1
        elif other.num_n_of_a_kind(2) == 2:
            return -1

        # one pair
        if self.num_n_of_a_kind(2) == 1:
            if other.num_n_of_a_kind(2) == 1:
                if self.get_nth_n_of_a_kind(2, 1) > other.get_nth_n_of_a_kind(2, 1):
                    return 1
                elif self.get_nth_n_of_a_kind(2, 1) == other.get_nth_n_of_a_kind(2, 1):
                    for i in range(2, 5):
                        if self.get_nth_highest_card(i) > other.get_nth_highest_card(i):
                            return 1
                        elif self.get_nth_highest_card(i) < other.get_nth_highest_card(i):
                            return -1
                    return 0
                else:
                    return -1
            else:
                return 1
        elif other.num_n_of_a_kind(2) == 1:
            return -1

        # high card
        for i in range(0, 5):
            if self.get_nth_highest_card(i) > other.get_nth_highest_card(i):
                return 1
            elif self.get_nth_highest_card(i) < other.get_nth_highest_card(i):
                return -1
        return 0

    def __str__(self):
        return "".join(self.cards.__str__())

    def __lt__(self, other):
        return self._compare_to(other) == -1

    def __eq__(self, other):
        return self._compare_to(other) == 0


def main():
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            hand_one = PokerHand(list(test[:14].split(" ")))
            hand_two = PokerHand(list(test[15:].strip().split(" ")))
            if hand_one > hand_two:
                print "left"
            elif hand_one == hand_two:
                print "none"
            else:
                print "right"

if __name__ == "__main__":
    main()

