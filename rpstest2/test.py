input = ""
output = ""
game_score = [0] * 3

def calculate_score():
  print("Human: " + input+ " Computer: " + output);
  winner((3 + choice(input) - choice(output)) % 3)

def choice(argument):
  if argument == 'R':
      return 0
  if argument == 'P':
      return 1
  if argument == 'S':
      return 2


def winner(winner):
  if winner == 0:
    print("Its a tie")
    game_score[2] += 1
  if winner == 1:
    print("Human wins")
    game_score[0] += 1
  if winner == 2:
    print("AI wins")
    game_score[1] += 1
  print("Human:" + str(game_score[0]) + " AI:" + str(game_score[1]) + " Tie:" + str(game_score[2]))



i = 1
while i < 60:


  player_move = raw_input("What is your move (RPS) ? ")[0].capitalize()
  if player_move not in "RPS":
      print("move not valid")
      continue
  else:
    execfile('bayes.py')
    input = str(player_move)
    calculate_score()
    i += 1













