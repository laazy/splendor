from game_basic import Deck, DevelopCard, GemSet, Player



def GemSet__str__(self) -> str:
    return ' '.join(
        [f'{gem.value}{cnt}' for gem, cnt in self.coins.items() if cnt > 0]
    )
    

def DevelopCard__str__(self):
    return f'{self.gem.value}: {self.cost}  [{self.score}]'


def Player__str__(self) -> str:
    return f'Player {self.name}:\n      coins: {self.coins}\n      score: {self.score}\n     cards: {self.cards_gem}\n reserved: {self.reserved}'


def Deck__str__(self) -> str:
    return (
        f'============ round: {self.round} ============\n'
        + '\n'.join(map(str, self.players))
        + '\n'
        + '\n'.join(
            [
                f'============ tier {i+1} ============\n'
                + '\n'.join(map(str, cards[: min(len(cards), 4)]))
                for i, cards in enumerate(self.cards)
            ]
        )
        + '\n============ coins ============\n'
        + str(self.coins)
        + f'\n============ {self.current_player.name} turn ============\n'
    )

def add_cli_display():
    Player.__str__ = Player__str__
    DevelopCard.__str__ = DevelopCard__str__
    GemSet.__str__ = GemSet__str__
    Deck.__str__ = Deck__str__