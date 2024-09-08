import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random


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
        if count_y == (square_side_size-1):
            count_x += 1
            count_y = 0
        else:
            count_y += 1

    return matrix

if __name__ == '__main__':
    G = nx.Graph()

    initial_state = np.array(generate_random_initial_state(5))

    G.add_node(1, matriz=initial_state)

