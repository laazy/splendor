from game_basic import Deck, DevelopCard, GemSet, Player, Gem
from player_action import Action



def GemSet__str__(self: GemSet) -> str:
    return ' '.join(
        [f'{gem}{cnt}' for gem, cnt in self.coins.items() if cnt > 0]
    )
    

def DevelopCard__str__(self: DevelopCard):
    return f'{self.gem}: {self.cost}  [{self.score}]'


def Player__str__(self: Player) -> str:
    return f'Player {self.name}:\n      coins: {self.coins}\n      score: {self.score}\n      cards: {self.cards_gem}\n reserved:\n'+"\n".join(map(str, self.reserved))


def Deck__str__(self: Deck) -> str:
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
    
def Gem__str__(self: Gem) -> str:
    return self.value

def Action__str__(self: Action) -> str:
    return str(self.value)

def add_cli_display():
    Player.__str__ = Player__str__
    DevelopCard.__str__ = DevelopCard__str__
    GemSet.__str__ = GemSet__str__
    Deck.__str__ = Deck__str__
    Gem.__str__ = Gem__str__
    Action.__str__ = Action__str__