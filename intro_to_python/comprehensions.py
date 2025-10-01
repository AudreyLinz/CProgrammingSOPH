#create a function that returns a list of cubes for odd numbers and in a given range

def cubes_of_odds(start, end):
    return[x**3 for x in range(start, end+1) if x % 2!=0]

print(list(cubes_of_odds, (1,10)))