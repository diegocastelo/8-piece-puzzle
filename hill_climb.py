import numpy as np
from helpers import generate_next_states
import pandas as pd
from memory_profiler import memory_usage, profile


class HillClimb:
    def __init__(self, initial_state, final_state):
        self.initial_state = initial_state
        self.final_state = final_state

    def manhattan_distance(self, state, final_state):
        """
        Calcula a distância de Manhattan entre o estado atual e o estado final.
        """
        distance = 0
        for i in range(len(state)):
            for j in range(len(state[i])):
                current_value = state[i][j]
                if current_value != 0:  # Assume que 0 é o espaço vazio e não conta na distância
                    final_pos = np.argwhere(np.array(final_state) == current_value)[0]
                    distance += abs(i - final_pos[0]) + abs(j - final_pos[1])
        return distance

    def solve(self):
        initial_state_tuple = tuple(map(tuple, self.initial_state))
        final_state_tuple = tuple(map(tuple, self.final_state))

        current_state = initial_state_tuple
        path = []

        while True:
            path.append(current_state)

            # Geração dos próximos estados
            current_state_np = np.array(current_state)
            next_states = generate_next_states(current_state_np)

            # Transformar os próximos estados em tuplas
            formatted_states = [tuple(map(tuple, state)) for state in next_states]

            if not formatted_states:
                # Se não houver próximos estados, retornar None
                return None

            # Avaliar a distância de Manhattan para cada estado
            distances = [self.manhattan_distance(state, final_state_tuple) for state in formatted_states]

            # Escolher o estado com a menor distância de Manhattan
            min_distance = min(distances)

            # Filtrar os estados que têm a menor distância de Manhattan
            best_states = [formatted_states[i] for i, dist in enumerate(distances) if dist == min_distance]

            if not best_states:
                # Se não houver estados melhores, retornar o caminho atual
                return path

            # Converter best_states para um array unidimensional
            best_states_array = np.array(best_states)

            # Escolher um estado aleatoriamente entre os melhores
            next_state = best_states_array[np.random.choice(best_states_array.shape[0])]
            next_state = tuple(map(tuple, next_state))
            if next_state == final_state_tuple:
                # Se o próximo estado for o estado final, retornar o caminho final
                path.append(next_state)
                return path

            # Mover para o próximo estado
            current_state = next_state
