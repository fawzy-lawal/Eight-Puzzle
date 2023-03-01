#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: ABdullahi Nur
# email: anur@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Fawzy Lawal
# partner's email: fawzy@bu.edu
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [['1'] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        #print(self.tiles)
        count = 0
        #print(len(self.tiles))
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[row])):
                self.tiles[row][col] = digitstr[count]
                count += 1
                if self.tiles[row][col] == '0':
                    """print(row)
                    print(col)"""
                    self.blank_r = row
                    self.blank_c = col
                    
    ### Add your other method definitions below. ###

    def __repr__(self):
        """ returns a string representation of a Board object
        """
        s = ''

        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[row])):
                if self.tiles[row][col] == '0':
                    s += '_' + ' '
                else:
                    s += self.tiles[row][col] + ' '
            s += '\n'
        return s
    
    def move_blank(self, direction):
        """ input a string direction that specifies the direction in which the blank should move
            The method should return True or False to indicate whether the requested move was possible.
        """
        new_row = self.blank_r
        new_col = self.blank_c
        """print(new_row)
        print(new_col)"""
        
        
        
        if direction == 'up':
            new_row = self.blank_r - 1
            
        elif direction == 'down':
            new_row = self.blank_r + 1
            
        elif direction == 'left':
            new_col = self.blank_c - 1
            
        elif direction == 'right':
            new_col = self.blank_c + 1
            
        else:
            return False
            
        if new_row < 0 or new_row >= 3: 
            return False
        elif new_col < 0 or new_col >= 3:
            return False
        else:
            
            self.tiles[self.blank_r][self.blank_c] = self.tiles[new_row][new_col]
            self.tiles[new_row][new_col] = '0'
            
            self.blank_r = new_row
            self.blank_c = new_col
    
            return True
        
        
    def digit_string(self):
        """ returns the string of digits that was used when creating the Board.
            string returned by digit_string() should reflect any changes that have
            been made to the tiles
        """
        s = ''
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[row])):
                s += self.tiles[row][col]
        return s
        
    def copy(self):
        """ returns a newly-constructed Board object that is a deep 
            copy of the called object
        """
        new_digit = self.digit_string()
        new_board = Board(new_digit)
        return new_board
    
    def num_misplaced(self):
        """ counts and returns the number of tiles in the called Board 
            object that are not where they should be in the goal state
        """
        count = 0
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[row])):
                if self.tiles[row][col] != GOAL_TILES[row][col]:
                    count += 1
        return count - 1
    
    def __eq__(self, other):
        """  return True if the called object (self) and the argument 
            (other) have the same values for the tiles attribute, and False otherwise.
        """
        if self.tiles == other.tiles:
            return True
        return False































