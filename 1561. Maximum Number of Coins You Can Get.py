
piles = [9, 8, 8, 7, 6, 5]

def maxCoins(piles):
    return sum(sorted(piles)[int(len(piles)/ 3):][:-1:2])


print(maxCoins(piles))
