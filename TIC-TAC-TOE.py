import math
import time

HUMAN = "🙂"
AI = "🤖"
EMPTY = " "

num_to_pos = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2)
}

def show_demo_board():
    print("\n📌 Board positions (Demo):\n")
    print(" 1 | 2 | 3 ")
    print("— — — — —")
    print(" 4 | 5 | 6 ")
    print("— — — — —")
    print(" 7 | 8 | 9 \n")

def print_board(board):
    print()
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("— — — — —")
    print()

def check_winner(board):
    lines = [
        [(0,0),(0,1),(0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)], [(0,1),(1,1),(2,1)], [(0,2),(1,2),(2,2)],
        [(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)]
    ]

    for line in lines:
        values = [board[r][c] for r, c in line]
        if values[0] != EMPTY and values.count(values[0]) == 3:
            return values[0]

    for row in board:
        if EMPTY in row:
            return None
    return "Draw"

def minimax(board, is_max):
    result = check_winner(board)
    if result == AI:
        return 1
    if result == HUMAN:
        return -1
    if result == "Draw":
        return 0

    if is_max:
        best = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == EMPTY:
                    board[r][c] = AI
                    best = max(best, minimax(board, False))
                    board[r][c] = EMPTY
        return best
    else:
        best = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == EMPTY:
                    board[r][c] = HUMAN
                    best = min(best, minimax(board, True))
                    board[r][c] = EMPTY
        return best

def ai_move(board):
    best_score = -math.inf
    move = None
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                board[r][c] = AI
                score = minimax(board, False)
                board[r][c] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (r, c)
    board[move[0]][move[1]] = AI

def human_move(board):
    while True:
        try:
            choice = int(input("Choose a position (1-9): "))
            if choice not in num_to_pos:
                print("❌ Enter number between 1 and 9.")
                continue

            r, c = num_to_pos[choice]
            if board[r][c] == EMPTY:
                board[r][c] = HUMAN
                break
            else:
                print("❌ That position is already taken.")
        except:
            print("❌ Invalid input.")

def main():
    board = [[EMPTY]*3 for _ in range(3)]

    show_demo_board()
    player_name = input("Enter your name: ").strip() or "Player"

    print(f"\n🙂 {player_name} vs 🤖 AI")
    print("You play first!\n")

    print_board(board)

    while True:
        print(f"🙂 {player_name}'s move")
        human_move(board)
        print_board(board)

        result = check_winner(board)
        if result:
            break

        print("🤖 AI is thinking...")
        time.sleep(1)
        ai_move(board)
        print_board(board)

        result = check_winner(board)
        if result:
            break

    if result == HUMAN:
        print(f"🎉 🙂 {player_name} WINS!")
    elif result == AI:
        print("💥 🤖 AI WINS!")
    else:
        print("🤝 It's a DRAW!")

if __name__ == "__main__":
    main()

