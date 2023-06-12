def check_surroundings(board, x, y):
    number_list = []
    for i in board[y]:
        if i != 0 and i not in number_list:
            number_list.append(i)
    for i in board:
        if i[x] != 0 and i[x] not in number_list:
            number_list.append(i[x])
    cube_x, cube_y = x // 3, y // 3
    for j in range(3):
        for k in range(3):
            current_location = board[j + cube_y * 3][k + cube_x * 3]
            if current_location != 0 and current_location not in number_list:
                number_list.append(current_location)
    return number_list

def find_zeros(board) -> list:
    zero_list = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                zero_list.append((j, i))  # (x, y)
    return zero_list


def solve(board):
    current_index = 0
    zero_list = find_zeros(board)
    while current_index < len(zero_list):
        print(current_index)
        x, y = zero_list[current_index]
        surroundings = check_surroundings(board, x, y)
        been_here = False
        for k in range(board[y][x] + 1, 10):
            if k not in surroundings:
                been_here = True
                print(f"OHAA {k}")
                board[y][x] = k
                current_index += 1
                break
        if board[y][x] == 0 or not been_here:
            board[y][x] = 0
            current_index -= 1
    return board