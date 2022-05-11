from random import randint
from time import sleep
from random import choice

simon_says = ["Hands on head", "Hands on ears",
          	"Right hand up", "Left hand up",
          	"Hands on shoulders"]
intros = ["Simon says...", ""]

for x in range(10):
 index = randint(0,4)
 instruction = simon_says[index]
 intro = choice(intros)
 print(intro,"{}".format(instruction))
 sleep(3)

