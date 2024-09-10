from collections import deque
import numpy as np
from helpers import generate_next_states


class BFS:
    def __init__(self, initial_state, final_state):
        self.initial_state = initial_state
        self.final_state = final_state

    def solve(self):
        initial_state_tuple = tuple(map(tuple, self.initial_state))
        final_state_tuple = tuple(map(tuple, self.final_state))

        queue = deque([(initial_state_tuple, [])])

        visited = set()
        visited.add(initial_state_tuple)
        while queue:
            current_state, path = queue.popleft()
            if current_state == final_state_tuple:
                return path
            current_state_np = np.array(current_state)
            next_states = generate_next_states(current_state_np)

            for next_state in next_states:
                next_state_tuple = tuple(map(tuple, next_state))
                if next_state_tuple not in visited:
                    visited.add(next_state_tuple)
                    queue.append((next_state_tuple, path + [next_state]))
        return None
