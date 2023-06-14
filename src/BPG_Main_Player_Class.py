#===================================================================================================
#  ?                                           ABOUT
#  @author         :  Santiago Arellano
#  @repo           :  Battleship.io
#  @createdOn      :  08-06-23
#  @description    :  Implementation of the player class for the game Battleship.io
#===================================================================================================

#! Import declarations
import re as rgexp
#! Class definition for Main Player Class

class Main_Player_Class:
    def __init__(self, player_fname: str, player_id: int):
        self.player_fname: str = "";
        self.player_id: int = 0;
        regex_expression_for_names = '[A-Z][a-z]+';
        #? Check if the player's first name and last name are valid
        check = rgexp.match(regex_expression_for_names, player_fname);
        if check:
            self.player_fname= player_fname;
        else:
            self.player_fname = "Empty String";
        #? Check if the player's ID is valid
        if player_id > 0 and player_id < 100:
            self.player_id = player_id;

        #? Setting players points to zero
        self.puntaje_usuario: int = 0;
    #* Implementacion de una funcion para determinar el puntaje inicial y un metodo para cambiarla
    def set___user_points_per_hit__(self, result_for_point_alloting: str):
        match result_for_point_alloting:
            case "Miss!":
                self.puntaje_usuario += 0;
            case "Hit on a Frigate!":
                self.puntaje_usuario += 10;
            case "Hit on a Destroyer!":
                self.puntaje_usuario += 50;
            case "Hit on a Submarine!":
                self.puntaje_usuario += 75;
            case "Hit on a Carrier!":
                self.puntaje_usuario += 100;
    def set_player_ship_grid_with_locations(self, ship_grid: list):
        self.ship_grid = ship_grid;

    

