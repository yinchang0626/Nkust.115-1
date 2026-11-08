def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # 檢查列與行
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    # 檢查對角線
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    for _ in range(9):
        print_board(board)
        try:
            row, col = map(int, input(f"玩家 {current_player} 請輸入列與行 (0-2，以空白分隔，例如 '0 1'): ").split())
            if board[row][col] == " ":
                board[row][col] = current_player
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"玩家 {current_player} 獲勝！")
                    return
                current_player = "O" if current_player == "X" else "X"
            else:
                print("這個位置已經被佔用了，請重新輸入。")
        except (ValueError, IndexError):
            print("輸入無效，請確保輸入的是兩個 0 到 2 之間的數字。")
            
    print_board(board)
    print("平手！")

if __name__ == "__main__":
    main()