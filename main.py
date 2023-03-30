board_ascii = """
    A     B     C  
       |     |     
1      |     |     
  _____|_____|_____
       |     |     
2      |     |     
  _____|_____|_____
       |     |     
3      |     |     
       |     |  
"""

play_game = True
while play_game:
    print(board_ascii)
    input('Make a move by entering box number (such as "A1" for top-left corner):')
