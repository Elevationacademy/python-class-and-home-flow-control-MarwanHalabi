from deck import *

print("===========print start deck============")
deck = Deck()
deck.deck_print()
deck.shuffle()
deck.deck_print()
print("=========== cards we deal ============")
dealCard = deck.deal()
print(dealCard)
dealCard = deck.deal()
print(dealCard)
dealCard = deck.deal()
print(dealCard)
print("==========deck after dealing =============")
deck.deck_print()
print("===========after iteration======(empty)======")
deck.iteration()