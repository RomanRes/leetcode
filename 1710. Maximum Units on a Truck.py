boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4

def maximumUnits(boxTypes, truckSize: int) -> int:
    boxTypes.sort(key=lambda a: a[1], reverse = True)
    result = 0
    for box, unit in boxTypes:
        if truckSize != 0:
            while box > 0 and truckSize != 0:
                result += unit
                box -= 1
                truckSize -= 1
        else:
            return result
    return result
print(maximumUnits(boxTypes, truckSize))

boxTypes = [[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]

truckSize = 35
def maximumUnits(boxTypes, truckSize: int) -> int:
    boxTypes.sort(key=lambda a: a[1], reverse = True)
    result = 0
    for box, unit in boxTypes:
        result += min(box, truckSize) * unit
        truckSize -= box
        if truckSize <= 0:
            return result
    return result
print(maximumUnits(boxTypes, truckSize))