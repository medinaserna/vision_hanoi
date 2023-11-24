# this state machine corresponds to all the behaviour of the Hanoi Droid robot, focused on solve the tower of hanoi game.

from transitions import Machine
import random


class hanoidroidFSM(object):

    # Define some states. Most of the time, narcoleptic superheroes are just like
    # everyone else. Except for...
    states = ['zero', 'face_track', 'voice_cmd', 'hanoi_game', 'hg_step1', 'hg_step2', 'hg_step3', 'hg_step4', 'hg_step5', 'hg_step6', 'hg_step7', \
              'custom_disc', 'organize_mov', 'game_solv', 'prompt_error'  ]
    # A more compact version of the quickstart transitions
    transitions = [['wakeup', 'asleep', 'hanging out'],
                   ['work_out',  'hanging out', 'hungry'],
                   ['eat', 'hungry', 'hanging out'],
                   {'trigger': 'distress_call', 'source': '*', 'dest':  'saving the world', 'before': 'change_into_super_secret_costume'},
                   {'trigger': 'complete_mission', 'source': 'saving the world', 'dest':  'sweaty', 'after': 'update_journal'},
                   {'trigger': 'clean_up', 'source': 'sweaty', 'dest':  'asleep', 'conditions': 'is_exhausted'},
                   ['clean_up', 'sweaty', 'hanging out'],
                   ['nap', '*', 'asleep']]


    def __init__(self, name):

        # No anonymous superheroes on my watch! Every narcoleptic superhero gets
        # a name. Any name at all. SleepyMan. SlumberGirl. You get the idea.
        self.name = name
        self.kittens_rescued = 0  # What have we accomplished today?

        # Initialize the state machine
        self.machine = Machine(model=self, states=NarcolepticSuperhero.states,
                               transitions=NarcolepticSuperhero.transitions, initial='asleep')

    def update_journal(self):
        """ Dear Diary, today I saved Mr. Whiskers. Again. """
        self.kittens_rescued += 1

    #@property
    def is_exhausted(self):
        """ Basically a coin toss. """
        return random.random() < 0.5

    def change_into_super_secret_costume(self):
        print("Beauty, eh?")
        
    def yell(self):
        print(f"I am {self.name} and I am {self.state}!")