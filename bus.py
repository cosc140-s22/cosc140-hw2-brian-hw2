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

traveltime = distance/0.01111 - 30*stops

secondstravelled = (traveltime%(3600)%60)
minutestravelled = int(traveltime%(3600)//60%60)
hourstravelled = int(traveltime//3600)

fminutes = int(minutestravelled + minutes)

if fminutes > 59:
  hourstravelled+=1
  fminutes=fminutes%60
secondstravelled = int(secondstravelled)
print("Arrival time is: ",int(hourstravelled+hours),":",fminutes,":",secondstravelled)





