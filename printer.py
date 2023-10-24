with open ("numbers.txt", "w") as file:
  file.close()
  for line in range(0, random.randint(1, 100)):
    file.write(line + '\n')
  
