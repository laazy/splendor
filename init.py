from itertools import combinations
from random import shuffle

from game_basic import Deck, DevelopCard, Gem, GemSet, Player


def _append_card(
    cards: list[list[DevelopCard]],
    tier: int,
    cost: dict[Gem, int],
    gem: Gem,
    score: int,
    nums: int,
):
    for _ in range(nums):
        cards[tier].append(DevelopCard(1, GemSet(cost), gem, score))


def init_card() -> list[list[DevelopCard]]:
    cards = [[], [], []]
    gems = [gem for gem in Gem if gem != Gem.GOLD]
    # 1 kind gem
    for g in Gem:
        _append_card(cards, 0, {g: 3}, g, 0, 2)
        _append_card(cards, 0, {g: 4}, g, 1, 1)
        _append_card(cards, 1, {g: 5}, g, 2, 2)
        _append_card(cards, 2, {g: 6}, g, 3, 2)
        _append_card(cards, 2, {g: 7}, g, 4, 1)
    for g1, g2 in combinations(Gem, 2):
        _append_card(cards, 0, {g1: 3}, g2, 0, 2)
        _append_card(cards, 0, {g1: 4}, g2, 1, 1)
        _append_card(cards, 1, {g1: 5}, g2, 2, 2)
        _append_card(cards, 2, {g1: 6}, g2, 3, 2)
        _append_card(cards, 2, {g1: 7}, g2, 4, 1)
    for i in cards:
        shuffle(i)
    return cards


def init_coin(player_cnt: int) -> GemSet:
    return GemSet(
        {
            Gem.RUBY: 7,
            Gem.SAPPHIRE: 7,
            Gem.EMERALD: 7,
            Gem.DIAMOND: 7,
            Gem.ONYX: 7,
            Gem.GOLD: 5,
        }
    )


def init_deck(players: list[str]) -> Deck:
    deck = Deck(
        [Player(name) for name in players], init_card(), init_coin(len(players))
    )
    return deck
