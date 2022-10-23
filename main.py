import random
#Number Guessing Game Objectives:
print("""    ___                    _             
  / _ \_   _  ___ ___ ___(_)_ __   __ _ 
 / /_\| | | |/ _ / __/ __| | '_ \ / _` |
/ /_\\| |_| |  __\__ \__ | | | | | (_| |
\____/ \__,_|\___|___|___|_|_| |_|\__, |
                                  |___/ """)
guess = 0
tries = 10 
randomNumber = random.randint(1,100)
difficulty = input("What difficulty do you want? easy or hard: ").lower()

if difficulty == 'easy':
    tries = 10
elif difficulty == 'hard':
    tries = 5

while(tries>0 and guess!=randomNumber):
    print(f"You have {tries} attempts remaining")
    guess = int(input("Make a guess: "))
    if(guess<randomNumber):
        print("Too low")
    elif(guess>randomNumber):
        print("Too High")
    tries-=1

if(guess!=randomNumber):
    print(f"You've run out of turns, the answer was {randomNumber}")
else:
    print(f"You got it! The answer is {randomNumber}")

    
    
        
    

    

    
