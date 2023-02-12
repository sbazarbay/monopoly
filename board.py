import csv


class Tile(object):
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def __str__(self):
        return (self.name)


class RailwayStation(Tile):
    pass


class Chance(Tile):
    pass


class Chest(Tile):
    pass


class Board(object):
    income = 200
    tiles = [None for _ in range(40)]
    streets = []
    utilities = []

    def __init__(self):
        return
    
    def setup_board(self):
        streets = []
        with open("streets.csv", "r") as streets_csv:
            streets_reader = csv.reader(streets_csv, delimiter=',')
            header = next(streets_reader)
            for street in streets_reader:
                self.streets.append(street)
        with open("utilities.csv", "r") as utilities_csv:
            utilities_reader = csv.reader(utilities_csv, delimiter=',')
            header = next(utilities_reader)
            for utility in utilities_reader:
                self.utilities.append(utility)
        
        # add corners
        start = Tile("Start", 0)
        jail = Tile("Jail", 10)
        parking = Tile("Free Parking", 20)
        go_to_jail = Tile("Go to Jail", 30)
        self.tiles[0] = start
        self.tiles[10] = jail
        self.tiles[20] = parking
        self.tiles[30] = go_to_jail

        # add streets
        for index, street in zip([1,3,6,8,9,11,13,14,16,18,19,21,23,24,26,27,29,31,32,34,37,39], self.streets):
            self.tiles[index] = Tile(street[0], index)
        
        # add taxes
        for index, utility in zip([4, 12, 28, 38], self.utilities):
            self.tiles[index] = Tile(utility[0], index)

        # add rails
        for index in [5, 15, 25, 35]:
            self.tiles[index] = RailwayStation("Railway station", index)

        # add chances
        for index in [7, 22, 36]:
            self.tiles[index] = Chance("Chance", index)

        # add chests
        for index in [2, 17, 33]:
            self.tiles[index] = Chest("Chest", index)
    
    def print_board(self):
        for i, tile in enumerate(self.tiles):
            print(i, tile)


board = Board()
board.setup_board()
board.print_board()
