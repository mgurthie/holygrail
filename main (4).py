GRAY = 30
RED = 31
GREEN = 32
YELLOW = 33
BLUE = 34
MAGENTA = 35
CYAN = 36
WHITE = 37 
ON_RED = 41
ON_GREEN = 42
ON_YELLOW = 43
ON_BLUE = 44
ON_PURPLE = 45
ON_CYAN = 46
ON_GRAY = 47

def colorText(text:str, color=WHITE):
  #Magic Formatting String
  fmt_str = "\033[%dm%s"
  rst_str = "\033[0m"
  if isinstance(color, list):
    for attr in color:
      text = fmt_str % (attr, text)
  else:
    text = fmt_str % (color, text)
  text += rst_str
  return text

BLANK = colorText(" ", ON_GRAY)

def createInitialBoard(width, height):
  board = []
  for r in range(height):
    board += [[BLANK] * width]
  return board


def makeMove(player, column, board):
  height = len(board)
  column = (int(column)-1) % 7
  for i in range(height):
    if isColumnEmpty(column, board):
      board[-1][column] = player
      break
    if not isColumnEmpty(column, board):
      if board[i][column] != colorText(" ", ON_GRAY):
        board[i-1][column] = player
        break
      else:
        pass
  return board

def isColumnEmpty(input, board):
  height = len(board)
  for i in range(height):
    if board[i][int(input)] != colorText(" ",ON_GRAY):
      return False
  return True
  

def basicGameWinCondition(board, player):
#check horizontal
  win = 0
  for i, r in enumerate(board):
    for j in range(len(r)):
      n = r[j]
      if n == player:
        win += 1
      else:
        win = 0
      if win >= 4:
        return player
  return False
#check vertical
  turnedBoard = []
  for r in board[0]:
    turnedBoard += [[]]
  for a, _ in enumerate(board):
    for b, item in enumerate(board[a]):      
      turnedBoard[b] += [item]

  #check
  for i, r in enumerate(turnedBoard):
    for j in range(len(r)):
      n = r[j]
      if n == player:
        win += 1
      else:
        win = 0
      if win >= 4:
        return player
  
#Check diagonal (rising to right)
  for i, item in enumerate(board): #row
    for g in range(len(item)):
      for j in range(4):
        if not (findplace(i+j, g-j, board) == player):
          break
      else:
        return player
     
  #Check diagonal (falling to right)
  for i, item in enumerate(board): #row
    for g in range(len(item)):
      for j in range(4):
        if not (findplace(i+j, g+j, board) == player):
          break
      else:
        return player
  return False

def findplace(r, c, board):
  if r < 0 or r >= len(board):
    return False
  elif c < 0 or c >= len(board[0]):
    return False
  else:
    return board[r][c]

def isPlayerInputValid(input, board):
  column = (int(input)-1) % 7
  if int(input) > len(board[1]):
    return False
  if board[0][column] !=  colorText(" ",ON_GRAY):
    return False
  return True

def getPlayerColumn(player, board):
  playerInput = input(f"What column would you like to play, player {player}? ")
  while not isPlayerInputValid(playerInput, board):
    print("Sorry.  That was not a valid play.")
    playerInput = input(
      f"What column would you like to play, player {player}? ")
  return playerInput


def printBoard(guesses):
  for turn in guesses:
    for place in turn:
      print(place,end=" ")
    print()
    print()


def connect4(
    players=("X", "O"), width=7, height=6, winCondition=basicGameWinCondition):
  #Setup the game
  board = createInitialBoard(width, height)
  printBoard(board)
  #Run Game
  for turn in range(
      width * height):  #Can't have more total turns than spots on the board
    #Each player gets their turns in order
    for p in players:
      #Get input from the player
      c = getPlayerColumn(p, board)
      #Change the board in response to the requested move
      board = makeMove(p, c, board)
      printBoard(board)
      #
      w = winCondition(board, p)
      if w:
        return w
  return False  #Nobody won/tie game


print(connect4([colorText(" ",ON_YELLOW),colorText(" ",ON_RED)]))