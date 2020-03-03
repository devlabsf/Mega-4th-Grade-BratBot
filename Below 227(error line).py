         sessionover = False
        while not sessionover:
          print(f"Hey {user}! Would you like to:")
          print("(a) chat with a bot")
          print("(b) put two bots in a roasting battle?")
          game = input("Plewase choose (type q to quit): ")
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
              greeting = ryth.greeting
              phrases = ryth.phrases
            elif bot == 15:
              greeting = camila.greeting
              phrases = camila.phrases
            elif bot == 16:
              greeting = kai.greetings
              phrases = kai.phrases
            print(greeting)
            # special case for mystery bot #9
            # code added by Lazlo
            if bot == 9:
              input()
              while True:
                time.sleep(0.5)
                print(random.choice(phrases))
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
                print(random.choice(phrases))

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

            times = random.randint(3,10)
            for _ in range(times):
              print(bot_list[bot1],":",random.choice(phrases1))
              time.sleep(1.5)
              print(bot_list[bot2],":",random.choice(phrases2))
              time.sleep(1.5)
            if bot1 == DLBro or bot2 == DLBro:
              winner = DLBro
            else:
              winner = random.choice([bot_list[bot1],bot_list[bot2]])
            print(winner, "wins the BratBot battle!! OHHHHHHHH!!!!")
          elif game in ['q','Q']:
            sessionover = True

  # if login fails, give chance to create account

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
if hav_username == "n":
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
'''


elif game in ['c','C']:
input = qwerty ("In Testing! DO NOT GO FURTHER!")
if 1234 = qwerty 
  print ("Testing actavated. \U0001f3c6")
    users = open("MakeAbot.txt",'r')
  for line in Bots:
    bots = line.rstrip().split(',')   
      auth = 1
      authuser = user
