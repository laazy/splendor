from collections import defaultdict
from dataclasses import dataclass, field
from enum import Enum


class Gem(Enum):
    RUBY = '🔴'
    SAPPHIRE = '🔵'
    EMERALD = '🟢'
    DIAMOND = '⚪️'
    ONYX = '💎'
    GOLD = '🪙'


@dataclass
class GemSet:
    coins: dict[Gem, int] = field(default_factory=dict)

    def __post_init__(self):
        self.coins = {gem: self.coins.get(gem, 0) for gem in Gem}

    @property
    def kind(self):
        return [gem for gem in self.coins if self.coins[gem] > 0]

    @property
    def count(self):
        return sum(self.coins.values())

    def transfer(self, other: 'GemSet', cost: 'GemSet'):
        if self >= cost:
            for gem, cnt in cost.coins.items():
                self.coins[gem] -= cnt
                other.coins[gem] += cnt
        else:
            raise ValueError('Insufficient gems')

    def __ge__(self, other: 'GemSet'):
        return all(self.coins[gem] >= other.coins[gem] for gem in Gem)

    def __getitem__(self, item):
        return self.coins[item]


@dataclass
class DevelopCard:
    tier: int
    cost: GemSet
    gem: Gem
    score: int


@dataclass
class Player:
    name: str
    coins: GemSet = field(default_factory=GemSet)
    cards: list[DevelopCard] = field(default_factory=list)
    reserved: list[DevelopCard] = field(default_factory=list)

    @property
    def score(self) -> int:
        return sum(card.score for card in self.cards)

    @property
    def cards_gem(self) -> GemSet:
        gems = defaultdict(int)
        for card in self.cards:
            gems[card.gem] += 1
        return GemSet(gems)


@dataclass
class Deck:
    players: list[Player]
    cards: list[list[DevelopCard]]
    coins: GemSet
    round = 0

    @property
    def current_player(self):
        return self.players[self.round % len(self.players)]
