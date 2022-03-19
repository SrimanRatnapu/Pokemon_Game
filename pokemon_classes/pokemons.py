from pokebase import pokemon


class pikachu(pokemon):
    
    def __init__(self, level):
        super().__init__(level)
        self.moves = {}        
        self.maximum_stats   = {'health': 35, 'attack': 55, 'defense': 40}
        self.effective_stats = {'health': None, 'attack': None, 'defense': None}
        self._stat_calculation()
        self.current_hp = self.effective_stats['health']
        self.alive = True
        
        
        
class bulbasaur(pokemon):
    
    def __init__(self, level):
        super().__init__(level):
        self.moves = {}
        self.maximum_stats   = {'health': 35, 'attack': 55, 'defense': 40}
        self.effective_stats = {'health': None, 'attack': None, 'defense': None}
        self._stat_calculation()
        self.current_hp = self.effective_stats['health']
        self.alive = True