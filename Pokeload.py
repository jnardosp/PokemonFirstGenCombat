import pickle
from requests_html import HTMLSession

# El "constructor" del pokemon(diccionario).
pokemon_base = {
    "name": "",
    "current_health": 100,
    "base_health": 100,
    "type": None,
    "level": 1,
    "current_exp": 0
}
POKEDEX_URL = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk="

# Creamos un pokemon(diccionario) a partir de su página de pokedex!
def get_pokemon(index):
    url = "{}{}" .format(POKEDEX_URL, index)
    session = HTMLSession()
    pokedex_page = session.get(url)
    new_pokemon = pokemon_base.copy()
    new_pokemon["name"] = pokedex_page.html.find("span", first=True).find(".mini", first=True).text
    new_pokemon["type"] = []

    for img in pokedex_page.html.find(".pkmain", first=True).find(".bordeambos", first=True).find("img"):
        new_pokemon["type"].append(img.attrs["alt"])

    new_pokemon["attacks"] = []

    for attack_item in pokedex_page.html.find(".pkmain")[-1].find("tr .check3"):
        attack = {
            "name": attack_item.find("td", first=True).find("a", first=True).text,
            "type": attack_item.find("td")[1].find("img", first=True).attrs["alt"],
            "min level": attack_item.find("th", first=True).text,
            "damage": int(attack_item.find("td")[3].text.replace("--", "0"))
        }
        new_pokemon["attacks"].append(attack)

    return new_pokemon


def get_all_pokemons():
    # Si ya existe un archivo con los pokemones lo cargamos.
    try:
        print("¡Buscando archivo de pokemons!")
        with open("pokefile.pkl", "rb") as pokefile:
            all_pokemons = pickle.load(pokefile)

    # De lo contrario creamos el archivo con los pokemones.
    except FileNotFoundError:
        print("Archivo no encontrado, descargando de internet...")
        all_pokemons = []
        for index in range(151):
            all_pokemons.append(get_pokemon(index + 1))
        with open("pokefile.pkl", "wb") as pokefile:
            pickle.dump(all_pokemons, pokefile)
        print("¡Archivo creado!")
    print("¡Pokemons cargados!")
    return all_pokemons


def main():
    get_all_pokemons()


if __name__ == "__main__":
    main()
