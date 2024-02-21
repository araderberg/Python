##############################################################################
###Program Name: Pickleball.py
###Programmer: Aaliyah Raderberg
###Project: Build a game that outlines the basic game logic and rules
###This code defines basic Player and Court classes, along with functions for serving, playing rallies, and
###checking game/match over conditions.
###TO DO: update functions to create a working simulation
##############################################################################

class Player:
  def __init__(self, name):
    self.name = name
    self.score = 0

class Court:
  def __init__(self):
    self.players = [Player("A1"), Player("A2"), Player("B1"), Player("B2")]
    self.serving_team = 0  # 0 for team A, 1 for team B
    self.server = 0  # 0 for A1, 1 for A2, 2 for B1, 3 for B2
    self.score = [0, 0]

def serve(server, court):
  # Implement serve logic here, checking for faults and updating score
  # This could involve random ball placement or user input
  pass

def rally(court):
  while True:
    # Simulate each shot, checking for faults and updating score
    # This could involve random ball placement or user input for shot selection
    pass
    # Check for game end conditions (11 points, 2 point lead)
    if game_over(court):
      break

def game_over(court):
  # Check if any team has reached 11 points with a 2 point lead
  pass

def main():
  court = Court()
  while True:
    serve(court.server, court)
    rally(court)
    # Switch serving team and server
    court.serving_team = (court.serving_team + 1) % 2
    court.server = (court.server + 1) % 4
    # Check for match end conditions (best of 3 games)
    if match_over(court):
      break

def match_over(court):
  # Check if any team has won 2 games
  pass

if __name__ == "__main__":
  main()
