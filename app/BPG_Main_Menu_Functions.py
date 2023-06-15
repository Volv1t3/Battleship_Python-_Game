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
import BPG_Common_Game_Phrases as GPH
import re
from random import randint
from os import environ, getenv, system
from dotenv import load_dotenv

load_dotenv()

#*Definition for the main menu option 1 function
def Main_Menu_Option_1():
    #? Constants
    logic_engine_instance = Main_Game_Engine(2);
    welcome_screen_width: int =  int(environ.get('MAX_SCREEN_WIDTH'));
    #? Defining initial players and Logic Engine Instances
    players: list = list()
    for repetition in range(0,2,1):
        print("|...Starting the fleet's Engine Captain...|".center(welcome_screen_width, '='))
        try:
            regex_expression_for_names = '[A-Z][a-z]+';
            user_name = input("Please enter your name: ")
            name_check = re.match(regex_expression_for_names, user_name)
            while not name_check:
                try:
                    print("Invalid name, please enter a valid string, remove any numbers or special characters")
                    user_name = input("Please enter your name: ")
                except ValueError:
                    print(GPH.incorrect_value_name_check.center(welcome_screen_width, '='))
                name_check = re.match(regex_expression_for_names, user_name)
            if name_check:
                print('\n')
                print("|Acknowledged, setting up your nametag|".center(welcome_screen_width, '='))
                player_id = randint(1, 100);
                players.append(Main_Player_Class(user_name, player_id))
        except ValueError:
            print(GPH.incorrect_value_name_check.center(welcome_screen_width, '='))
    system('cls')
    #? Having defined the list of players each of them needs a given starting grid
    print("|Setting up each players grid|".center(welcome_screen_width, '='))
    #* control variables for loop
    amount_of_total_ships: int = 4;
    ships_placed: int = 0;
    ships_already_placed = set();

    for repetition in range(0,2,1):
        print("|Setting up the grid for  {}|".format(players[repetition].player_fname).center(welcome_screen_width, '='))
        players_grid:list = logic_engine_instance.define_game_grid()
        players[repetition].set_player_ship_grid_with_locations(players_grid)
        while ships_placed < amount_of_total_ships:
            print("".center(welcome_screen_width, '='))
            print("Here's your navy captain:\n1. A destroyer (4 spaces)\n2. A frigate (3 spaces)\n3. A carrier (5 spaces)\n4. A submarine (2 spaces)")
            print("".center(welcome_screen_width, '='))
            try:
                ship_check: bool = False;
                while ship_check == False:
                    ship_number_select = int(input("You choose to place (Please enter the number option):"))
                    if ship_number_select in ships_already_placed or ship_number_select > 4:
                        print("Invalid option, make sure you are not inputting the same ship again:")
                        for value in ships_already_placed:
                            if value == 1:
                                print(GPH.user_alr_placed_destroyer.center(welcome_screen_width, ' '))
                            elif value == 2:
                                print(GPH.user_alr_placed_frigate.center(welcome_screen_width, ' '))
                            elif value == 3:
                                print(GPH.user_alr_placed_carrier.center(welcome_screen_width, ' '))
                            elif value == 4:
                                print(GPH.user_alr_placed_submarine.center(welcome_screen_width, ' '))
                    elif ship_number_select not in ships_already_placed and ship_number_select <= 4:
                        ship_check = True;
                match ship_number_select:
                    case 1:
                        print("".center(welcome_screen_width, '='))
                        print("You chose to place a destroyer")
                        print("".center(welcome_screen_width, '='))
                        logic_engine_instance.get__tabletop_view(players[repetition].ship_grid)
                        print("".center(welcome_screen_width, '='))
                        print("Please enter the starting coordinates of the destroyer (row,column)")
                        row_position = int(input(GPH.user_needs_input_row))
                        col_position = int(input(GPH.user_needs_input_col))
                        direction_of_placement = str(input(GPH.user_needs_input_direction))
                        #! Quality of inputs control
                        if row_position > 6 or col_position > 6:
                            print(GPH.error_msg_row_too_high.center(welcome_screen_width, ' '))
                            continue
                        if (row_position < 0 or col_position < 0):
                            print(GPH.error_msg_row_too_low)
                            continue
                        if direction_of_placement.lower() != "horizontal" and direction_of_placement.lower() != "vertical":
                            print(GPH.error_msg_direction.center(welcome_screen_width, " "))
                            continue
                        logic_check = logic_engine_instance.set__disposition_of_ships("Destroyer",row_position,col_position,direction_of_placement,players[repetition].ship_grid)
                        if logic_check:
                            ships_placed += 1;
                            ships_already_placed.add(1);
                        else:
                            print(GPH.error_msg_full_ship_placement.center(welcome_screen_width, "="))
                        
                        system('cls')
                    case 2:
                        print("".center(welcome_screen_width, '='))
                        print("You chose to place a frigate")
                        print("".center(welcome_screen_width, '='))
                        logic_engine_instance.get__tabletop_view(players[repetition].ship_grid)
                        print("".center(welcome_screen_width, '='))
                        print("Please enter the starting coordinates of the frigate (row,column)")
                        row_position = int(input(GPH.user_needs_input_row))
                        col_position = int(input(GPH.user_needs_input_col))
                        direction_of_placement = str(input(GPH.user_needs_input_direction))
                        #! Quality of inputs control
                        if row_position > 6 or col_position > 6:
                            print(GPH.error_msg_row_too_high.center(welcome_screen_width, ' '))
                            continue
                        if (row_position < 0 or col_position < 0):
                            print(GPH.error_msg_row_too_low.center(welcome_screen_width, ' '))
                            continue
                        if direction_of_placement.lower() != "horizontal" and direction_of_placement.lower() != "vertical":
                            print(GPH.error_msg_direction.center(welcome_screen_width, " "))
                            continue
                    
                        logic_check = logic_engine_instance.set__disposition_of_ships("Frigate",row_position,col_position,direction_of_placement,players[repetition].ship_grid)
                        if logic_check:
                            ships_placed += 1;
                            ships_already_placed.add(2);
                        else:
                            print(GPH.error_msg_full_ship_placement.center(welcome_screen_width, "="))
                        
                        system('cls')
                    case 3: 
                        print("".center(welcome_screen_width, '='))
                        print("You chose to place a carrier")
                        print("".center(welcome_screen_width, '='))
                        logic_engine_instance.get__tabletop_view(players[repetition].ship_grid)
                        print("".center(welcome_screen_width, '='))
                        print("Please enter the starting coordinates of the carrier (row,column)")
                        row_position = int(input(GPH.user_needs_input_row))
                        col_position = int(input(GPH.user_needs_input_col))
                        direction_of_placement = str(input(GPH.user_needs_input_direction))
                        #! Quality of inputs control
                        if row_position > 6 or col_position > 6:
                            print(GPH.error_msg_row_too_high.center(welcome_screen_width, ' '))
                            continue
                        if (row_position < 0 or col_position < 0):
                            print(GPH.error_msg_row_too_low.center(welcome_screen_width, ' '))
                            continue
                        if direction_of_placement.lower() != "horizontal" and direction_of_placement.lower() != "vertical":
                            print(GPH.error_msg_direction.center(welcome_screen_width, " "))
                            continue

                        logic_check = logic_engine_instance.set__disposition_of_ships("Carrier",row_position,col_position,direction_of_placement,players[repetition].ship_grid)
                        if logic_check:
                            ships_placed += 1;
                            ships_already_placed.add(3);
                        else:
                            print(GPH.error_msg_full_ship_placement.center(welcome_screen_width, "="))
                        
                        system('cls')
                    case 4: 
                        print("".center(welcome_screen_width, '='))
                        print("You chose to place a Submarine")
                        print("".center(welcome_screen_width, '='))
                        logic_engine_instance.get__tabletop_view(players[repetition].ship_grid)
                        print("".center(welcome_screen_width, '='))
                        print("Please enter the starting coordinates of the submarine (row,column)")
                        row_position = int(input(GPH.user_needs_input_row))
                        col_position = int(input(GPH.user_needs_input_col))
                        direction_of_placement = str(input(GPH.user_needs_input_direction))
                        #! Quality of inputs control
                        if row_position > 6 or col_position > 6:
                            print(GPH.error_msg_row_too_high.center(welcome_screen_width, ' '))
                            continue
                        if (row_position < 0 or col_position < 0):
                            print(GPH.error_msg_row_too_low.center(welcome_screen_width, ' '))
                            continue
                        if direction_of_placement.lower() != "horizontal" and direction_of_placement.lower() != "vertical":
                            print(GPH.error_msg_direction.center(welcome_screen_width, " "))
                            continue
                            
                    
                        logic_check = logic_engine_instance.set__disposition_of_ships("Submarine",row_position,col_position,direction_of_placement,players[repetition].ship_grid)
                        if logic_check:
                            ships_placed += 1;
                            ships_already_placed.add(4);
                        else:
                            print(GPH.error_msg_full_ship_placement.center(welcome_screen_width, "="))
                        
                        system('cls')
            except ValueError:
                print("Incorrect Value, please ensure you are entering numbers and not text")
        ships_already_placed.clear();
        ships_placed = 0;
    system('cls')
    #! Implementation of the main game mechanism, a while loop for guessing a ship colision.
    #================================================
    #  *                    INFO
    #    The following section of code presents the main targetting
    #    sequence in the game, it allows users to guess a ships location and see it updated in the oponents grid. it will be based on a two level nested while loop
    #    The first while loop will check if any of the players ships location list are empty, the second one will check until there is a miss.
    #================================================

    #? Constants for ship_placement_checking

    list_of_ship_coordinates_p1:list = logic_engine_instance.get__cummulative_ship_positions__(players[0].ship_grid)
    list_of_ship_coordinates_p2:list = logic_engine_instance.get__cummulative_ship_positions__(players[1].ship_grid)
    player_turn_number:int = randint(0,1)
    while (len(list_of_ship_coordinates_p1) > 0) and (len(list_of_ship_coordinates_p2) >0):
        if (player_turn_number == 0):
            print(f"|{players[0].player_fname}'s turn|".center(welcome_screen_width, '=')) 
            logic_engine_instance.get__tabletop_view(players[0].ship_grid)
            print("This is your own grid...".center(welcome_screen_width, '='))
            print("Chose wisely a set of row, column coordinates for you to attack!")
            shot_result_bool_control = True;
            while shot_result_bool_control:
                try:
                    validity_check = False;
                    while (validity_check == False):
                        user_chosen_row: int = int(input(GPH.user_needs_input_row))
                        user_chosen_col: int = int(input(GPH.user_needs_input_col))
                        if user_chosen_row > 6 or user_chosen_col > 6:
                            print(GPH.error_msg_row_too_high.center(welcome_screen_width, ' '))
                            continue
                        if (user_chosen_row < 0 or user_chosen_col < 0):
                            print(GPH.error_msg_row_too_low.center(welcome_screen_width, ' '))
                            continue
                        if (user_chosen_row > 0 and user_chosen_row <= 6) and (user_chosen_col > 0 and user_chosen_col <= 6):
                            validity_check = True;
                    #? Enter the shot check from the main logic engine
                    shot_result: tuple = logic_engine_instance.set__shot_on_location(players[1].ship_grid,user_chosen_row,user_chosen_col)
                    shot_result_string, shot_result_bool_control = shot_result
                    players[player_turn_number].set___user_points_per_hit__(shot_result_string)
                    #? Informing the user of a hit or a miss
                    print(("| " + shot_result_string + " |").center(welcome_screen_width, '='))
                except ValueError:
                    print(GPH.error_msg_value_error_guess_section.center(welcome_screen_width, ' '))
            if shot_result_bool_control == False:
                player_turn_number = 1;
                list_of_ship_coordinates_p1:list = logic_engine_instance.get__cummulative_ship_positions__(players[0].ship_grid)
                list_of_ship_coordinates_p2:list = logic_engine_instance.get__cummulative_ship_positions__(players[1].ship_grid)
                system('cls')
        elif (player_turn_number == 1):
            print(f"|{players[1].player_fname}'s turn|".center(welcome_screen_width, '=')) 
            logic_engine_instance.get__tabletop_view(players[1].ship_grid)
            print("This is your own grid...".center(welcome_screen_width, '='))
            print("Chose wisely a set of row, column coordinates for you to attack!")
            shot_result_bool_control = True;
            while shot_result_bool_control:
                try:
                    validity_check = False;
                    while (validity_check == False):
                        user_chosen_row: int = int(input(GPH.user_needs_input_row))
                        user_chosen_col: int = int(input(GPH.user_needs_input_col))
                        if user_chosen_row > 6 or user_chosen_col > 6:
                            print(GPH.error_msg_row_too_high.center(welcome_screen_width, ' '))
                            continue
                        if (user_chosen_row < 0 or user_chosen_col < 0):
                            print(GPH.error_msg_row_too_low.center(welcome_screen_width, ' '))
                            continue
                        if (user_chosen_row > 0 and user_chosen_row <= 6) and (user_chosen_col > 0 and user_chosen_col <= 6):
                            validity_check = True;
                    #? Enter the shot check from the main logic engine
                    shot_result: tuple = logic_engine_instance.set__shot_on_location(players[0].ship_grid,user_chosen_row,user_chosen_col)
                    shot_result_string, shot_result_bool_control = shot_result
                    players[player_turn_number].set___user_points_per_hit__(shot_result_string)
                    print(("| " + shot_result_string + " |").center(welcome_screen_width, '='))
                except ValueError:
                    print(GPH.error_msg_value_error_guess_section.center(welcome_screen_width, ' '))
            if shot_result_bool_control == False:
                player_turn_number = 0;
                list_of_ship_coordinates_p1:list = logic_engine_instance.get__cummulative_ship_positions__(players[0].ship_grid)                
                list_of_ship_coordinates_p2:list = logic_engine_instance.get__cummulative_ship_positions__(players[1].ship_grid)
                system('cls')
    system('cls')
    #! Printing whoever won the game 
    if len(list_of_ship_coordinates_p1) == 0:
        print(f'Player 2 {players[1].player_fname} has won the game!')
        print(f'You finish the game with {players[1].puntaje_usuario} points!')
    elif len(list_of_ship_coordinates_p2) == 0:
        print(f'Player 1 {players[0].player_fname} has won the game!')
        print(f'You finish the game with {players[0].puntaje_usuario} points!')

    #? Return to main menu
    print("Returning to the main menu...".center(welcome_screen_width, '='))


