#settings.py

import numpy as np

def init():
   

    #the color ranges, this is setting experimentally but should be improved or looking for a theorical approach

    global L_limit_blue
    global U_limit_blue   

    ##------ BLUE----------
    L_limit_blue=np.array([98,50,50]) # setting the blue lower limit
    U_limit_blue=np.array([139,255,255]) # setting the blue upper limit
    
    
    global L_limit_red1
    global U_limit_red1 
    global L_limit_red2
    global U_limit_red2
    
    
    ##------ RED----------
    L_limit_red1=np.array([0,50,50]) # setting the red part1 lower limit
    U_limit_red1=np.array([10,255,255]) # setting the red part1 upper limit
    L_limit_red2=np.array([160,50,50]) # setting the red part1 lower limit
    U_limit_red2=np.array([179,255,255]) # setting the red part1 upper limit

    
    global L_limit_yellow
    global U_limit_yellow   


    ##------ YELLOW----------
    L_limit_yellow=np.array([20,50,50]) # setting the yellow lower limit
    U_limit_yellow=np.array([40,255,255]) # setting the yellow upper limit
    
    
    
    
    ##--------Fixed disc positions and movements represented as matrix
    
    
    global hanoi_matrix_num
    hanoi_matrix_num = np.zeros((3,3))
    hanoi_matrix_num = np.array([[1, 0, 0 ], [2, 0, 0 ], [3, 0, 0], 
                            [0, 0, 0 ], [2, 0, 0 ], [3, 0, 1],
                            [0, 0, 0 ], [0, 0, 0 ], [3, 2, 1],
                            [0, 0, 0 ], [0, 1, 0 ], [3, 2, 0],
                            [0, 0, 0 ], [0, 1, 0 ], [0, 2, 3],
                            [0, 0, 0 ], [0, 0, 0 ], [1, 2, 3],
                            [0, 0, 0 ], [0, 0, 2 ], [1, 0, 3],
                            [0, 0, 1 ], [0, 0, 2 ], [0, 0, 3]]) 
    
    
    
    global hanoi_matrix_char
    hanoi_matrix_char = np.zeros((3,3), dtype = str)
    hanoi_matrix_char = np.array([['B', '0', '0' ], ['Y', '0', '0' ], ['R', '0', '0'], 
                            ['0', '0', '0' ], ['Y', '0', '0' ], ['R', '0', 'B'],
                            ['0', '0', '0' ], ['0', '0', '0' ], ['R', 'Y', 'B'],
                            ['0', '0', '0' ], ['0', 'B', '0' ], ['R', 'Y', '0'],
                            ['0', '0', '0' ], ['0', 'B', '0' ], ['0', 'Y', 'R'],
                            ['0', '0', '0' ], ['0', '0', '0' ], ['B', 'Y', 'R'],
                            ['0', '0', '0' ], ['0', '0', 'Y' ], ['B', '0', 'R'],
                            ['0', '0', 'B' ], ['0', '0', 'Y' ], ['0', '0', 'R']]) 
    
    
    
    ##---------------------------------------------------------------------------------
    
    
    global mask_height
    mask_height = None
    global mask_width 
    mask_width = None