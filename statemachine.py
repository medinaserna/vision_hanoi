# this state machine corresponds to all the behaviour of the Hanoi Droid robot, focused on solve the tower of hanoi game.

from transitions import Machine

class HanoiDroidFSM(object):

    # Define some states. Most of the time, narcoleptic superheroes are just like
    # everyone else. Except for...
    states = ['zero', 'face_track', 'voice_cmd', 'hanoi_game', 'hg_step1', 'hg_step2', 'hg_step3', 'hg_step4', 'hg_step5', 'hg_step6', 'hg_step7', \
              'custom_disc', 'organize_mov','comp_matrix' , 'game_solv', 'prompt_error'  ]
    # A more compact version of the quickstart transitions
    transitions = [{'trigger': 'timer_start_track', 'source': 'zero', 'dest':  'face_track'},
                   {'trigger': 'timer_face_out', 'source': 'face_track', 'dest':  'zero'},
                   {'trigger': 'voice', 'source': 'zero', 'dest':  'voice_cmd', 'before': 'recognize_command'},
                   {'trigger': 'voice', 'source': 'face_track', 'dest':  'voice_cmd'},
                   {'trigger': 'non_voice', 'source': 'voice_cmd', 'dest':  'zero'},
                   {'trigger': 'custom_disc', 'source': 'voice_cmd', 'dest':  'custom_disc'},
                   {'trigger': 'get_mtx', 'source': 'custom_disc', 'dest':  'organize_mov'},
                   {'trigger': 'ack', 'source': 'organize_mov', 'dest':  'comp_matrix'},
                   {'trigger': 'eq_mtx', 'source': 'comp_matrix', 'dest':  'game_solved'},
                   {'trigger': 'dif_mtx', 'source': 'comp_matrix', 'dest':  'prompt_error'},
                   {'trigger': 'solve_hanoi', 'source': 'voice_cmd', 'dest':  'hanoi_game'},
                   {'trigger': 'hg_start', 'source': 'hanoi_game', 'dest':  'hg_step1'},
                   {'trigger': 'ack', 'source': 'hg_step1', 'dest':  'hg_step2'},
                   {'trigger': 'ack', 'source': 'hg_step2', 'dest':  'hg_step3'},
                   {'trigger': 'ack', 'source': 'hg_step3', 'dest':  'hg_step4'},
                   {'trigger': 'ack', 'source': 'hg_step4', 'dest':  'hg_step5'},
                   {'trigger': 'ack', 'source': 'hg_step5', 'dest':  'hg_step6'},
                   {'trigger': 'ack', 'source': 'hg_step6', 'dest':  'hg_step7'},
                   {'trigger': 'dif_mtx', 'source': 'hanoi_game', 'dest':  'prompt_error'},
                   {'trigger': 'dif_mtx', 'source': 'hg_step1', 'dest':  'prompt_error'},
                   {'trigger': 'dif_mtx', 'source': 'hg_step2', 'dest':  'prompt_error'},
                   {'trigger': 'dif_mtx', 'source': 'hg_step3', 'dest':  'prompt_error'},
                   {'trigger': 'dif_mtx', 'source': 'hg_step4', 'dest':  'prompt_error'},
                   {'trigger': 'dif_mtx', 'source': 'hg_step5', 'dest':  'prompt_error'},
                   {'trigger': 'dif_mtx', 'source': 'hg_step6', 'dest':  'prompt_error'},
                   {'trigger': 'dif_mtx', 'source': 'hg_step7', 'dest':  'prompt_error'},
                   {'trigger': 'ack', 'source': 'hg_step7', 'dest':  'game_solved'},
                   {'trigger': 'timer_show', 'source': 'game_solved', 'dest':  'zero'},
                   {'trigger': 'timer_show', 'source': 'prompt_error', 'dest':  'zero'}]
    
    
    
    def __init__(self, name):

        self.name = name
        #self.kittens_rescued = 0  # What have we accomplished today?

        # Initialize the state machine
        self.machine = Machine(model=self, states=HanoiDroidFSM.states,
                               transitions=HanoiDroidFSM.transitions, initial='zero')
    
    def change_into_super_secret_costume(self):
        