        feeling = input(f"How are you feeling,{user}? ")
      except ValueError:
        print("What is wrong with you?")
        continue
      except IndexError:
        print("Sorry, try a different feeling.")
        continue
      except SyntaxError:
        print("Sorry, try a different feeling.")
        continue
      time.sleep(.5)
      if feeling in ['happy', 'Happy']:
        print("Oh great, I'm happy you're happy.")
      elif feeling in ['sad', 'Sad']:
        print("I'm sad that you're sad.")
      elif feeling in ['bad', 'Bad']:
        print("Maybe this bot battle will make you feel better!")
      elif feeling in ['hungry', 'Hungry']:
        print("Oh, sorry I don't have any food. (I'm just a computer, you know.)")
      elif feeling in ['nervous','Nervous']:
        print("You should be nervous its about to get crazy.")
      elif feeling in ['good','Good']:
        print("Great! Heads up it's going to get crazy.")
      elif feeling in ['mad', 'Mad']:
        print("Sorry you feel mad. Hope this makes you happy.")
      elif feeling in ['great', 'Great']:
        print("Hope this doesn't make you bad cause it's going to get crazy!")
      else:
        print("Ooooookaaaaaayyyyyyy....")
        break