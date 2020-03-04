"""
4th Grade Python class MegaBratBot program.
We need to have it so the bratbots only say stuff twice. I will work on that.

March 3 code update: 
We converted the data structure holding bot roasts from a list to a dictionary, so we could assign a value (score) to each roast. Why? So that when two bots battle, the program will evaluate the winner based on the combined numerical value all roasts given, rather than just randomly picking a winner.
To make that work, we have to make a change to all roast print statements. When the 'phrases' variable was a list, random.choice() could work directly with it, but since it's now a dictionary, we have to convert it on the fly to a list by doing list(phrases).
Old form: print(random.choice(phrases))
Old form: print(random.choice(list(phrases)))

Team: our code is still inefficient and repetitive. DRY! We'll look at ways to clean it all up. This is a job for object-oriented programming! But there are other hacks we can do to greatly reduce the size of the codebase even without OOP.
"""
import random
import time

from bots import sammy
from bots import daisy
from bots import juli
from bots import tao
from bots import zoe_w
from bots import pax
from bots import lachlan
from bots import john
from bots import shaila
from bots import mhhmbot
from bots import ellis
from bots import DLBro
from bots import fifer
from bots import RandomBot
from bots import ryth
from bots import camila
from bots import kai

print ("This code is a production of the DL bros")
time.sleep (1.5)
print ("Harry's signature","\U0001f3c6")
time.sleep (1.5)
print ("Jayden's signature","\u2b50")
time.sleep (1.5)
print("Lazlo's signuture","\U0001f48e")
time.sleep (1.5)

