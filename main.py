import random
import math 
import time
import sys
import tkinter 


 #runinput = input("You have found an Enemy! Try and Run or Stay and Fight? Run!/Fight!: ")
PP1 = 10
PP2 = 10
PP3 = 10
PP4 = 10
battle_dialogue = """These are your moves! 
F = 1 (PP=""" + str(PP1) + """) 
E = 2 (PP=""" + str(PP2) + """) 
W = 3 (PP=""" + str(PP3) + """) 
A = 4 (PP=""" + str(PP4) + ")"


fight = [True, False]
battle = True
character_health = 30 



#print(battle_dialogue)
enemy_health = 30
attack = [1, 2, 3, 4, 5]
enemy_attack_moves = ["Tackle", "Punch", "Fire Breath"]
run = [True, False]
no_combat = False

difficulty_prompt = input("What difficulty would you like to play at? Hard/Easy: ")


if character_health <= 0:
  print("Game Over!")
if difficulty_prompt == "Easy":
  print("Welcome to the Game! Beware of the Enemies!")
  time.sleep(2)
  print("You start walking through a forest ...")
  time.sleep(1)
  print("...")
  time.sleep(2)
  runinput = input("You have found an Enemy! Try and Run or Stay and Fight? Run!/Fight!: ")
  if runinput == "Run!":
    run2 = random.choice(run)
    if run2 == False:
      print("You tried to run, but it didn't work!")
      print(battle_dialogue)
      select_move = input("What move would you like to do? 1/2/3/4: ")
      if select_move == "1":
        
        attack_damage = random.randrange(1, len(attack))
        damage_done = attack_damage
        enemy_health = enemy_health - damage_done
        print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
        PP1u = PP1 - 1
        time.sleep(3)
        enemy_damage = random.randrange(1, len(attack))
        character_health = character_health - enemy_damage
        enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
        if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
       
      
      
      if select_move == "2":
  
        attack_damage = random.randrange(1, len(attack))
        damage_done = attack_damage
        print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
        PP2u  = PP2 - 1
        time.sleep(3)
        enemy_damage = random.randrange(1, len(attack))
        character_health = character_health - enemy_damage
        enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
        if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
        
   
      if select_move == "3":
     
        attack_damage = random.randrange(1, len(attack))
        damage_done = attack_damage
        enemy_health = enemy_health - damage_done
        print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
        PP3u = PP3 - 1
        time.sleep(3)
        enemy_damage = random.randrange(1, len(attack))
        character_health = character_health - enemy_damage
        enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
        if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
   
   
        
      if select_move == "4":
       
        attack_damage = random.randrange(1, len(attack))
        damage_done = attack_damage
        enemy_health = enemy_health - damage_done
        print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
        PP4u = PP4 - 1
        time.sleep(3)
        enemy_damage = random.randrange(1, len(attack))
        character_health = character_health - enemy_damage
        enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
        if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
       
    
        
        
    if run2 == True:
      print("Game Over!")
      quit()
  
  if character_health == 0 or enemy_health == 0:
    print("You have died!")
    quit()
    battle = False
  
  if runinput == "Fight!":
    print(battle_dialogue)
    select_move = input("What move would you like to do? 1/2/3/4: ")
    if select_move == "1":
        attack_damage = random.randrange(1, len(attack))
        damage_done = attack_damage
        enemy_health = enemy_health - damage_done
        print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
        PP1 = PP1 - 1
        time.sleep(3)
        enemy_damage = random.randrange(1, len(attack))
        character_health = character_health - enemy_damage
        enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
        if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
    

    if select_move == "2":
        attack_damage = random.randrange(1, len(attack))
        damage_done = attack_damage
        enemy_health = enemy_health - damage_done
        print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
        PP2 = PP2 - 1
        time.sleep(3)
        enemy_damage = random.randrange(1, len(attack))
        character_health = character_health - enemy_damage
        enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
        if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
       
   
        
    if select_move == "3":
        attack_damage = random.randrange(1, len(attack))
        damage_done = attack_damage
        enemy_health = enemy_health - damage_done
        print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
        PP3 = PP3 - 1
        time.sleep(3)
        enemy_damage = random.randrange(1, len(attack))
        character_health = character_health - enemy_damage
        enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
        if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
      
        
        
    if select_move == "4":
        attack_damage = random.randrange(1, len(attack))
        damage_done = attack_damage  
        enemy_health = enemy_health - damage_done
        print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
        PP4 = PP4 - 1
        time.sleep(3)
        enemy_damage = random.randrange(1, len(attack))
        character_health = character_health - enemy_damage
        
        enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
        character_health = character_health - enemy_damage
        if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
     
      

    
  if character_health == 0 or enemy_health == 0:
    print("You have died!")
    quit()
    battle = False

  while character_health > 0 or enemy_health > 0 or battle == True :
    print(battle_dialogue)
    select_move = input("What move would you like to do? 1/2/3/4: ")
    if character_health > 0 or enemy_health > 0:
      if select_move == "1":
        attack_damage = random.randrange(1, len(attack))
        damage_done = attack_damage
        enemy_health = enemy_health - damage_done
        print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
        PP1 = PP1 - 1
        time.sleep(3)
        enemy_damage = random.randrange(1, len(attack))
        character_health = character_health - enemy_damage
        enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
        if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
    if select_move == "2":     
        attack_damage = random.randrange(1, len(attack))
        damage_done = attack_damage
        enemy_health = enemy_health - damage_done
        print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
        PP2 = PP2 - 1
        time.sleep(3)
        enemy_damage = random.randrange(1, len(attack))
        character_health = character_health - enemy_damage
        enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
        if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
    
      
    if select_move == "3":
        attack_damage = random.randrange(1, len(attack))
        damage_done = attack_damage
        enemy_health = enemy_health - damage_done
        print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
        PP3 = PP3 - 1
        time.sleep(3)
        enemy_damage = random.randrange(1, len(attack))
        character_health = character_health - enemy_damage
        enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
        if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
    if select_move == "4":
        attack_damage = random.randrange(1, len(attack))
        damage_done = attack_damage
        enemy_health = enemy_health - damage_done
        print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
        PP4 = PP4 - 1
        time.sleep(3)
        enemy_damage = random.randrange(1, len(attack))
        character_health = character_health - enemy_damage
        enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
        if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
      
