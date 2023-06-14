#===================================================================================================
#  ?                                           ABOUT
#  @author         :  Santiago Arellano
#  @repo           :  Battleship.io
#  @createdOn      :  07-06-23
#  @description    :  Implementation of the Main Logic Engine class for the game Battleship.io
#===================================================================================================



#! Class definition for the game mechanic
class Main_Game_Engine:
    #? Initial Constructor
    def __init__(self, number_of_players: int):
        try:
            self.number_of_players: int = number_of_players;
            self.max_number_of_guesses: int = 10;
            self.amount_of_turns_till_end: int = 0;
        except (ValueError):
            self.number_of_players: int = 1;
    #? Function to increment movements by one;
    def set__turns_increment(self):
        self.amount_of_turns_till_end += 1;
    def get__turns_increment(self):
        return self.amount_of_turns_till_end;
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
    def get__ship_near_colisions(self, direction_of_ship_placement:str,ship_size: int, players_board: list, starting_position_row: int, starting_position_col: int):
        colisions_list: set(int) = set(); 
        error_on_bound_message: str = "The values presented for initial position are out of bounds"
        if (starting_position_row -1 > 5 or starting_position_row -1 < 0) or (starting_position_col -1 > 5 or starting_position_col -1 < 0):
            return error_on_bound_message
        else:
            if direction_of_ship_placement.lower() == "vertical":
                for unit_of_len in range(0,ship_size-1,1):
                    try:
                        #? Check in place:
                        if players_board[(starting_position_row-1)+unit_of_len][starting_position_col-1] != "[   ]":
                            colisions_list.add("Colision on Starting Place");
                        #? Check Below:
                        if players_board[starting_position_row + unit_of_len][starting_position_col-1] != "[   ]":
                            colisions_list.add("Colision below");
                    except IndexError:
                        print("Stopping the execution of the check given that the ship in question is going out of bounds. Ensure that your starting row and columns are within bounds and the ships direction will not cause the ship to go out of the board.")
                        colisions_list.clear()
                        colisions_list.add(404)
                        return colisions_list
            elif direction_of_ship_placement.lower() == "horizontal":
                
                for unit_of_len in range(0,ship_size-1,1):
                    #? Check in place:
                    try:
                        if players_board[starting_position_row-1][(starting_position_col-1)+unit_of_len] != "[   ]":
                            colisions_list.add("Colision on Starting Place");
                        #? Check Right:
                        if players_board[starting_position_row-1][starting_position_col + unit_of_len] != "[   ]":
                            colisions_list.add("Colision Right");
                    except IndexError:
                        print("Stopping the execution of the check given that the ship in question is going out of bounds. Ensure that your starting row and columns are within bounds and the ships direction will not cause the ship to go out of the board.")
                        colisions_list.clear()
                        colisions_list.add(404)
                        return colisions_list

        return colisions_list;                
    def set__disposition_of_ships(self, type_of_ship: str, starting_position_row: int, starting_position_col: int, direction_of_ships_placement: str, players_board: list):
        #* Check to see which type of battleship we are working with in terms of sizing nothing will go further than 6 in either direction 
        placement_result = True;
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
        
        #* Checking to see if the starting position & orientation is valid
        colisions_check = self.get__ship_near_colisions(direction_of_ships_placement,battleship_length,players_board,starting_position_row,starting_position_col)
        for value in colisions_check:
            if value == 404:
                print("Stopping the execution of ship placement given that ship is going out of bounds, consider that ships go from left to right and if not placed carefully might go out of bounds")
                placement_result = False;
                return placement_result;
            else: 
                continue;
        
        if len(colisions_check) == 0:
            len_control = 0;
            if battleship_direction_based_on_ship.lower() == "horizontal":
                try:
                    for unit_of_length in range(0,battleship_length,1):
                        len_control += 1;
                        players_board[starting_position_row-1][(starting_position_col-1) + unit_of_length] = "[ "+battleship_type[0:1:1] + " ]" ;
                except IndexError:
                    print("Ships placement has failed due to it being placed outside of the bounds of the board.\n Incident information:\n1. Row: " + str(starting_position_row) + "\n2. Column: " + str(starting_position_col))
                    for unit_of_length in range(0, len_control,1):
                        players_board[starting_position_row-1][(starting_position_col-1) + unit_of_length] = "[   ]" ;
                    len_control = 0;
                    placement_result = False;
            if direction_of_ships_placement.lower() == "vertical":
                try:
                    for unit_of_length in range(0,battleship_length,1):
                        len_control += 1;
                        players_board[(starting_position_row -1)+ unit_of_length][starting_position_col-1] = "[ "+battleship_type[0:1:1] + " ]" ;
                except IndexError:
                    print("Ships placement has failed due to it being placed outside of the bounds of the board.\n Incident information:\n1. Row: " + str(starting_position_row) + "\n2. Column: " + str(starting_position_col))
                    players_board[(starting_position_row -1)+ unit_of_length][starting_position_col-1] = "[   ]";
                    placement_result = False;
        else:   
            print(f'The |{type_of_ship}| you are trying to place on |{starting_position_row}| |{starting_position_col}| presents the following colisions with the ships')
            for value in enumerate(colisions_check, start=1):
                print(value)
            user_decision: str = ""
            while (user_decision.upper() != "Y" and user_decision.upper() != "N"):
                try:
                    user_decision = input("Would you like to place it either way or skip this placement? (Y/N)")
                except ValueError:
                    print("Please enter a valid string value (Y or N)")
                    continue
            if user_decision.upper() == "N":
                print("Acknowledge passing up this placement request Captain!")
                placement_result = False;
                return placement_result;
            elif user_decision.upper() == "Y":
                len_control = 0;
                if battleship_direction_based_on_ship.lower() == "horizontal":
                    try:
                        for unit_of_length in range(0,battleship_length,1):
                            len_control += 1;
                            players_board[starting_position_row-1][(starting_position_col-1) + unit_of_length] = "[ "+battleship_type[0:1:1] + " ]" ;
                    except IndexError:
                        print("Ships placement has failed due to it being placed outside of the bounds of the board.\n Incident information:\n1. Row: " + str(starting_position_row) + "\n2. Column: " + str(starting_position_col))
                        for unit_of_length in range(0, len_control,1):
                            players_board[starting_position_row-1][(starting_position_col-1) + unit_of_length] = "[   ]" ;
                        len_control = 0;
                        placement_result = False;
                if direction_of_ships_placement.lower() == "vertical":
                    try:
                        for unit_of_length in range(0,battleship_length,1):
                            len_control += 1;
                            players_board[(starting_position_row -1)+ unit_of_length][starting_position_col-1] = "[ "+battleship_type[0:1:1] + " ]" ;
                    except IndexError:
                        print("Ships placement has failed due to it being placed outside of the bounds of the board.\n Incident information:\n1. Row: " + str(starting_position_row) + "\n2. Column: " + str(starting_position_col))
                        players_board[(starting_position_row -1)+ unit_of_length][starting_position_col-1] = "[   ]";
                        placement_result = False;
        return placement_result;
    
    def set__shot_on_location(self, enemy_player_grid: list, shot_row: int, shot_col: int):
        #* Comparing the value on the shot direction with the current value to see if its the initial of a ship
        present_value_on_location = enemy_player_grid[shot_row-1][shot_col-1];
        result = "Miss!";
        result_for_point_alloting = False;
        match present_value_on_location:
            case "[   ]":
                result = "Miss!";
                result_for_point_alloting = False;
                enemy_player_grid[shot_row-1][shot_col-1] = "[ \xD8 ]";
            case "[ F ]":
                result = "Hit on a Frigate!"
                result_for_point_alloting = True;
                enemy_player_grid[shot_row-1][shot_col-1] = "[ \xD7 ]";
            case "[ D ]":
                result = "Hit on a Destroyer!";
                result_for_point_alloting = True;
                enemy_player_grid[shot_row-1][shot_col-1] = "[ \xD7 ]";
            case "[ S ]":
                result = "Hit on a Submarine!";
                result_for_point_alloting = True;
                enemy_player_grid[shot_row-1][shot_col-1] = "[ \xD7 ]";
            case "[ C ]":
                result = "Hit on a Carrier";
                result_for_point_alloting = True;
                enemy_player_grid[shot_row-1][shot_col-1] = "[ \xD7 ]";
        results_tuple = (result, result_for_point_alloting);
        return results_tuple;

    #? Function to analyze the board and save positions of each ship for the player
    def get__cummulative_ship_positions__(self, player_board: list):
        ship_positions_pairs: list = list()
        for row in range(0,6,1):
            for col in range(0,6,1):
                if player_board[row][col] != "[   ]":
                    ship_positions_pairs.append((row,col))
                else:
                    continue
        return ship_positions_pairs;
    def get__tabletop_view(self, player_board: list):
        for sub_list in player_board:
            printable_row = "";
            for value in sub_list:
                printable_row += " ".join(value) + " ";
            print(printable_row);


        
if __name__ == "__main__":
    print("This is a source file dont run alone")
    
        
                



