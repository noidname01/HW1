import numpy as np

def p1_has_cycle(sets):
    # TODO
    # return True if the graph has cycle; return False if not
    '''
      HINT: You can `print(sets)` to show what the matrix looks like
        If we have a directed graph with 2->3 4->1 3->5 5->2 0->1
               0  1  2  3  4  5
            0  0  0 -1  1  0  0
            1  0  1  0  0 -1  0
            2  0  0  0 -1  0  1
            3  0  0  1  0  0 -1
            4 -1  1  0  0  0  0
        The size of the matrix is (5,6)
    '''
    return False

