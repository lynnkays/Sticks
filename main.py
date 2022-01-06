import random

def main():
   # Global Variables
  active = True
  is_player1_turn = True
  is_computer = False
  player1_score = 0
  player2_score = 0
  player2_title = "Player 2"
  entries = 20
  valid_options = [["A", "a", "B", "b", "C", "c"], [1, 2, 3]]


  def validate_input (valid_options_index, option):
    """
    Validates Inputted Answers 

    :param valid_options_index: Determines which set is used for comparison
    :param option: Incoming option
    :return: Validated option
    """ 
    validate = True
    while(validate):
      validate = True if option not in valid_options[valid_options_index] else False
      if(validate):
        option = input("Invalid: Please select one of the options above: ")
    return option

  def print_board (rows, entries):
    """
    Prints the board of sticks

    :param rows: Number of rows 
    :param entries: Number of bar entries in each row
    """ 
    for row in range(rows):
      entry = "| " * entries
      print(entry)

  """
  Starts the Sticks Game

  """ 
  # Start of Game 
  print(
    '''
  -------------------------------------------
    _     _     _     _     _     _  
    / \   / \   / \   / \   / \   / \ 
  ( S ) ( t ) ( i ) ( c ) ( k ) ( s )
    \_/   \_/   \_/   \_/   \_/   \_/ 

  -------------------------------------------

  \nInstructions:
    • During every turn, a player can take one, two, or 
      three sticks from the board.
    • The player who takes the last stick, loses                           
    '''
  )

  # Handles Two Player and Computer Options
  print(
  """
  ****************  MENU   *****************
  \ta) Two Player          b) Computer
  """
  )
  player_choice = input("\nEnter a or b: ")
  validated_choice = validate_input(0, player_choice)

  # Handle computer verses player 2 options
  if(validated_choice in ["B", "b"]):
    is_computer = True
    player2_title = "Computer"
  elif(validated_choice in ["A", "a"]):
    is_computer = False
    player2_title = "Player 2"


  while(active):
    # Display Score  
    print(
      """
              CURRENT SCORE         
      --------------------------------          
      Player 1: %(p1_sticks)d     %(player2)s: %(p2_sticks)d
      """%{"player2": player2_title, "p1_sticks": player1_score, "p2_sticks": player2_score }
    )

    # Print board
    print_board(5, entries)
    # Keep Track of Turns
    print("\n\t\t\tPlayer 1's Turn") if is_player1_turn else print("\n\t\t\t%s's Turn"%(player2_title))

    # Handle each play
    play = 0
    if(is_computer and not is_player1_turn):
      play = random.randint(1,3)
      player2_score += play
    else:
      initial_play = int(input("\nEnter 1, 2 or 3: "))
      play = validate_input(1, initial_play)

      if(is_player1_turn):
        player1_score += play
      else:
        player2_score += play;

    # Handle end game condition 
    if(player1_score + player2_score >= 20):
      active = False
      print("\n\t\t\t%s Wins!"%(player2_title)) if is_player1_turn else print("\n\t\t\tPlayer 1 Wins!")

    is_player1_turn = not is_player1_turn
    entries -= play

if __name__ == '__main__':
  main()