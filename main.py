from game_basic import DevelopCard, Gem, GemSet
from player_action import *
from init import init_deck
import cli_display


class Game:
    def __init__(self, players = list[str]) -> None:
        self.deck = init_deck(players)
        self.players = self.deck.players
        self.actions = []
        
    def gem_set(self, s: str, nums) -> GemSet:
        gem_mapping = [Gem.RUBY, Gem.SAPPHIRE, Gem.EMERALD, Gem.DIAMOND, Gem.ONYX]
        return GemSet({gem_mapping[int(i)-1]: nums for i in s})
    
    def card(self, s: str) -> DevelopCard:
        return self.deck.cards[int(s[0])-1][int(s[1])-1]
        
    def round(self):
        print(self.deck)
        print(f'actions: {Action.GET_COIN}.take coins, {Action.BUY_CARD}.buy card, '+
              f'{Action.RESERVE_CARD}.reserve card, {Action.BUY_RESERVED_CARD}.buy reserved card, space: pass\n'+
              'coins code: '+ ', '.join(f'{idx+1}{gem}' for idx, gem in enumerate(Gem)) + '\n'+
              f'coins example: 1 1, means take two {Gem.RUBY}\n'+
              f'coins example: 2 134 , means take {Gem.RUBY}{Gem.EMERALD}{Gem.DIAMOND}\n'+
              'buy card example: 3 12, means buy the second card of tier 1\n')
        if self.actions:
            action = self.actions.pop().strip().split()
        else:
            action = input('action: ').strip().split()
        if len(action) != 2 or not action[0].isdecimal() or not action[1].isdecimal():
            print(f'invalid action: {action}')
            return
        player = self.deck.current_player
        match(Action(int(action[0]))):
            case Action.GET_COIN:
                get_coin(player, self.deck, self.gem_set(action[1], 1))
            case Action.BUY_CARD:
                buy_card(player, self.deck, self.card(action[1]))
            case Action.RESERVE_CARD:
                reserve_card(player, self.deck, self.card(action[1]))
            case Action.BUY_RESERVED_CARD:
                buy_reserved_card(player, self.deck, player.reserved[int(action[1])-1])
            case _:
                print(f'invalid action: {action}')
        self.deck.round += 1

    def run(self):
        cli_display.add_cli_display()
        while True:
            self.round()
            
if __name__ == "__main__":
    # game = Game('Alice Bob Coco David'.split())
    game = Game('Alice'.split())
    game.actions = '1 123'.split(',')
    # game.actions = '1 1,1 2,1 3,1 4,2 123,2 234,2 345,2 451,3 11'.split(',')
    # game.actions.reverse()
    game.deck.coins.transfer(game.deck.current_player.coins, GemSet({Gem.RUBY: 2, Gem.SAPPHIRE: 2, Gem.EMERALD: 2, Gem.DIAMOND: 2, Gem.ONYX: 2, Gem.GOLD: 2}))
    game.run()