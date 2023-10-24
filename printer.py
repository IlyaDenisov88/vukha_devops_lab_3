
with open ("numbers.txt", "w") as file:
  for line in range(0, 2):
    file.write(str(line))
    file.write('\n')
  file.close()
  
