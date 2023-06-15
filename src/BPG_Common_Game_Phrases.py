#===================================================================================================
#  ?                                           ABOUT
#  @author         :  Santiago Arellano
#  @repo           :  Battleship.io
#  @createdOn      :  14-06-23
#  @description    :  Definition of a variety of game phrases that can be extracted as constant to declutter game files
#===================================================================================================

#? Incorrect value for name
incorrect_value_name_check: str = "|Incorrect Value, please ensure you are entering text and not numbers|"

#? Already placed ships
user_alr_placed_destroyer: str = "|You have already placed a Destroyer|"
user_alr_placed_frigate: str = "|You have already placed a Frigate|"
user_alr_places_carrier: str = "|You have already placed a Carrier|"
user_alr_placed_submarine:str = "|You have already placed a Submarine|"

#? Row and Column input declarations
user_needs_input_row: str = "|Row [1-6]: "
user_needs_input_col: str = "|Column [1-6]: "
user_needs_input_direction: str = "|Direction of placement (horizontal or vertical): "

#? Error messages for row placement

error_msg_row_too_high: str = "|Invalid location please try again, make sure you are sending columns and rows less than 6.|"
error_msg_row_too_low: str = "|Invalid location please try again, make sure you are sending columns and rows higher than 0.|"
error_msg_direction: str = "|Invalid direction please try again, make sure you are sending either horizontal or vertical.|"
error_msg_full_ship_placement = "|Ship placement failed, try again|"

#? Error message for ValueError guessing clause
error_msg_value_error_guess_section: str = "|Invalid value, please ensure you are entering text and not numbers|"