sessionover = False
hav_username = input("Do you have a account? (y/n) ")
if hav_username == "y":
  # authenticate user
  auth = 0
  users = open("users.txt",'r')
  username = input("Username: ")
  password = input("Password: ")
  for line in users:
    user, passwd = line.rstrip().split(',')   
    if username == user and password == passwd:
      auth = 1
      authuser = user
      print("WELCOME! ")
  if auth:
    bot_list = {1:'Daisy',2:'Juli',3:'Tao',4:'Zoe W',5:'Pax',6:'Lachlan', 7:'John', 8:'Shaila', 9:'mystery', 10:'Ellis', 11:'DLBros', 12:'fifer', 13:'RandomBot', 14:'Ryth', 15:'Camila',16:'Kai',17:'Sammy'}
    user = username
    while not sessionover:
      print(f"Hey {user}! Would you like to:")
      print("(a) chat with a bot")
      print("(b) put two bots in a roasting battle?")
      print("(c) add a bot")
      game = input("Please choose (type q to quit): ")
      # single-bot chat
      # DLBros: notice how much code is repeated here?
      # DRY=Don't Repeat Yourself
      # We'll talk about how to make this code more efficient
      if game in ['a','A']:
        for bot in bot_list:
          print(bot,":",bot_list[bot])
        bot = int(input("Choose your bot (enter a number from the list): "))
        if bot == 1:
          greeting = daisy.greeting
          phrases = daisy.phrases
        elif bot == 2:
          greeting = juli.greeting
          phrases = juli.phrases
        elif bot == 3:
          greeting = tao.greeting
          phrases = tao.phrases
        elif bot == 4:
          greeting = zoe_w.greeting
          phrases = zoe_w.phrases
        elif bot == 5:
          greeting = pax.greeting
          phrases = pax.phrases
        elif bot == 6:
          greeting = lachlan.greeting
          phrases = lachlan.phrases
        elif bot == 7:
          greeting = john.greeting
          phrases = john.phrases    
        elif bot == 8:
          greeting = shaila.greeting
          phrases = shaila.phrases
        elif bot == 9:
          greeting = mhhmbot.greeting
          phrases = mhhmbot.phrases
        elif bot == 10:
          greeting = ellis.greeting
          phrases = ellis.phrases
        elif bot == 11:
          greeting = DLBro.greeting
          phrases = DLBro.phrases
        elif bot == 12:
          greeting = fifer.greeting
          phrases = fifer.phrases
        elif bot == 13:
          greeting = RandomBot.greeting
          phrases = RandomBot.phrases
        elif bot == 14:
          greeting = ryth.greetings
          phrases = ryth.phrases
        elif bot == 15:
          greeting = camila.greetings
          phrases = camila.phrases
        elif bot == 16:
          greeting = kai.greetings
          phrases = kai.phrases
        elif bot == 17:
          greeting = sammy.greeting
          phrases = sammy.phrases
        print(greeting)
        # special case for mystery bot #9
        # code added by Lazlo
        if bot == 9:
          while True:
            time.sleep(0.5)
            print(random.choice(list(phrases)))
            y = phrases
            x = input()
            if x == "mhm" or x == "mhhm" or x == "mhhhm":
              print("No copying!")
              phrases = y
            else:
              phrases = y
              continue
        else:
          while True:
            inpt = input()
            time.sleep(1.5)
            print(random.choice(list(phrases)))

      ## BattleBot mode
      elif game in ['b','B']:
        for bot in bot_list:
          print(bot,":",bot_list[bot])
        bot1 = int(input("Choose your first bot (enter a number from the list): "))
        if bot1 == 1:
          phrases1 = daisy.phrases
        elif bot1 == 2:
          phrases1 = juli.phrases
        elif bot1 == 3:
          phrases1 = tao.phrases
        elif bot1 == 4:
          phrases1 = zoe_w.phrases
        elif bot1 == 5:
          phrases1 = pax.phrases
        elif bot1 == 6:
          phrases1 = lachlan.phrases
        elif bot1 == 7:
          phrases1 = john.phrases
        elif bot1 == 8:
          phrases1 = shaila.phrases
        elif bot1 == 9:
          phrases1 = mhhmbot.phrases
        elif bot1 == 10:
          phrases1 = ellis.phrases
        elif bot1 == 11:
          phrases1 = DLBro.phrases
        elif bot1 == 12:
          phrases1 = fifer.phrases
        elif bot1 == 13:
          phrases1 = RandomBot.phrases
        elif bot1 == 14:
          phrases1 = ryth.phrases
        elif bot1 == 15:
          phrases1 = camila.phrases
        elif bot1 == 16:
          phrases1 = kai.phrases
          
        for bot in bot_list:
          print(bot,":",bot_list[bot])
        bot2 = int(input("Choose your second bot (enter a number from the list): "))
        if bot2 == 1:
          phrases2 = daisy.phrases
        elif bot2 == 2:
          phrases2 = juli.phrases
        elif bot2 == 3:
          phrases2 = tao.phrases
        elif bot2 == 4:
          phrases2 = zoe_w.phrases
        elif bot2 == 5:
          phrases2 = pax.phrases
        elif bot2 == 6:
          phrases2 = lachlan.phrases
        elif bot2 == 7:
          phrases2 = john.phrases
        elif bot2 == 8:
          phrases2 = shaila.phrases
        elif bot2 == 9:
          phrases2 = mhhmbot.phrases
        elif bot2 == 10:
          phrases2 = ellis.phrases
        elif bot2 == 11:
          phrases2 = DLBro.phrases
        elif bot2 == 12:
          phrases2 = fifer.phrases
        elif bot2 == 13:
          phrases2 = RandomBot.phrases
        elif bot2 == 14:
          phrases2 = ryth.phrases
        elif bot2 == 15:
          phrases2 = camila.phrases
        elif bot2 == 16:
          phrases2 = kai.phrases
        elif bot2 == 17:
          phrases2 = sammy.phrases

        times = random.randint(3,10)
        bot1score = bot2score = 0
        for _ in range(times):
          bot1roast = random.choice(list(phrases1))
          bot1score += phrases1[bot1roast]
          print(bot_list[bot1],":",bot1roast)
          time.sleep(1.5)
          bot2roast = random.choice(list(phrases2))
          bot2score += phrases2[bot2roast]
          print(bot_list[bot2],":",bot2roast)
          time.sleep(1.5)
          winner = bot1 if bot1score > bot2score else bot2
          #winner = random.choice([bot_list[bot1],bot_list[bot2]])
        print(bot_list[winner], f"wins the BratBot battle!! {bot1score} to {bot2score}!! OHHHHHHHH!!!!")
        print()

      # this will be the place to create a new bot
      elif game in ['C','c']:
        new_file = input("What would you like the name of the bot to be?")
        print("This feature coming soon!")
        #f = open('%s.txt' % new_file, 'w')

      elif game in ['Q','q']:
        break

  else:
    print("you bad")
    time.sleep(1)
    add_file = input("Would you like to make a account? (y/n) ")
    if add_file == "y":
      a = input("What would you like your username to be? ")
      b = input("What would you like your password to be? ")
      with open("users.txt", "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0 :
          file_object.write("\n")
          file_object.write(a)
          file_object.write(",")
          file_object.write(b)
          print("Done! Run program again to login \U0001f3c6")

elif hav_username == "n":
  a = input("What would you like your username to be? ")
  b = input("What would you like your password to be? ")
  with open("users.txt", "a+") as file_object:
    file_object.seek(0)
    data = file_object.read(100)
    if len(data) > 0 :
      file_object.write("\n")
      file_object.write(a)
      file_object.write(",")
      file_object.write(b)
      print("Done! Run program again to login \U0001f3c6")

'''
Harrys testing area! Do not touch!

elif game in ['c','C']:
input = qwerty ("In Testing! DO NOT GO FURTHER!")
if 1234 = qwerty 
  print ("Testing actavated. \U0001f3c6")
    users = open("MakeAbot.txt",'r')
  for line in Bots:
    bots = line.rstrip().split(',')   
      auth = 1
      authuser = user
'''