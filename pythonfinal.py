import random

'''
HELPER STRINGS -- Feel free to copy these lines to aid in your printouts:


Press Enter when you are ready to begin...

You encountered ___

Enter:  '1' to use your ___
        '2' to run away
Your choice: ___                       -
Press Enter to continue...

You won the fight!

You lost the fight...

You ran away.

You made it to the other town!

You left the game.
'''

#----------------------------------------------------------------------------------
def game_loop():
    #game loop will be the main funcion in the program.
    #this function will contain loops that run the game
    
    print("\nWelcome adventurer.")
    
    #get the weapon from the user
    user_weapon = get_weapon()
    
    #get the name from the user
    user_name = get_name()
    
    print("\nHello,", name)
    print("Welcome to The Legend of Python!")
    print("Before you is a path that you must take to reach the next town.")
    print("However, there are monsters roaming the path up ahead, and you")
    print("must be prepared to battle!")
    print("I see you have your trusty ", weapon, ". You will need it.", sep="")
#--------------------------------------------------------------------------------------------------
def get_name():
    #get name will get the name of the user and pass it to game_loop()                  #something is looping here?
    
    #get the user input
    user_name = input("What is your name?: ")
    
    #return it so other functions can get it
    return user_name
    
    get_weapon()
#--------------------------------------------------------------------------------------------------
def get_weapon():
    #get weapon will get the weapon of choice from the user and pass it to game_loop()
    
    #get the weapon choice
    user_weapon = input("What is your weapon of choice?: ")
    
    #return it so other functions get it
    return user_weapon
    
    game_loop()
#----------------------------------------------------------------------------------------------------
#def encounter():
    #encounter will simulate the adventure along the path
    #each monster will have a 1 in 3 chance of being chosen
    #based on the chosen monster, one of three files will be read from to get information about the monster
    #the user will take the name of the monster and description
    #it will print the lines in each file depending on which monster is summoned
    
#---------------------------------------------------------------------------------------------------
def previous_adventurer():
    #previous_adventurer will tell the user stats and results of the previous adventurer
    #a file will be read to give the output
    
    try:
        #open the file
        previousAdventurer_file = open('previousAdventurer.txt', 'r')
        name = previousAdventurer.readline()
        
        while name != '':
            name = name.rstrip('\n')
            weapon = previousAdventurer_file.readline().rstrip('\n')
            
            #output
            print('')
            print(f"Name: {name}")
            print(f"Weapon: {weapon}")
            print('')
            
            #read the next description
            name = previousAdventurer_file.readline()
        
        #close the file and output a message
        previousAdventurer_file.close()
        print("All records read.")
        
    except Exception as err:
        print(err)
#----------------------------------------------------------------------------------------------------
#def game_over():
    #game_over will congratulate the user and be the ending point in the game
    #this function will also save the user's name and weapon to the file

#----------------------------------------------------------------------------------------------------
def main():
    #main will accept no arguments
    #it is just a function for the user to choose to start the game
    #see the stats of previous players, or quit the game
    #for my help, it is main and menu combined
    
    #try and except
    try:
        
        #display menu
        print("Game Menu")
        print("Enter '1' to start the game")
        print("Enter '2' to see the previous adventurer's stats")
        print("Enter '3' to quit the game")
        
        #get input from the user
        choice = input("Your choice: ")
        
        # Validate if the input is a number and between 1 and 3
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 3:
                return choice  # Return valid choice
            else:
                print("Invalid choice! Please choose a number between 1 and 3.")
        else:
            print("Invalid input! Please enter a valid number (not a letter or special character).")
            
    except Exception as err:
        print(err)
        
def menu():
    #menu will call the functions
    try:
        
        # Prime the loop with a valid choice from contact_manager
        choice = main()
        
        # Loop to call the desired function based on the choice
        while choice != 3:
            if choice == 1:
                get_name()
            elif choice == 2:
                previous_adventurer()

            # Get the next valid choice from the user
            choice = int(main())
        
        print("You have left the game...")
    
    except Exception as err:
        print(err)
        
    
#------------------------------------------------------------------------------------------------------    
main()