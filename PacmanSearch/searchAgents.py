from game import Directions
from game import Agent
from game import Actions
import util
import time
import random
import search

class RandomAgent(Agent):
    def getAction(self, state):
        legalActions = state.getLegalPacmanActions()
        if len(legalActions) > 0:
            return random.choice(legalActions)
        else:
            return Directions.STOP
        
'''
# TODO 03: SearchAgent
Implement a subclass of Agent class.
For each game step, getAction() method is invoked and 
the returned action is performed.
'''