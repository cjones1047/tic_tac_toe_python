import random

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

winning_codes = [
    ['A1', 'A2', 'A3'],
    ['B1', 'B2', 'B3'],
    ['C1', 'C2', 'C3'],
    ['A1', 'B1', 'C1'],
    ['A2', 'B2', 'C2'],
    ['A3', 'B3', 'C3'],
    ['A1', 'B2', 'C3'],
    ['A3', 'B2', 'C1']
]

players = {
    'X': [],
    'O': []
}

play_game = True
current_player = random.choice(['X', 'O'])
while play_game:
    print(''.join(board_list))
    player_move = input(f'Player {current_player} move by entering box number (such as "A1" for top-left corner):'
                        f'\n').upper()
    if player_move in board_cell_dict:
        board_list[board_cell_dict[player_move]] = current_player
        player_moves = players[current_player]
        player_moves.append(current_player)
    else:
        print('Invalid move.')
        continue
    current_player = [player for player in players if player != current_player][0]
