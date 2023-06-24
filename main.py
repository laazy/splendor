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
        print(f'actions: {Action.GET_COIN}. take coins, {Action.BUY_CARD}. buy card, '+
              f'{Action.RESERVE_CARD}. reserve card, {Action.BUY_RESERVED_CARD}. buy reserved card, space: pass\n'+
              'coins code: '+ ', '.join(f'{idx+1}{gem.value}' for idx, gem in enumerate(Gem)) + '\n'+
              f'coins example: 1 1, means take two {Gem.RUBY.value}\n'+
              f'coins example: 2 134 , means take {Gem.RUBY.value}{Gem.EMERALD.value}{Gem.DIAMOND.value}\n'+
              'buy card example: 3 12, means buy the second card of tier 1\n')
        action = input('action: ').strip().split()
        # action = self.actions.pop().strip().split()
        if len(action) != 2 or not action[0].isdecimal() or not action[1].isdecimal():
            print(f'invalid action: {action}')
            return
        player = self.deck.current_player
        match(int(action[0])):
            case 1:
                self.deck.coins.transfer(player.coins, self.gem_set(action[1], 2))
            case 2:
                self.deck.coins.transfer(player.coins, self.gem_set(action[1], 1))
            case 3:
                buy_card(player, self.deck, self.card(action[1]))
            case 4:
                reserve_card(player, self.deck, self.card(action[1]))
            case 5:
                buy_reserved_card(player, self.deck, self.card(action[1]))
            case 2:
                pass
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
    game.actions = '1 1,1 2,1 3,1 4,2 123,2 234,2 345,2 451,3 11'.split(',')
    game.actions.reverse()
    game.deck.coins.transfer(game.deck.current_player.coins, GemSet({Gem.RUBY: 2, Gem.SAPPHIRE: 2, Gem.EMERALD: 2, Gem.DIAMOND: 2, Gem.ONYX: 2, Gem.GOLD: 2}))
    game.run()