# Train journey 
stations = ["Station 01", "Station 02", "Station 03", "Station 04"]

current_station = 0
destination_station = "Station 03"

while stations[current_station] != destination_station:
  print(f"current station is: {stations[current_station]}")
  print(f"my destination is: {destination_station}")
  print("Continue the journey I haven't reached the destination")
  current_station = current_station + 1
  print(f"Next station is: {stations[current_station]}")
  print("-----")
else:
  print(f"I have arrived at: {stations[current_station]}")  

stations = ["Station 01", "Station 02", "Station 03", "Station 04"]

current_station = 0
destination_station = "Station 03"

while stations[current_station] != destination_station:
  print(f"current station is: {stations[current_station]}")
  print(f"my destination is: {destination_station}")
  print("Continue the journey I haven't reached the destination")
  current_station = current_station + 1
  print(f"Next station is: {stations[current_station]}")
  print("-----")
