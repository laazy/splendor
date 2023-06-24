from game_basic import DevelopCard, Gem, GemSet
from player_action import *
from init import init_deck

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
        print('actions: 1. take 2 coins, 2. take 3 coins, 3. buy card, 4. reserve card, 5. buy reserved card, 6. pass\n'+
              f'coins code: 1{Gem.RUBY}, 2{Gem.SAPPHIRE},  3{Gem.EMERALD},  4{Gem.DIAMOND},  5{Gem.ONYX}\n'+
              f'coins example: 1 1, means take two {Gem.RUBY}\n'+
              f'coins example: 2 134 , means take {Gem.RUBY}{Gem.EMERALD}{Gem.DIAMOND}\n'+
              'card format: 3 12, means buy second tier 1 card\n')
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
            case 6:
                pass
            case _:
                print(f'invalid action: {action}')
        self.deck.round += 1

    def run(self):
        while True:
            self.round()
            
if __name__ == "__main__":
    # game = Game('Alice Bob Coco David'.split())
    game = Game('Alice'.split())
    game.actions = '1 1,1 2,1 3,1 4,2 123,2 234,2 345,2 451,3 11'.split(',')
    game.actions.reverse()
    game.deck.coins.transfer(game.deck.current_player.coins, GemSet({Gem.RUBY: 6, Gem.SAPPHIRE: 6, Gem.EMERALD: 6, Gem.DIAMOND: 6, Gem.ONYX: 6}))
    game.run()