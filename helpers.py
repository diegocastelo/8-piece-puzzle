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

def verify_correct_pieces(current_state, final_state):
    current_state = tuple(map(tuple, current_state))
    if current_state == final_state:
        return 9
    else:
        return sum(1 for (row1, row2) in zip(current_state, final_state)
                           for (elem1, elem2) in zip(row1, row2)
                           if elem1 == elem2)

def generate_random_initial_state(moves, final_state):
    state = final_state

    for i in range(moves):
        possible_next_states = generate_next_states(state)
        state = random.choice(possible_next_states)

    return state

