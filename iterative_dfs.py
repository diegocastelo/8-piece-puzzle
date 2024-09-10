import numpy as np
from helpers import generate_next_states


class IterativeDFS:
    def __init__(self, initial_state, final_state):
        self.initial_state = initial_state
        self.final_state = final_state

    def solve(self, max_depth=100):
        for depth in range(max_depth):
            initial_state_tuple = tuple(map(tuple, self.initial_state))
            final_state_tuple = tuple(map(tuple, self.final_state))

            stack = [(initial_state_tuple, [], 0)]

            visited = set()

            while stack:
                current_state, path, current_depth = stack.pop()
                if current_depth > depth:
                    continue
                if current_state in visited:
                    continue

                visited.add(current_state)

                if current_state == final_state_tuple:
                    return path

                for next_state in generate_next_states(np.array(current_state)):
                    next_state_tuple = tuple(map(tuple, next_state))
                    stack.append((next_state_tuple, path + [next_state], current_depth + 1))

        return None
