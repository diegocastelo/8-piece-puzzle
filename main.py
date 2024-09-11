import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
from consts import dict_final_states
from helpers import generate_random_initial_state
from bfs import BFS
from dfs import DFS
from iterative_dfs import IterativeDFS
from greedy import Greedy
from hill_climb import HillClimb
from memory_profiler import memory_usage, profile
import time


def main():
    square_side_size = int(input("Digite o tamanho do lado do quadrado: "))
    if square_side_size in dict_final_states:
        final_state = dict_final_states.get(square_side_size)
    else:
        return print('Cadastre o estado final desejado no arquivo consts')
    initial_state = np.array(generate_random_initial_state(25, final_state))
    initial_state = np.array([['5', '6', '3'], ['2', '7', '8'], ['1', '4', 'b']])
    # initial_state = np.array([['8', '1', '3'], ['2', 'b', '4'], ['7', '6', '5']])
    # initial_state = np.array([['1', '2', '3', '4'], ['12', '15', '13', '5'], ['10', '11', '14', '7'], ['b', '9', '6', '8']])
    # initial_state = np.array([['1', '2', '3', '4'], ['9', '12', '13', '5'], ['b', '15', '14', '7'], ['11', '10', '6', '8']])

    bfs = BFS(initial_state, final_state)
    inicio = time.time()
    path_bfs = bfs.solve()
    fim = time.time()
    tempo_total_bfs = fim - inicio

    # dfs = DFS(initial_state, final_state)
    # inicio = time.time()
    # path_dfs = dfs.solve()
    # fim = time.time()
    # tempo_total_dfs = fim - inicio

    idfs = IterativeDFS(initial_state, final_state)
    inicio = time.time()
    path_idfs = idfs.solve()
    fim = time.time()
    tempo_total_idfs = fim - inicio

    greedy = Greedy(initial_state, final_state)
    inicio = time.time()
    path_greedy = greedy.solve()
    fim = time.time()
    tempo_total_greedy = fim - inicio

    hillClimb = HillClimb(initial_state, final_state)
    inicio = time.time()
    path_hillclimb = hillClimb.solve()
    fim = time.time()
    tempo_total_hillclimb = fim - inicio

    return True


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        raise e
