#######################################################
#
# COSC 140 Homework 2, "bus trip planner" problem
#
#######################################################

hours = input("What hour departure time? ")
minutes = input("What minute? ")
hours = float(hours)
minutes = float(minutes)

distance = input("How far are you trying to go? (km please) ")
stops = input("How many stops will there be? ")
distance = float(distance)
stops = int(stops)

totalSeconds = hours*3600+minutes*60
travelSeconds = distance/.01111111111+30*stops

totalSeconds += travelSeconds

seconds = int(totalSeconds)

secondsS = seconds%(3600*24)%60

minutes = seconds%(3600*24)//60%60
hours = seconds%86400//3600
days = seconds//86400

if days >0:
  hours - 24
  
print("Arrival time:",hours, ":", minutes, ":", secondsS)




