import numpy as np
from ball import *

class game():
    def __init__(self):
        cue, target = self.initialize_game()
        self.play_game(cue, target)
        import pdb; pdb.set_trace()

    def initialize_game(self):
        targets = [ball(name = i + 1, location = [np.random.random_sample(), 2*np.random.random_sample()]) for i in range(0, 14)]
        cue = ball(name = 0, location = [np.random.random_sample(), 2*np.random.random_sample()])
        return cue, targets

    def play_game(self, cue, target):
        pass
        # infinite while loop with 'win condition' exit
