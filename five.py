# 创建五子棋棋盘
def create_board():
    board = []
    for _ in range(15):
        row = ['+'] * 15
        board.append(row)
    return board

# 打印棋盘
def print_board(board):
    for row in board:
        print(' '.join(row))

# 判断是否五子连珠
def check_win(board, player, row, col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    for d in directions:
        count = 1
        dx, dy = d
        x, y = row + dx, col + dy
        while 0 <= x < 15 and 0 <= y < 15 and board[x][y] == player:
            count += 1
            x += dx
            y += dy
        x, y = row - dx, col - dy
        while 0 <= x < 15 and 0 <= y < 15 and board[x][y] == player:
            count += 1
            x -= dx
            y -= dy
        if count >= 5:
            return True
    return False

# 主程序
def main():
    board = create_board()
    players = ['X', 'O']
    current_player = 0
    print_board(board)
    
    while True:
        player = players[current_player]
        move = input(f"Player {player}, enter your move (row col): ")
        row, col = map(int, move.split())
        
        if board[row][col] != '+':
            print("Invalid move. Try again.")
            continue
        
        board[row][col] = player
        print_board(board)
        
        if check_win(board, player, row, col):
            print(f"Player {player} wins!")
            break
        
        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    main()
