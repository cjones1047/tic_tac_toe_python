board_ascii = """

    1     2     3  
       |     |     
A      |     |     
  _____|_____|_____
       |     |     
B      |     |     
  _____|_____|_____
       |     |     
C      |     |     
       |     | 
       
"""

board_list = list(board_ascii)

board_cell_dict = {
    'A1': 46,
    'A2': 52,
    'A3': 58,
    'B1': 106,
    'B2': 112,
    'B3': 118,
    'C1': 166,
    'C2': 172,
    'C3': 178
}

play_game = True
while play_game:
    print(''.join(board_list))
    player_move = input('Player "X" move by entering box number (such as "A1" for top-left corner):\n').upper()
    if player_move in board_cell_dict:
        print(board_cell_dict[player_move])
    else:
        print('Invalid move.')
        continue
    print('Valid move.')
