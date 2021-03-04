moves = "RRDD"

def judgeCircle(moves):
    hmap = {"R":0, "U":0, "L":0, "D":0}
    for move in moves:
        hmap[move] += 1
    if hmap["R"] != hmap["L"] or hmap["U"] != hmap["D"]:
        return False
    return True

def judgeCircle(moves):
    if moves.count("R") != moves.count("L") or moves.count("U") != moves.count("D"):
        return False
    return True

print(judgeCircle(moves))


