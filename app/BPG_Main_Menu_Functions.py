#===================================================================================================
#  ?                                           ABOUT
#  @author         :  Santiago Arellano
#  @repo           :  Battleship.io
#  @createdOn      :  08-06-23
#  @description    :  Implementation for each menu function defined in Main Gam.py
#===================================================================================================

#! Preproccesing Directives
import sys
sys.path.insert(0, "C:/Users/santi/OneDrive - Universidad San Francisco de Quito/Interests/Computer Science/Battleship_Python_Game/src")
from BPG_Main_Logic_Engine import Main_Game_Engine
from BPG_Main_Player_Class import Main_Player_Class
import re
from random import randint

#*Definition for the main menu option 1 function
def Main_Menu_Option_1():
    #? Constants

    welcome_screen_width = 60;
    #? Defining initial players and Logic Engine Instances
    players: list = list()
    for repetition in range(0,2,1):
        print("Starting the fleet's Engine Captain...".center(welcome_screen_width, '='))
        try:
            regex_expression_for_names = '[A-Z][a-z]+';
            user_name = input("Please enter your name: ")
            name_check = re.match(regex_expression_for_names, user_name)
            while not name_check:
                try:
                    print("Invalid name, please enter a valid string, remove any numbers or special characters")
                    user_name = input("Please enter your name: ")
                except ValueError:
                    print("Incorrect Value, please ensure you are entering text and not numbers")
                name_check = re.match(regex_expression_for_names, user_name)
            if name_check:
                print("Acknowledged, setting up your nametag".center(welcome_screen_width, '='))
                player_id = randint(1, 100);
                players.append(Main_Player_Class(user_name, player_id))
        except ValueError:
            print("Incorrect Value, please ensure you are entering text and not numbers")


    #? Return to main menu
    print("Returning to the main menu...".center(welcome_screen_width, '='))


