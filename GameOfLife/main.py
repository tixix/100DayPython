from game_of_life import next_board_state
from game_of_life import render

init_state = [

    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]
render(init_state)
print(init_state)
print(next_board_state(init_state))
# while True:

