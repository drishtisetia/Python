width = float(input("What is the width of the floor in meters? :"))
height = float(input("What is the length of the floor in meters? :"))

width_tile = float(input("What is the width of the tile in meters? :"))
height_tile = float(input("What is the length of the tile in meters? :"))

price_of_tile = float(input("What is the price of one tile in dollars? :"))


area = ((width*height)/(width_tile*height_tile))
total_cost = area*price_of_tile
print("Total cost of the flooring will be : $",total_cost)
