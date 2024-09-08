import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
from consts import dict_final_states
from helpers import generate_random_initial_state


def main():
    G = nx.Graph()
    square_side_size = int(input("Digite o tamanho do lado do quadrado: "))
    if square_side_size in dict_final_states:
        final_state = dict_final_states.get(square_side_size)
    else:
        return print('Cadastre o estado final desejado no arquivo consts')

    initial_state = np.array(generate_random_initial_state(square_side_size))

    G.add_node(1, matriz=initial_state)

    return True


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        raise e