if difficulty_prompt == "Hard":
  print("Welcome to the Game! Beware of the Enemies!")
  time.sleep(2)
  print("You start walking through a forest ...")
  time.sleep(1)
  print("...")
  time.sleep(2)
  runinput = input("You have found an Enemy! Try and Run or Stay and Fight? Run!/Fight!: ")
  if runinput == "Run!":
    run2 = random.choice(run)
    if run2 == False:
      print("You tried to run, but it didn't work!")
      print(battle_dialogue)
      select_move = input("What move would you like to do? 1/2/3/4: ")
      if select_move == "1":
        
        attack_damage = random.randrange(1, len(attack))
        damage_done = attack_damage
        enemy_health = enemy_health - damage_done
        print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
        PP1u = PP1 - 1
        time.sleep(3)
        enemy_damage = random.randrange(1, len(attack))
        character_health = character_health - enemy_damage
        enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
        if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
       
      
      
      if select_move == "2":
  
        attack_damage = random.randrange(1, len(attack))
        damage_done = attack_damage
        print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
        PP2u  = PP2 - 1
        time.sleep(3)
        enemy_damage = random.randrange(1, len(attack))
        character_health = character_health - enemy_damage
        enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
        if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
        
   
      if select_move == "3":
     
        attack_damage = random.randrange(1, len(attack))
        damage_done = attack_damage
        enemy_health = enemy_health - damage_done
        print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
        PP3u = PP3 - 1
        time.sleep(3)
        enemy_damage = random.randrange(1, len(attack))
        character_health = character_health - enemy_damage
        enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
        if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
   
   
        
      if select_move == "4":
       
        attack_damage = random.randrange(1, len(attack))
        damage_done = attack_damage
        enemy_health = enemy_health - damage_done
        print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
        PP4u = PP4 - 1
        time.sleep(3)
        enemy_damage = random.randrange(1, len(attack))
        character_health = character_health - enemy_damage
        enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
        if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
       
    
        
        
    if run2 == True:
      print("Game Over!")
      quit()
  
  if character_health == 0 or enemy_health == 0:
    print("You have died!")
    quit()
    battle = False
  
    if runinput == "Fight!":
      print(battle_dialogue)
      select_move = input("What move would you like to do? 1/2/3/4: ")
      if select_move == "1":
        fight_hit = random.choice(fight)
        if fight_hit == False:
          print("Your move missed!")
          time.sleep(3)
          enemy_damage = random.randrange(1, len(attack))
          character_health = character_health - enemy_damage
          enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
          if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
 
      
        if fight_hit == True:
          attack_damage = random.randrange(1, len(attack))
          damage_done = attack_damage
          enemy_health = enemy_health - damage_done
          print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
          PP1 = PP1 - 1
          time.sleep(3)
          enemy_damage = random.randrange(1, len(attack))
          character_health = character_health - enemy_damage
          enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
          if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
    

      if select_move == "2":
        fight_hit = random.choice(fight)
        if fight_hit == False:
          print("Your move missed!")
          time.sleep(3)
          enemy_damage = random.randrange(1, len(attack))
          character_health = character_health - enemy_damage
          enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
          if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
        
        if fight_hit == True:
      
          attack_damage = random.randrange(1, len(attack))
          damage_done = attack_damage
          enemy_health = enemy_health - damage_done
          print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
          PP2 = PP2 - 1
          time.sleep(3)
          enemy_damage = random.randrange(1, len(attack))
          character_health = character_health - enemy_damage
          enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
          if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
       
   
        
      if select_move == "3":
        fight_hit = random.choice(fight)
        if fight_hit == False:
        
          print("Your move missed!")
          time.sleep(3)
          enemy_damage = random.randrange(1, len(attack))
          character_health = character_health - enemy_damage
          enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
          if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
        
    
        if fight_hit == True:
        
          attack_damage = random.randrange(1, len(attack))
          damage_done = attack_damage
          enemy_health = enemy_health - damage_done
          print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
          PP3 = PP3 - 1
          time.sleep(3)
          enemy_damage = random.randrange(1, len(attack))
          character_health = character_health - enemy_damage
        
          enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
          if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
      
        
        
      if select_move == "4":
        fight_hit = random.choice(fight)
        if fight_hit == False:
      
          print("Your move missed!")
          time.sleep(3)
          enemy_damage = random.randrange(1, len(attack))
          character_health = character_health - enemy_damage
          enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
          if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
      
        if fight_hit == True:
      
          attack_damage = random.randrange(1, len(attack))
          damage_done = attack_damage  
          enemy_health = enemy_health - damage_done
          print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
          PP4 = PP4 - 1
          time.sleep(3)
          enemy_damage = random.randrange(1, len(attack))
          character_health = character_health - enemy_damage
        
          enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_atbjtack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
        character_health = character_health - enemy_damage
        if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()

  while character_health > 0 or enemy_health > 0 or battle == True :
    print(battle_dialogue)
    select_move = input("What move would you like to do? 1/2/3/4: ")
    if character_health > 0 or enemy_health > 0:
      if select_move == "1":
        fight_hit = random.choice(fight)
        if fight_hit == False:
      
          print("Your move missed!")
          time.sleep(3)
          enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health - enemy_damage) + " health remaining!" )
          if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
        if fight_hit == True:
          attack_damage = random.randrange(1, len(attack))
          damage_done = attack_damage
          enemy_health = enemy_health - damage_done
          print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
          PP1 = PP1 - 1
          time.sleep(3)
          enemy_damage = random.randrange(1, len(attack))
          character_health = character_health - enemy_damage
          enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
          if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
      if select_move == "2":
        fight_hit = random.choice(fight)
        if fight_hit == False:
     
          print("Your move missed!")
          time.sleep(3)
          enemy_damage = random.randrange(1, len(attack))
          character_health = character_health - enemy_damage
          enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
          if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
      
        if fight_hit == True:
     
          attack_damage = random.randrange(1, len(attack))
          damage_done = attack_damage
          enemy_health = enemy_health - damage_done
          print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
          PP2 = PP2 - 1
          time.sleep(3)
          enemy_damage = random.randrange(1, len(attack))
          character_health = character_health - enemy_damage
          enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
          if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
    
      
      if select_move == "3":
        fight_hit = random.choice(fight)
        if fight_hit == False:
 
          print("Your move missed!")
          time.sleep(3)
          enemy_damage = random.randrange(1, len(attack))
          character_health = character_health - enemy_damage
          enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
          if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
  
        if fight_hit == True:
      
          attack_damage = random.randrange(1, len(attack))
          damage_done = attack_damage
          enemy_health = enemy_health - damage_done
          print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
          PP3 = PP3 - 1
          time.sleep(3)
          enemy_damage = random.randrange(1, len(attack))
          character_health = character_health - enemy_damage
          enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
          if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
      if select_move == "4":
        fight_hit = random.choice(fight)
        if fight_hit == False:
          print("Your move missed!")
          time.sleep(3)
          enemy_damage = random.randrange(1, len(attack))
          character_health = character_health - enemy_damage
          enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
          if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
      
      
    
        if fight_hit == True:
    
          attack_damage = random.randrange(1, len(attack))
          damage_done = attack_damage
          enemy_health = enemy_health - damage_done
          print("You did " + str(damage_done)  + " damage! The enemy has " + str(enemy_health) + " health remaining!")
          PP4 = PP4 - 1
          time.sleep(3)
          enemy_damage = random.randrange(1, len(attack))
          character_health = character_health - enemy_damage
    
          enemy_attack = print("Enemies Turn! Enemy used " + random.choice(enemy_attack_moves) + " and it did " + str(enemy_damage) + " damage! You have " + str(character_health) + " health remaining!" )
        if character_health < 1 or enemy_health < 1:
             print("You have died") 
             quit()
      
  
   

      

      
      



  

