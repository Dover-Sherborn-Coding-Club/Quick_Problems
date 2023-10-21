import random

#This program creates a pumpkin (I can't make this look beter) with random colors for each line and slightly different randomly generated figures
#Two inputs, how much of each color is going to be randomly generated and the number of figures to generate

number_of_figures = 2

colors = {
  #Black
  "\033[30m": 1,

  #Red
  "\033[91m": 1,

  #Green
  "\033[32m": 1,

  #Yellow
  "\033[33m": 1,

  #Blue
  "\033[34m": 1,

  #Magenta (Pink/Purple)
  "\033[35m": 1,

  #Cyan (Fluorescent Blue)
  "\033[36m": 1,
}

#Generates a random color
def generate_random_color():
  color_choices=[]
  for color_code in colors:
    num_of_color = colors[color_code]
    while num_of_color > 0:
      color_choices.append(color_code)
      num_of_color -= 1
  return random.choice(color_choices)

#Resets the color
def default_color():
    return "\033[0m"

#Creates a pumpkin figure
def create_pumpkin():
  stem = "    ^     "
  middle = " /#####\\"
  layer = "/#######\\"
  bottom = "|#######|"

  random_value = random.random()
  if (random_value <= 0.33):
    top = "  /###\\ "
  elif (random_value <= 0.66):
    top = "  /...\\ "
  else:
    top = "  /|||\ "

  random_value = random.random()
  if (random_value <= 0.16):
    eyes = "|   ^   |"
  elif (random_value <= 0.33):
    eyes = "|   _   |"
  elif (random_value <= 0.5):
    eyes = "|   -   |"
  elif (random_value <= 0.66):
    eyes = "|   ~   |"
  elif (random_value <= 0.83):
    eyes = "|       |"
  else:
    eyes = "|#######|"

  random_value = random.random()
  if (random_value <= 0.2):
    mouth = "|  / \\  |"
  elif (random_value <= 0.4):
    mouth = "|  ~ ~  |"
  elif (random_value <= 0.6):
    mouth = "|  - -  |"
  elif (random_value <= 0.8):
    mouth = "|  ^ ^  |"
  else:
    mouth = "|  * *  |"

  pumpkin = [
    stem,
    top,
    middle,
    bottom,
    eyes,
    mouth,
  ]

  return pumpkin

#Makes pumpkin figures with random colors
def make_pumpkin():
  for i in range(number_of_figures + 1):
    pumpkin = create_pumpkin()
    if (i >= 1):
      for lines in pumpkin:
        print(" " * (5 // 2 - 5) + generate_random_color() + lines + default_color())
    if (i == number_of_figures):
      break
    print ("\n")

if (__name__ == "__main__"):
  print("\nPumpkin Pattern:")
  make_pumpkin()
