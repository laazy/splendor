from enum import Enum
from game_basic import Player, Gem, GemSet, DevelopCard, Deck
from rule import DeepCollect


class Action(Enum):
    GET_COIN = 1
    BUY_CARD = 2
    RESERVE_CARD = 3
    BUY_RESERVED_CARD = 4


def _actual_cost(player: Player, card: DevelopCard) -> GemSet:
    gems = player.cards_gem
    cost = GemSet(
        {gem: max(0, cnt - gems[gem]) for gem, cnt in card.cost.coins.items()}
    )
    if player.coins >= cost:
        return cost
    for gem, cnt in cost.coins.items():
        extra_coin = max(0, cnt - player.coins[gem])
        cost.coins[Gem.GOLD] += extra_coin
        cost.coins[gem] = min(cnt, player.coins[gem])
    return cost


def get_coin(player: Player, deck: Deck, coins: GemSet):
    if coins.count <= 3 and coins.count == len(coins.kind):
        pass
    elif len(coins.kind) == DeepCollect.KIND_COUNT and coins.count == DeepCollect.AMOUT:
        if deck.coins[coins.kind[0]] < DeepCollect.DECK_LIMIT:
            raise ValueError("deck have insufficient coins")
    else:
        raise ValueError("must be <=3 different or 2 same")

    deck.coins.transfer(player.coins, coins)


def buy_card(player: Player, deck: Deck, card: DevelopCard):
    cost = _actual_cost(player, card)
    if cost <= player.coins:
        player.coins.transfer(deck.coins, cost)
        player.cards.append(card)
        deck.cards[card.tier - 1].remove(card)
    else:
        raise ValueError("player have insufficient coins")


def reserve_card(player: Player, deck: Deck, card: DevelopCard):
    player.reserved.append(card)
    if deck.coins[Gem.GOLD] > 0:
        deck.coins.transfer(player.coins, GemSet({Gem.GOLD: 1}))
        deck.cards[card.tier - 1].remove(card)
    else:
        raise ValueError("player have 3 cards")


def buy_reserved_card(player: Player, deck: Deck, card: DevelopCard):
    cost = _actual_cost(player, card)
    if cost <= player.coins:
        player.coins.transfer(deck.coins, cost)
        player.cards.append(card)
        player.reserved.remove(card)
    else:
        raise ValueError("player have insufficient coins")
