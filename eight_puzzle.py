#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: ABdullahi Nur
# email: anur@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Fawzy Lawal
# partner's email: fawzy@bu.edu
#


from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()
            
            
            
def process_file(filename, algorithm, param):
    """ prints results for eight puzzle using the 3 parameters that are passed in
    inputs:
        a string filename
        a string algorithm
        paramter for searcher either a depth limit (for the uninformed search algorithms)
    """
    
    file = open(filename, 'r')
    
    count = 0
    avg_moves = 0
    avg_states = 0
    
    bool = True
    for line in file:
        digitstring = line[:-1]      # chop off newline at end
        
        init_board = Board(digitstring)
        init_state = State(init_board, None, 'init')
        searcher = create_searcher(algorithm, param)
        
        
        soln = None
        try:
            soln = searcher.find_solution(init_state)
        except KeyboardInterrupt:
            print('search terminated, ', end='')
        
        
    
        
            
        if soln == None:
            print(str(digitstring) + ': no solution.')
            bool = False
        else:
        
            avg_moves += soln.num_moves
            avg_states += searcher.num_tested
            count += 1
            print(str(digitstring) + ':', soln.num_moves, 'moves,', searcher.num_tested, 'states tested.')
    print('solved', count, 'puzzles')
    print('averages: ', avg_moves / count, 'moves,', avg_states / count, 'states tested.')
    file.close()
    
    if bool == False:
        
        print('solved', count, 'puzzles')
    
    
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

