def is_valid(board):
    if len(board) % 3 != 0 :
        raise Exception("The size must be a multiple of 3") 
    section_summary = len(board) * (len(board) + 1) / 2
    #row
    for x in board:
        if sum(x) != section_summary:
            #print("1")
            return False
    #collumn
    for x in range(len(board)):
        number_sum = 0
        for y in board:
            number_sum += y[x]
        if number_sum != section_summary:
            #print("2")
            return False
    #cube
    cube_width_count = int(len(board) / 3)
    for i in range(0, cube_width_count, 1):
        for j in range(0, cube_width_count, 1):
            number_sum = 0
            y, x = 0, 0
            for k in range(9):
                number_sum += board[k // 3 + i * 3][k % 3 + j * 3]
                #print(board[k // 3 + i * 3][k % 3 + j * 3])
                #print(f"y: {k // 3 + i * 3}, x: {k % 3 + j * 3}")
            if number_sum != section_summary:
                #print("3")
                return False
    return True