import os
import random
from pprint import pprint
import Pokeload as pl

# Creamos al jugador como un diccionario, con 3 pokemones random.
def get_player_profile(pokemon_list):
    return {
        "player_name": input("¿Cuál es tu nombre? "),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)],
        "combats": 0,
        "pokeballs": 0,
        "potions": 0
    }

# Checar si sigue vivo algun pokemon del entrenador
def any_player_pokemon_lives(player_profile):
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0

# El jugador elige con que pokemon iniciar el combate
def choose_pokemon(player_profile):
    pk1 = player_profile["pokemon_inventory"][0]
    pk2 = player_profile["pokemon_inventory"][1]
    pk3 = player_profile["pokemon_inventory"][2]
    print("{} estos son tus pokemón: {}, {} y {} \n".format(player_profile["player_name"], pk1["name"], pk2["name"],
                                                            pk3["name"]))
    player_choice = input("¿Con cuál pokemón quieres pelear? (Introduce el nombre) ").lower()
    if player_choice == pk1["name"].lower():
        pokemon_fighting = pk1.copy()
    elif player_choice == pk2["name"].lower():
        pokemon_fighting = pk2.copy()
    elif player_choice == pk3["name"].lower():
        pokemon_fighting = pk3.copy()
    else:
        print("No has introducido ningún nombre de pokemón, eligiendolo al azar...")
        pokemon_fighting = random.choice[pk1, pk2, pk3]
    return pokemon_fighting

# El combate del jugador.
def player_turn(player_profile, pokemon_fighting, enemy_pokemon):
    end_turn = True
    while end_turn:
        player_move = input("¿Que debería hacer? (M) Movimientos (C) Características del pokemón (H) Huir ")
        if player_move == "M":
            for attack in pokemon_fighting["attacks"]:
                print("Ataque: {} dmg / {}" .format(attack["name"],
                                                    attack["damage"]))
            player_move2 = input("Elige un ataque o presiona (P) para cambiar de pokemón ").lower()
            for attack in pokemon_fighting["attacks"]:
                if player_move2 == attack["name"].lower():
                    print("{} usa {}" .format(pokemon_fighting["name"], player_move2))
                    enemy_pokemon["current_health"] -= attack["damage"]
                    print("{} le hace {} de daño al pokemón enemigo" .format(pokemon_fighting["name"],
                                                                                 attack["damage"]))
                    end_turn = False
            if player_move2 == "P":
                choose_pokemon(player_profile)
                end_turn = False
        elif player_move == "C":
            print("\n Estas son las características de tu pokemón: Nombre: {} Tipo: {} Vida: {}/{} Nivel: {} \n"
                  .format(pokemon_fighting["name"], pokemon_fighting["type"], pokemon_fighting["current_health"],
                          pokemon_fighting["base_health"], pokemon_fighting["level"]))
        elif player_move == "H":
            print("Venga, no seas cobarde {} ¡LUCHA!" .format(player_profile["player_name"]))
        else:
            print("No has introducido un comando correcto, intenta de nuevo...")

# El turno del pokemon salvaje!
def enemy_turn(enemy_pokemon, pokemon_fighting):
    print("Después de tu turno al {} le queda {}/{} de vida"
          .format(enemy_pokemon["name"], enemy_pokemon["current_health"], enemy_pokemon["base_health"]))
    enemy_attack = random.choice(enemy_pokemon["attacks"])
    print("El {} enemigo usa {} y te hace {} de daño" .format(enemy_pokemon["name"], enemy_attack["name"],
                                                              enemy_attack["damage"]))
    pokemon_fighting["current_health"] -= enemy_attack["damage"]
    print("A tu {} le queda {}/{} de vida" .format(pokemon_fighting["name"], pokemon_fighting["current_health"],
                                                   pokemon_fighting["base_health"]))

# Inicio de la batalla.
def fight(player_profile, enemy_pokemon):
    print("¡Comienza la batalla pokemón!")
    print("\n Un {} salvaje ha aparecido \n" .format(enemy_pokemon["name"]))
    pokemon_fighting = choose_pokemon(player_profile)
    print("¡Adelante {}!" .format(pokemon_fighting["name"]))
    player_turn(player_profile, pokemon_fighting, enemy_pokemon)
    enemy_turn(enemy_pokemon, pokemon_fighting)


def main():
    pokemon_list = pl.get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)
    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(pokemon_list)
        fight(player_profile, enemy_pokemon)
    print("Has perdido en el combate {}".format(player_profile["combats"]))


if __name__ == "__main__":
    main()
