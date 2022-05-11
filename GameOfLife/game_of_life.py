import random

SURROUNDING_COORDINATE = [(-1, -1), (0, -1), (1, -1),
                          (-1, 0), (1, 0),
                          (-1, 1), (0, 1), (1, 1)]


def random_state(height, width):
    """This function will take in 2 arguments
    your boards width and its height.
    ALIVE = 1; DEAD = 0
    :return
    """
    # Build the board using your previous work
    state = dead_state(width, height)

    # randomize each element of `state`  to either 0 or 1
    for i in range(len(state)):
        for j in range(len(state[i])):
            random_number = random.random()
            if random_number >= 0.39:
                state[i][j] = 0
            else:
                state[i][j] = 1

    return state


def dead_state(width, height):
    dead_state_grid = [[0 for x in range(height)] for x in range(width)]
    return dead_state_grid


def render(a_random_state):
    temp_state = a_random_state
    for i in range(len(temp_state)):
        for j in range(len(temp_state[i])):
            if temp_state[i][j] == 1:
                temp_state[i][j] = '#'
            elif temp_state[i][j] == 0:
                temp_state[i][j] = ' '
    # for i in range(len(temp_state)):
    #     temp_state[i].append('|')
    #     temp_state[i].insert(0, '|')
    print('- ' * (len(temp_state[0])))
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in temp_state]))
    print('- ' * (len(temp_state[0])))


def neighbours_position(x_position, y_position):
    result = []
    for dx, dy in SURROUNDING_COORDINATE:
        result.append((x_position + dx, y_position + dy))
    return result


def is_valid_neighbour(x_position, y_position, state):
    height = len(state)
    width = len(state[0])
    valid = True
    if x_position < 0 or y_position < 0 or x_position >= width or y_position >= height:
        valid = False
    return valid


def cell_is_alive(x_position, y_position, state):
    alive = True
    if state[x_position][y_position] != 1:
        alive = False
    return alive


def number_of_alive_neighbour(x_position, y_position, state):
    living_neighbour = 0
    list_of_pos = neighbours_position(x_position, y_position)
    for pos in list_of_pos:
        if is_valid_neighbour(pos[0], pos[1], state):
            if cell_is_alive(pos[0], pos[1], state):
                living_neighbour += 1
    return living_neighbour


def next_board_state(initial_state):
    new_state = dead_state(len(initial_state), len(initial_state[0]))
    for x_row in range(0, len(initial_state)):
        for y_column in range(0, len(initial_state[x_row])):
            if cell_is_alive(x_row, y_column, initial_state):
                if number_of_alive_neighbour(x_row, y_column, initial_state) in [2, 3]:
                    new_state[x_row][y_column] = 1
                else:
                    new_state[x_row][y_column] = 0
            else:
                if number_of_alive_neighbour(x_row, y_column, initial_state) == 3:
                    new_state[x_row][y_column] = 1
                else:
                    new_state[x_row][y_column] = 0

    return new_state
# https://codereview.stackexchange.com/questions/62160/checking-for-neighbours-more-elegantly-in-conways-game-of-life

