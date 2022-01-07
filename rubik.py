from copy import deepcopy

from data import *


class piece:

    def __init__(self, colors, xyz):
        assert len(colors) == 3
        self.color = colors
        self.xyz = xyz

    def printer(self):
        print(self.color, self.xyz.tolist())


# to do:
# 1) initialize piece given colors and orientation
# 2) change orientation
# 3)

class cubes:
    moves = ''

    def __init__(self, cube_input):
        color = [[cube_input[5], cube_input[3], cube_input[13]],
                 [cube_input[23], cube_input[1], cube_input[19]],
                 [cube_input[21], cube_input[17], cube_input[18]],
                 [cube_input[7], cube_input[11], cube_input[12]],
                 [cube_input[4], cube_input[2], cube_input[8]],
                 [cube_input[22], cube_input[0], cube_input[14]],
                 [cube_input[20], cube_input[16], cube_input[15]],
                 [cube_input[6], cube_input[10], cube_input[9]]]

        self.pieces = []

        for x in range(len(color)):
            self.pieces.append(piece(color[x], cords[x]))

    # left move cw
    def left_turn(self):
        # storage
        temp_array1 = np.copy(self.pieces[7].xyz)
        temp = self.pieces[4].color

        # calculating new orientations in their new positions

        for x in range(len(self.pieces[4].xyz)):
            self.pieces[7].xyz[x] = np.dot(left_matrix, self.pieces[4].xyz[x])

        self.pieces[4].color = self.pieces[5].color

        for x in range(len(self.pieces[5].xyz)):
            self.pieces[4].xyz[x] = np.dot(left_matrix, self.pieces[5].xyz[x])

        self.pieces[5].color = self.pieces[6].color

        for x in range(len(self.pieces[6].xyz)):
            self.pieces[5].xyz[x] = np.dot(left_matrix, self.pieces[6].xyz[x])

        self.pieces[6].color = self.pieces[7].color

        for x in range(len(temp_array1)):
            self.pieces[6].xyz[x] = np.dot(left_matrix, temp_array1[x])

        self.pieces[7].color = temp
        self.moves = self.moves + "L "

    # left move ccw
    def left_prime(self):
        for x in range(3):
            self.left_turn()

        self.moves = self.moves[:-6] + "L' "

    # right move cw
    def right_turn(self):
        # storage
        temp_array1 = np.copy(self.pieces[0].xyz)
        temp = deepcopy(self.pieces[3].color)

        # calculating new orientations in their new positions

        for x in range(len(self.pieces[3].xyz)):
            self.pieces[0].xyz[x] = np.dot(right_matrix, self.pieces[3].xyz[x])

        self.pieces[3].color = self.pieces[2].color

        for x in range(len(self.pieces[2].xyz)):
            self.pieces[3].xyz[x] = np.dot(right_matrix, self.pieces[2].xyz[x])

        self.pieces[2].color = self.pieces[1].color

        for x in range(len(self.pieces[1].xyz)):
            self.pieces[2].xyz[x] = np.dot(right_matrix, self.pieces[1].xyz[x])

        self.pieces[1].color = self.pieces[0].color

        for x in range(len(temp_array1)):
            self.pieces[1].xyz[x] = np.dot(right_matrix, temp_array1[x])

        self.pieces[0].color = temp
        self.moves = self.moves + "R "

    # right move ccw
    def right_prime(self):
        for x in range(3):
            self.right_turn()

        self.moves = self.moves[:-6] + "R' "

    # front move cw
    def front_turn(self):
        # storage
        temp_array1 = np.copy(self.pieces[4].xyz)
        temp = deepcopy(self.pieces[7].color)

        # calculating new orientations in their new positions

        for x in range(len(self.pieces[7].xyz)):
            self.pieces[4].xyz[x] = np.dot(front_matrix, self.pieces[7].xyz[x])

        self.pieces[7].color = self.pieces[3].color

        for x in range(len(self.pieces[3].xyz)):
            self.pieces[7].xyz[x] = np.dot(front_matrix, self.pieces[3].xyz[x])

        self.pieces[3].color = self.pieces[0].color

        for x in range(len(self.pieces[0].xyz)):
            self.pieces[3].xyz[x] = np.dot(front_matrix, self.pieces[0].xyz[x])

        self.pieces[0].color = self.pieces[4].color

        for x in range(len(temp_array1)):
            self.pieces[0].xyz[x] = np.dot(front_matrix, temp_array1[x])

        self.pieces[4].color = temp

        self.moves = self.moves + "F "

    # front move ccw
    def front_prime(self):
        for x in range(3):
            self.front_turn()

        self.moves = self.moves[:-6] + "F' "

    # back move cw
    def back_turn(self):
        # storage
        temp_array1 = np.copy(self.pieces[6].xyz)
        temp = deepcopy(self.pieces[5].color)

        # calculating new orientations in their new positions

        for x in range(len(self.pieces[5].xyz)):
            self.pieces[6].xyz[x] = np.dot(back_matrix, self.pieces[5].xyz[x])

        self.pieces[5].color = self.pieces[1].color

        for x in range(len(self.pieces[1].xyz)):
            self.pieces[5].xyz[x] = np.dot(back_matrix, self.pieces[1].xyz[x])

        self.pieces[1].color = self.pieces[2].color

        for x in range(len(self.pieces[2].xyz)):
            self.pieces[1].xyz[x] = np.dot(back_matrix, self.pieces[2].xyz[x])

        self.pieces[2].color = self.pieces[6].color

        for x in range(len(temp_array1)):
            self.pieces[2].xyz[x] = np.dot(back_matrix, temp_array1[x])

        self.pieces[6].color = temp

        self.moves = self.moves + "B "

    # back move ccw
    def back_prime(self):
        for x in range(3):
            self.back_turn()
        self.moves = self.moves[:-6] + "B' "

    # top move cw
    def top_turn(self):
        # storage
        temp_array1 = np.copy(self.pieces[5].xyz)
        temp = deepcopy(self.pieces[4].color)

        # calculating new orientations in their new positions

        for x in range(len(self.pieces[4].xyz)):
            self.pieces[5].xyz[x] = np.dot(top_matrix, self.pieces[4].xyz[x])

        self.pieces[4].color = self.pieces[0].color

        for x in range(len(self.pieces[0].xyz)):
            self.pieces[4].xyz[x] = np.dot(top_matrix, self.pieces[0].xyz[x])

        self.pieces[0].color = self.pieces[1].color

        for x in range(len(self.pieces[1].xyz)):
            self.pieces[0].xyz[x] = np.dot(top_matrix, self.pieces[1].xyz[x])

        self.pieces[1].color = self.pieces[5].color

        for x in range(len(temp_array1)):
            self.pieces[1].xyz[x] = np.dot(top_matrix, temp_array1[x])

        self.pieces[5].color = temp

        self.moves = self.moves + "U "

    # top move ccw
    def top_prime(self):
        for x in range(3):
            self.top_turn()
        self.moves = self.moves[:-6] + "U' "

    # bot move cw
    def bot_turn(self):
        # storage
        temp_array1 = np.copy(self.pieces[2].xyz)
        temp = deepcopy(self.pieces[3].color)

        # calculating new orientations in their new positions

        for x in range(len(self.pieces[3].xyz)):
            self.pieces[2].xyz[x] = np.dot(bottom_matrix, self.pieces[3].xyz[x])

        self.pieces[3].color = self.pieces[7].color

        for x in range(len(self.pieces[7].xyz)):
            self.pieces[3].xyz[x] = np.dot(bottom_matrix, self.pieces[7].xyz[x])

        self.pieces[7].color = self.pieces[6].color

        for x in range(len(self.pieces[6].xyz)):
            self.pieces[7].xyz[x] = np.dot(bottom_matrix, self.pieces[6].xyz[x])

        self.pieces[6].color = self.pieces[2].color

        for x in range(len(temp_array1)):
            self.pieces[6].xyz[x] = np.dot(bottom_matrix, temp_array1[x])

        self.pieces[2].color = temp

        self.moves = self.moves + "D "

    # bot move ccw
    def bot_prime(self):
        for x in range(3):
            self.bot_turn()
        self.moves = self.moves[:-6] + "D' "

    def get_dir_color(self, x, pos):
        index = np.where(np.all(self.pieces[x].xyz == pos, axis=1))
        return self.pieces[x].color[index[0][0]]

    def get_color_dir(self, x, color):
        index = self.pieces[x].color.index(color)
        return self.pieces[x].xyz[index]

    def solve(self):
        self.position_fl()

        self.orientate_fl()

        self.position_ll()

        check = self.orientate_ll()
        if not check:
            return False
        else:
            return self.moves

    def position_fl(self):
        self.get_piece2()
        self.get_piece7()
        self.get_piece6()

    def get_piece2(self):
        bot_color = self.get_dir_color(3, neg_y)
        right_color = self.get_dir_color(3, pos_z)
        piece2_pos = -1  # initialize

        # first check if the piece is already in the right position
        if self.check_color(2, bot_color, right_color):
            return

        for x in range(len(self.pieces)):
            if x == 3:
                continue
            if bot_color in self.pieces[x].color and right_color in self.pieces[x].color:
                piece2_pos = x
                break

        # piece 2 could be in pos 0, 1, 4, 5, 6, 7

        if piece2_pos == 0:
            self.top_prime()
            self.back_prime()

        elif piece2_pos == 1:
            self.back_prime()

        elif piece2_pos == 4:
            self.top_turn()
            self.top_turn()
            self.back_prime()

        elif piece2_pos == 5:
            self.back_prime()
            self.back_prime()

        elif piece2_pos == 6:
            self.back_turn()

        else:
            self.left_turn()
            self.back_turn()

        # piece 2 in correct position

    def get_piece7(self):
        bot_color = self.get_dir_color(3, neg_y)
        front_color = self.get_dir_color(3, pos_x)
        piece7_pos = -1  # initialize
        # first check if the piece is already in the right position
        if self.check_color(7, bot_color, front_color):
            return

        for x in range(len(self.pieces)):
            if x == 3 or x == 2:
                continue
            if bot_color in self.pieces[x].color and front_color in self.pieces[x].color:
                piece7_pos = x
                break

        # piece 7 could be in pos 0, 1, 4, 5, 6

        if piece7_pos == 0:
            self.top_turn()
            self.left_turn()

        elif piece7_pos == 1:
            self.top_turn()
            self.top_turn()
            self.left_turn()

        elif piece7_pos == 4:
            self.left_turn()

        elif piece7_pos == 5:
            self.left_turn()
            self.left_turn()

        else:
            self.left_prime()

    def get_piece6(self):
        bot_color = self.get_dir_color(3, neg_y)
        piece6_pos = -1  # initialize

        for x in range(len(self.pieces)):
            if x == 3 or x == 2 or x == 7:
                continue
            if bot_color in self.pieces[x].color:
                piece6_pos = x
                break
        if piece6_pos == 6:
            return

        # piece 6 could be in pos 0, 1, 4, 5

        if piece6_pos != 5:
            if piece6_pos == 0:
                self.top_turn()
                self.top_turn()
            elif piece6_pos == 1:
                self.top_prime()
            else:
                self.top_turn()

        self.back_prime()
        self.top_prime()
        self.back_turn()

    def check_orientation(self, x, pos, target_color):
        current = self.get_dir_color(x, pos)
        if current == target_color:
            return True
        else:
            return False

    def check_color(self, x, color1, color2):
        if color1 in self.pieces[x].color and color2 in self.pieces[x].color:
            return True
        else:
            return False

    def orientate_fl(self):
        bot_color = self.get_dir_color(3, neg_y)

        # check orientation of piece 2

        for x in range(3):
            counter = 0
            self.bot_prime()
            orientation = self.check_orientation(3, neg_y, bot_color)

            while not orientation:
                self.orientate_bot_corner()
                orientation = self.check_orientation(3, neg_y, bot_color)
                counter += 1

                # exit if cube is impossible to solve

                if counter > 5:
                    return False
        self.bot_prime()
        return True

    def position_ll(self):
        front_color = self.get_dir_color(3, pos_x)
        right_color = self.get_dir_color(3, pos_z)
        back_color = self.get_dir_color(6, neg_x)
        left_color = self.get_dir_color(6, neg_z)
        piece0_correct = self.check_color(0, right_color, front_color)

        while not piece0_correct:
            self.top_turn()
            piece0_correct = self.check_color(0, right_color, front_color)

        # either all false or 1 false
        pieces_correct = [self.check_color(1, right_color, front_color),
                          self.check_color(5, back_color, left_color),
                          self.check_color(4, right_color, front_color)]

        pieces_incorrect = pieces_correct.count(False)

        if pieces_incorrect == 3:
            while pieces_incorrect == 3:
                self.three_corners_ccw()

                pieces_correct = [self.check_color(1, right_color, back_color),
                                  self.check_color(5, back_color, left_color),
                                  self.check_color(4, left_color, front_color)]
                pieces_incorrect = pieces_correct.count(False)

        pieces_correct = [self.check_color(1, right_color, back_color),
                          self.check_color(5, back_color, left_color),
                          self.check_color(4, left_color, front_color)]

        if not all(pieces_correct):
            if pieces_correct[1]:
                self.diagonal_swap()
            if pieces_correct[0]:
                self.top_prime()
                self.front_swap()
                self.top_turn()
            if pieces_correct[2]:
                self.top_prime()
                self.top_prime()
                self.front_swap()
                self.top_turn()
                self.top_turn()

    def three_corners_ccw(self):
        self.top_turn()
        self.right_turn()
        self.top_prime()
        self.left_prime()
        self.top_turn()
        self.right_prime()
        self.top_prime()
        self.left_turn()

    def diagonal_swap(self):
        self.front_prime()
        self.right_prime()
        self.front_prime()
        self.right_turn()
        self.bot_turn()
        self.right_turn()
        self.bot_prime()

    def front_swap(self):
        self.left_turn()
        self.front_prime()
        self.left_prime()
        self.bot_prime()
        self.left_prime()
        self.bot_turn()
        self.front_turn()

    def orientate_ll(self):
        front_color = self.get_dir_color(3, pos_x)
        right_color = self.get_dir_color(3, pos_z)

        # check orientation of piece 0
        orientation_p0 = [self.check_orientation(0, pos_x, front_color),
                          self.check_orientation(0, pos_z, right_color)]
        while not all(orientation_p0):
            self.orientate_top_corner()

            orientation_p0 = [self.check_orientation(0, pos_x, front_color),
                              self.check_orientation(0, pos_z, right_color)]

        top_color = self.get_dir_color(0, pos_y)

        for x in range(3):
            counter = 0
            self.top_turn()
            orientation = self.check_orientation(0, pos_y, top_color)

            while not orientation:
                self.orientate_top_corner()
                orientation = self.check_orientation(0, pos_y, top_color)
                counter += 1

                # exit if cube is impossible to solve

                if counter > 5:
                    return False
        self.top_turn()
        return True

    def orientate_top_corner(self):
        self.right_prime()
        self.bot_prime()
        self.right_turn()
        self.bot_turn()

    def orientate_bot_corner(self):
        self.right_turn()
        self.top_turn()
        self.right_prime()
        self.top_prime()

    def print_cube(self):
        for x in self.pieces:
            x.printer()
