#===================================================================================================
#  ?                                           ABOUT
#  @author         :  Santiago Arellano
#  @email          :  santiagofarellanoj@gmail.com
#  @repo           :  Battleship.io
#  @createdOn      :  08-06-23
#  @description    :  Implementation of the player class for the game Battleship.io
#===================================================================================================

#! Import declarations
import regex as rgexp
#! Class definition for Main Player Class

class Main_Player_Class:
    def __init__(self, player_fname: str, player_lname: str, player_id: int):
        self.player_fname: str = "";
        self.player_lname: str = "";
        self.player_id: int = 0;
        regex_expression_for_names = rgexp.Regex('[A-Z][a-z]+');
        #? Check if the player's first name and last name are valid
        check = rgexp.match(regex_expression_for_names, player_fname);
        if check:
            self.player_fname= player_fname;
        else:
            self.player_fname = "Empty String";
        check = rgexp.match(regex_expression_for_names, player_lname);
        if check: 
            self.player_lname = player_lname;
        else:
            self.player_lname = "Empty String";

        #? Check if the player's ID is valid
        if player_id > 0 and player_id < 100:
            self.player_id = player_id;

