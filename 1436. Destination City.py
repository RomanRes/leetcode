paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

def destCity(paths):
    start = paths[0][1]
    paths = dict(paths)
    while paths.get(start):
        start = paths.get(start)
    return start
print(destCity(paths))


def destCity(paths):
    paths = dict(paths)
    return (set(paths.values()) - set(paths.keys())).pop()

print(destCity(paths))