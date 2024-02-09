numheads=35
numlegs=94
rabbits=int()
chickens=int()
def solve(numheads, numlegs):
    rabbits = (numlegs-(2*numheads))/2
    chickens = numheads-rabbits
    print(rabbits, chickens)
solve(numheads, numlegs)