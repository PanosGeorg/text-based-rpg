import time
import random
from functionsgame import type_slow, battle

type_slow("Welcome to the game! Press x to continue.")
user_input = input()
if user_input.lower() != 'x':
    pass


type_slow("You wake up alone, in the middle of a dark forest. Noone with you, except silence.")
type_slow("You start walking to find a way out. Suddenly, a monster jumps from the bushes!")
time.sleep(1)
hero_health = 100  # hero's starting health
enemy_health = 50  #enemies' starting health
coins = 0
xp = 0
hero_health = battle(hero_health, enemy_health)
coins = coins + 10
xp = xp + 5
type_slow("You won 5xp and 10 gold! Press x to continue.")
user_input = input()
if user_input.lower() != 'x':
    pass

type_slow("You continue walking, till you reach a clearing. There you can see the remains of a campfire, and blood spilled on the ground.")
type_slow("There must have been a battle here, you think to yourself.")
type_slow("Before you know it, a new enemy attacks!")
time.sleep(1)
hero_health = battle(hero_health, enemy_health+5)
coins = coins + 12
xp = xp + 7
hero_health = 105
type_slow("You won 7xp and 12 gold! You leveled up! Your max health is now regenerated up to 105.")
type_slow("Press x to continue.")
user_input = input()
if user_input.lower() != 'x':
    pass

type_slow("You continue walking in the forest.")
type_slow("Suddenly, you see something shiny lying on the ground. You get closer, and you see that it is a sword! You pick it up.")
type_slow("Then, a goblin comes in front of you and blocks the way!")
hero_health = battle(hero_health, enemy_health+15)

type_slow("You win! That's the game for now, with updates to follow! :)")

