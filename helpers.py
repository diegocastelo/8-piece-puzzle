import numpy as np
import random


def generate_next_states(node):
    possible_next_states = []
    pos = np.argwhere(node == 'b')[0]
    i, j = pos

    directions = {
        'right': (i, j + 1),
        'left': (i, j - 1),
        'up': (i - 1, j),
        'down': (i + 1, j)
    }
    for direction, (neighbor_i, neighbor_j) in directions.items():
        if 0 <= neighbor_i < node.shape[0] and 0 <= neighbor_j < node.shape[1]:
            new_state = node.copy()
            new_state[i, j], new_state[neighbor_i, neighbor_j] = new_state[neighbor_i, neighbor_j], new_state[i, j]
            possible_next_states.append(new_state)

    return possible_next_states


def generate_random_initial_state(square_side_size: int):
    array = list(range(1, square_side_size ** 2)) + ['b']

    # Gerar a matriz preenchida com 'x'
    matrix = np.full((square_side_size, square_side_size), 'x', dtype=object)

    count_x = 0
    count_y = 0
    while len(array) != 0:
        random_index = random.randint(0, len(array) - 1)
        element = array[random_index]
        array.pop(random_index)
        matrix[count_x][count_y] = element
        if count_y == (square_side_size - 1):
            count_x += 1
            count_y = 0
        else:
            count_y += 1

    return matrix

