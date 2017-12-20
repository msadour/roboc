from function_lib import *

class Robot():
    def __init__(self,nickname, position=(2,2)):
        self.nickname = nickname
        self.position = position #it's the position of the gamer. it's look : (line, col)

    def move(self, direction ,nb_move, labirynth):
        """"
        this methode take a direction and a number of case. If the position which we played is free
        (not contain the value '0'), the robot go to this position. if the value position is '@',
        the game is finish.
        """
        current_line = self.position[0]
        current_col = self.position[1]

        if direction == "o":
            next_position = (current_line, current_col-nb_move)
        elif direction == "e":
            next_position = (current_line, current_col+nb_move)
        elif direction == "n":
            next_position = (current_line-nb_move, current_col)
        elif direction == "s":
            next_position = (current_line+nb_move, current_col)
        else:
            next_position = (current_line, current_col)

        if labirynth.board[next_position[0]-1][next_position[1]-1] == '0':
            pass
        elif labirynth.board[next_position[0]-1][next_position[1]-1] == '$':
            self.position = next_position
            labirynth.change_state(current_line, current_col, next_position[0], next_position[1])
            return 'win'
        else:
            self.position = next_position
            labirynth.change_state(current_line, current_col, next_position[0], next_position[1])
            return (next_position[0], next_position[1])


class Labirynth():
    def __init__(self, level, position):
        """"
        the function make_board return a tuple with board (by the level) and the level.
        """
        self.board = make_board(level)[1]
        self.level = make_board(level)[0]
        if position:
            self.board[1][1] = " "
            self.board[position[0] - 1][position[1] - 1] = "@"

    def change_state(self, old_line, old_col, new_line, new_col):
        """"
        change the value of a field when the robot change of position
        """
        self.board[old_line-1][old_col-1] = " "
        self.board[new_line-1][new_col-1] = "@"

    def __repr__(self):
        good_display = ""
        nb_col = 0
        if self.level == "enfant":
            nb_col = 7
        elif self.level == "facile":
            nb_col = 12
        elif self.level == "moyen":
            nb_col = 17
        elif self.level == "difficile":
            nb_col = 22
        elif self.level == "enfer":
            nb_col = 32

        for line in self.board:
            for idx, elm in enumerate(line):
                good_display = good_display + elm + "  "
                if idx+1 == nb_col:
                    good_display = good_display + "\n"
        return good_display
