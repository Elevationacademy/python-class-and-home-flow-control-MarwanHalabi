import random


class Deck:
    def __init__(self):
        colors = ["red", "blue", "green", "yellow"]
        self.deck = [[x, y] for x in colors for y in range(1, 11)]

    def deck_print(self):
        for i in self.deck:
            print(f"{i[0]} : {i[1]}")

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        random.shuffle(self.deck)
        return self.deck.pop()

    def iteration(self):
        iteatator = iter(self.deck)
        while():
            print(self.deal())
            next(iteatator)

    def __iter__(self):
        return self

    def __next__(self):
        if self.deck:
            return self.deck.pop()
        else:
            raise StopIteration


