from collections import deque
import numpy as np
from helpers import generate_next_states, verify_correct_pieces
import pandas as pd


class Greedy:
    def __init__(self, initial_state, final_state):
        self.initial_state = initial_state
        self.final_state = final_state

    def solve(self):
        initial_state_tuple = tuple(map(tuple, self.initial_state))
        final_state_tuple = tuple(map(tuple, self.final_state))

        queue = deque([(initial_state_tuple, [])])

        visited = set()
        visited.add(initial_state_tuple)
        last_visited = None
        queue_length = len(queue[0][1])

        while queue:
            if queue_length < len(queue[0][1]):
                queue_length = len(queue[0][1])

            current_state, path = queue.popleft()
            if current_state == final_state_tuple:
                print(f'Tamanho máximo da lista: {queue_length}')
                return path

            current_state_np = np.array(current_state)
            next_states = generate_next_states(current_state_np)
            if last_visited is not None:
                next_states = [state for state in next_states if not np.array_equal(state, last_visited)]

            formatted_states = [list(map(list, sublist)) for sublist in next_states]
            df_states = pd.DataFrame({'state': formatted_states})

            df_states['num_correct_pieces'] = df_states.apply(lambda row: verify_correct_pieces(row['state'], final_state_tuple), axis=1)

            max_correct_pieces = df_states['num_correct_pieces'].max()

            # Filtrar os estados que têm o número máximo de peças corretas
            filtered_df = df_states[df_states['num_correct_pieces'] == max_correct_pieces]

            # Escolher um estado aleatoriamente entre os filtrados
            next_state = filtered_df['state'].sample(n=1).iloc[0]

            next_state_tuple = tuple(map(tuple, next_state))

            last_visited = current_state_np

            queue.append((next_state_tuple, path + [next_state]))

        return None