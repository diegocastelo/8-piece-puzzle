import numpy as np
from helpers import generate_next_states

class DFS:
    def __init__(self, initial_state, final_state):
        self.initial_state = initial_state
        self.final_state = final_state

    def solve(self):
        initial_state_tuple = tuple(map(tuple, self.initial_state))
        final_state_tuple = tuple(map(tuple, self.final_state))

        stack = [(initial_state_tuple, [])]

        visited = set()
        visited.add(initial_state_tuple)
        stack_length = len(stack)
        while stack:
            if stack_length < len(stack):
                stack_length = len(stack)
                print(stack_length)
            current_state, path = stack.pop()
            if current_state == final_state_tuple:
                return path
            current_state = np.array(current_state)
            next_states = generate_next_states(current_state)

            for next_state in next_states:
                next_state_tuple = tuple(map(tuple, next_state))
                stack.append((next_state_tuple, path + [next_state]))

        return None
