import random

def play_rock_paper_scissors():
  """Plays a single round of Rock-Paper-Scissors."""

  user_choice = input("Choose rock, paper, or scissors: ").lower()
  computer_choice = random.choice(['rock', 'paper', 'scissors'])

  print("You chose:", user_choice)
  print("Computer chose:", computer_choice)

  if user_choice == computer_choice:
    print("It's a tie!")
  elif (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissors' and computer_choice == 'paper'):
    print("You win!")
  else:
    print("Computer wins!")

# Main game loop
while True:
  play_rock_paper_scissors()

  play_again = input("Play again? (yes/no): ").lower()
  if play_again != 'yes':
    break

print("Thanks for playing!")
