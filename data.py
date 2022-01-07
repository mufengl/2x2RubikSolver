import numpy as np

pos_x = np.array([1, 0, 0])
neg_x = np.array([-1, 0, 0])
pos_y = np.array([0, 1, 0])
neg_y = np.array([0, -1, 0])
pos_z = np.array([0, 0, 1])
neg_z = np.array([0, 0, -1])

cords = np.array([[pos_x, pos_y, pos_z],
                  [neg_x, pos_y, pos_z],
                  [neg_x, neg_y, pos_z],
                  [pos_x, neg_y, pos_z],
                  [pos_x, pos_y, neg_z],
                  [neg_x, pos_y, neg_z],
                  [neg_x, neg_y, neg_z],
                  [pos_x, neg_y, neg_z]])

left_matrix = np.array([[0, 1, 0],
                        [-1, 0, 0],
                        [0, 0, 1]])

right_matrix = np.array([[0, -1, 0],
                         [1, 0, 0],
                         [0, 0, 1]])

front_matrix = np.array([[1, 0, 0],
                         [0, 0, -1],
                         [0, 1, 0]])

back_matrix = np.array([[1, 0, 0],
                        [0, 0, 1],
                        [0, -1, 0]])

top_matrix = np.array([[0, 0, 1],
                       [0, 1, 0],
                       [-1, 0, 0]])

bottom_matrix = np.array([[0, 0, -1],
                          [0, 1, 0],
                          [1, 0, 0]])

