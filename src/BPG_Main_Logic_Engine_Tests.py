from BPG_Main_Logic_Engine import Main_Game_Engine;

engine_test = Main_Game_Engine(1)
engine_test.set__num_of_players(3);
num_of_players = engine_test.get__num_of_players();
print(num_of_players);
game_grid_test = engine_test.define_game_grid();

for sub_list in game_grid_test:
    printable_row = "";
    for value in sub_list:
        printable_row += " ".join(value) + " ";
    print(printable_row);

print("\n")
engine_test.set__disposition_of_ships("Frigate",1,2,"Horizontal",game_grid_test)

engine_test.set__disposition_of_ships("Submarine",1,1,"Vertical",game_grid_test)
engine_test.set__disposition_of_ships("Carrier",1,6,"Vertical",game_grid_test)
for sub_list in game_grid_test:
    printable_row = "";
    for value in sub_list:
        printable_row += " ".join(value) + " ";
    print(printable_row);
engine_test.set__disposition_of_ships("Frigate",2,2,"Horizontal",game_grid_test)

result: tuple = engine_test.set__shot_on_location(game_grid_test,2,2)
result: tuple = engine_test.set__shot_on_location(game_grid_test,4,2)

for sub_list in game_grid_test:
    printable_row = "";
    for value in sub_list:
        printable_row += " ".join(value) + " ";
    print(printable_row);


list_of_position_pairs = engine_test.set__cummulative_ship_positions(game_grid_test)

for pair in list_of_position_pairs:
    print(pair);


