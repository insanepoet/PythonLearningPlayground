from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

'''
Spells
'''
#  Black Magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")

#  White Magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")

player_magic = [fire, thunder, blizzard, meteor, cure, cura]


'''
Items
'''
#  Potions
potion = Item("Potion", "potion", "Heals 100 HP", 100)
hipotion = Item("Hi-Potion", "potion", "Heals 500 HP", 500)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)

#  Elixirs
elixer = Item("Elixir", "elixir", "Full restores HP/MP of one party member", 9999)
hielixir = Item("Hi-Elixir", "elixir", "Fully restores party's HP/MP", 9999)

#  Damage
grenade = Item("Grenade", "attack", "Deals 500 Damage", 500)
bomb = Item("Bomb", "attack", "Deals 1000 Damage", 1000)

player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixir, "quantity": 2}, {"item": grenade, "quantity": 3},
                {"item": bomb, "quantity": 3}]

'''
PC / NPCS
'''
player1 = Person("Valos", 3260, 132, 300, 34, player_magic, player_items)
player2 = Person("Sarah", 4160, 188, 311, 34, player_magic, player_items)
player3 = Person("Robot", 3089, 274, 288, 34, player_magic, player_items)

enemy = Person("Magus", 11200, 500, 701, 25, [], [])

players = [player1, player2, player3]
'''
MAIN SCRIPT
'''


running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("========================")
    print("\n")
    print("Name               HP                                                     MP")
    for player in players:
        player.get_stats()

    print("\n")

    for player in players:
        player.choose_action()
        choice = input("Choose " + player.name + "'s action:")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attack for", dmg, "points of damage.")
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose Spell to Cast:")) - 1

            # If user hits 0 go back
            if magic_choice == -1:
                continue

            # Get info about caster / spell
            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()
            current_mp = player.get_mp()

            # Check to ensure caster has enough mp
            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            # Reduce caster MP by spell cost
            player.reduce_mp(spell.cost)

            # Cast the spell
            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type =="black":
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage." +bcolors.ENDC)

        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose ItemL")) - 1

            # If user presses 0 go back
            if item_choice == -1:
                continue

            # Set the item locally
            item = player.items[item_choice]["item"]

            # Check to ensure item is in inventory
            if player.items[item_choice]["quantity"] ==0:
                print(bcolors.FAIL + "\n" + "You have no more " + item.name + "'s remaining" + bcolors.ENDC)
                continue

            # Remove one from inventory
            player.items[item_choice]["quantity"] -= 1

            # Use the Item
            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP." + bcolors.ENDC)
            elif item.type == "elixir":
                if item.name == "Hi-Elixir":
                    # Player
                    player.hp = player.max_hp
                    player.mp = player.max_mp
                    # Party not yet implemented

                    print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage." +bcolors.ENDC)



    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "!")
    print("-------------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "The Enemy has defeated you!" + bcolors.ENDC)
        running = False

    #  running = False


'''
print("Test Rand Atk Dmg")
print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())

print("Test Rand Spell Dmg")
print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))
print(player.generate_spell_damage(2))
'''