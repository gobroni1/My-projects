board = ['0',  '1',  '2',  '3',  '4',  '5',  '6', 
         '7',  '8',  '9',  '10', '11', '12', '13',
         '14', '15', '16', '17', '18', '19', '20', 
         '21', '22', '23', '24', '25', '26', '27', 
         '28', '29', '30', '31', '32', '33', '34',
         '35', '36', '37', '38', '39', '40', '41']

def gen_board(boardg):
    max_length = max(len(str(item)) for item in boardg)  
    column_width = max_length +1

    for i in range(0, len(boardg), 7):
        row = boardg[i:i+7]
        print("| ".join([f"{item:>{column_width}}" for item in row]))
        
        if i + 7 < len(boardg):
            print("-" * 35)  

def valid (gameb,attmpt):
    if gameb[attmpt] != "🟢" and gameb[attmpt] != "🔴":
        return True
    else:
        return False

def gravity (gameb,attmpt):
    ls = []
    if valid(gameb, attmpt):
        for i in range (attmpt, 42, 7):
            if valid(gameb, i):
                ls.append(i)
        return max(ls)

def is_invalid (gameb, attmpt):
    try:
        attmpt = int(attmpt)
    except ValueError:
            return "invalid"
    if not isinstance(attmpt, int):
        return "invalid"
    if attmpt > 40: 
        return "invalid"
    elif gameb[attmpt] == "🔴" or gameb[attmpt] == "🟢":
        return "invalid"

def make_move (gameb, player, attmpt):
    gameb[gravity(gameb, attmpt)] = player
   

def won(board):
    rows = 6  
    cols = 7  
    def get_value(row, col):
        if 0 <= row < rows and 0 <= col < cols:
            return board[row * cols + col]
        return None
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  
    for row in range(rows):
        for col in range(cols):
            current = get_value(row, col)
            if current in ["🟢", "🔴"]:
                for dr, dc in directions:
                    if all(get_value(row + i * dr, col + i * dc) == current for i in range(4)):
                        return True, current  
    return False  

    
def game_won (gameb):
         
    red_move = []
    green_move = []
        
    for i in range(len(gameb)):
        if gameb[i] == "🔴":
            red_move.append(i)
        elif gameb[i] == "🟢":
            green_move.append(i)
                
        # red_move.sort()
        # green_move.sort()

    if won(gameb):
        return True

    
game = True
moves_count = 1
att = 0
print("game intro")
while game:
    gen_board(board)
    
    
    if game_won(board):
        print(f"{won(board)[1]} won the game")
        break
    if moves_count % 2 != 0:
        att = input("here: ")
        if is_invalid(board, att) == "invalid":
            print("invalid")
        else:
            make_move(board, "🟢",int(att))
            gravity(board, int(att))
            moves_count += 1
    elif moves_count % 2 ==0:
        att = input("here: ")
        if is_invalid(board, att) == "invalid":
            print("invalid")
        else:
            make_move(board,"🔴" ,int(att))
            gravity(board, int(att))
            moves_count += 1
    print(f"moves done: {moves_count}")