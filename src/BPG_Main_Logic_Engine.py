#===================================================================================================
#  ?                                           ABOUT
#  @author         :  Santiago Arellano
#  @email          :  santiagofarellanoj@gmail.com
#  @repo           :  Battleship.io
#  @createdOn      :  07-06-23
#  @description    :  Representation of the Iconic Battleship Game
#===================================================================================================
#! Import declarations
from random import randint
from array import array


#! Class definition for the game mechanics

class Main_Game_Engine:
    #? Initial Constructor
    def __init__(self, number_of_players: int):
        try:
            self.number_of_players: int = number_of_players;
            self.max_number_of_guesses: int = 10;
            self.amount_of_turns_till_end: int = 0;
        except (ValueError):
            self.number_of_players: int = 1;
    #? Function to redefine the number of players and get the value
    def set__num_of_players(self, number_of_players: int):
        try:
            self.number_of_players: int = number_of_players;
        except (ValueError):
            self.number_of_players: int = 1;
    def get__num_of_players(self):
        return self.number_of_players;
    #? Function to define the initial grid size for the game
    def define_game_grid(self):
        game_grid = [];
        for row in range(0,6,1):
            game_grid_row = [];
            for col in range(0,6,1):
                game_grid_row.append('[   ]');
            game_grid.append(game_grid_row);
        self.game_grid: list = game_grid;
        return game_grid;
    #? Function to define the disposition of ships
    def set__disposition_of_ships(self, type_of_ship: str, starting_position_x: int, starting_position_y: int, direction_of_ships_placement: str, players_board: list):
        #* Check to see which type of battleship we are working with in terms of sizing nothing will go further than 6 in either direction
        battleship_type: str = type_of_ship;
        battleship_length: int = 0;
        battleship_direction_based_on_ship: str = direction_of_ships_placement.lower();
        match battleship_type.capitalize():
            case "Frigate":
                battleship_length = 3;
            case "Destroyer":
                battleship_length = 4;
            case "Submarine":
                battleship_length = 2;
            case "Carrier":
                battleship_length = 5;
        #* Setting up based on the initial x and y coordinates and direction
        if battleship_direction_based_on_ship.lower() == "horizontal":
            for unit_of_length in range(0,battleship_length,1):
                players_board[starting_position_x-1][(starting_position_y-1) + unit_of_length] = "[ "+battleship_type[0:1:1] + " ]" ;
        if direction_of_ships_placement.lower() == "vertical":
            for unit_of_length in range(0,battleship_length,1):
                players_board[(starting_position_x -1)+ unit_of_length][starting_position_y-1] = "[ "+battleship_type[0:1:1] + " ]" ;
    def set__shot_on_location(self, player_grid: list, shot_x: int, shot_y: int):
        #* Comparing the value on the shot direction with the current value to see if its the initial of a ship


        
        
    
        
                



