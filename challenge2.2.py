'''
Implement a class called player that represent a cricket player.the player class should have a
method called play() which prints "The player is playing cricket.derive two calsses,batsman and
Bowler, from the player class.override the play() method in each derived class to print "The batsman 
is batting", and "The bowler is bowling",respectively.write a program to create objects of both the
Batsman and bowler classes and call the play() method for each  object.'''

class player:
  def play(self):
    print("The player is playing cricket.")

class Batsman(player):
  def play(self):
    print("The Batsman is batting.")

class Bowler(player):
  def play(self):
    print("The bowler is bowling .")

batsman = Batsman()
bowler = Bowler()

batsman.play()
bowler.play()
