import random

def create_pumpkin():
  stem = "   ^   "
  middle = "|#####|"
  bottom = "|#####|"

  random_value = random.random()
  if (random_value <= 0.33):
    top = " /###\\ "
  elif (random_value <= 0.66):
    top = " /...\\ "
  else:
    top = " /|||\ "

  random_value = random.random()
  if (random_value <= 0.16):
    eyes = "|  ^  |"
  elif (random_value <= 0.33):
    eyes = "|  _  |"
  elif (random_value <= 0.5):
    eyes = "|  -  |"
  elif (random_value <= 0.66):
    eyes = "|  ~  |"
  elif (random_value <= 0.83):
    eyes = "|     |"
  else:
    eyes = "|#####|"

  random_value = random.random()
  if (random_value <= 0.2):
    mouth = "| / \\ |"
  elif (random_value <= 0.4):
    mouth = "| ~ ~ |"
  elif (random_value <= 0.6):
    mouth = "| - - |"
  elif (random_value <= 0.8):
    mouth = "| ^ ^ |"
  else:
    mouth = "| * * |"

  pumpkin = [
    stem,
    top,
    middle,
    bottom,
    eyes,
    mouth
  ]

  return pumpkin

def print_pumpkin(pumpkin):
  for line in pumpkin:
    print(line)

pumpkin = create_pumpkin()
print_pumpkin(pumpkin)
