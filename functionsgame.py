import random
import time

def battle(hero_health, enemy_health):           # function that handles 
    defending = False                            # the battle with the enemy
    while hero_health > 0 and enemy_health > 0:  
        
        

        print("Choose your action:")     #player chooses what to do
        print("1. Attack")
        print("2. Defend")
        choice = input("Enter your choice: ")

        if choice == '1':                # player attacks
            hit_chance = random.random()
            if hit_chance <= 0.8:
                damage = random.randint(10, 20)
                type_slow(f"You hit the enemy for {damage} damage!")
                enemy_health -= damage
                if enemy_health > 0:
                    type_slow(f"Enemy Health: {enemy_health}")
                    time.sleep(1)
            else:
                type_slow("You missed!")
                time.sleep(1)

        elif choice == '2':            # player defends
            defending = True
            type_slow("You choose to defend. You take reduced damage from the enemy's attack.")
            time.sleep(1)
            

        else:
            type_slow("Invalid choice. Please choose 1 or 2.")

        if enemy_health <= 0:
            break  

        enemy_damage = random.randint(5, 15)   #enemy's turn to attack
        if defending:
            enemy_damage *= 0.8 # reduces enemy damage by 20% when defending
            defending = False   # resets defending status
        type_slow(f"The enemy attacks and deals {enemy_damage} damage to you!")
        hero_health -= enemy_damage
        if hero_health > 0:
            type_slow(f"Hero Health: {hero_health}")
            time.sleep(1)
    
    if hero_health <= 0:
        type_slow("You have been defeated. Game over.")
        return 0
    else:
        type_slow("You defeated the enemy! Victory!")
        return hero_health


def type_slow(text):   # makes text print lower like a retro game
    for char in text:
        print(char, end='', flush=True)  # prints each character
        time.sleep(0.03)  # adds delay
    print()  # newline
