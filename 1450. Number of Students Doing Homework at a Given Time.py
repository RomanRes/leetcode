
startTime = [4]
endTime = [4]
queryTime = 4
counter = 0
for i in range(len(startTime)):
   if startTime[i] <= queryTime <= endTime[i]:
       counter += 1

print(counter)
