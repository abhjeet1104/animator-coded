total_marks = 1000
cutoff = 400
scores = [100, 200, 300, 399, 500]

# I will keep on attempting until I succeed
year = 0 # indexing in python starts with 0

while scores[year] < cutoff:
  print(f"Your score is: {scores[year]}, cutoff: {cutoff}")
  print("I will attempt next year")
  year = year + 1 # I am adding 1 to current year
