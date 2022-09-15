import requests
import json


# Function that gets an API response.
# Arg: str url of endpoint
# Returns: API response
def get_json_response(url):
    response = requests.get(url)

    return response


# Function that prints the names of all Pokémon from a JSON object and stores the name and
#   endpoint url of each Pokémon within a dictionary.
# Arg: A JSON object from a Pokémon type endpoint
# Returns: A dictionary with key/value pairs being the name/url.
def get_all_pokemon(json_obj):
    my_map = {}

    for pokemon in json_obj['pokemon']:
        name = pokemon['pokemon']['name']
        url = pokemon['pokemon']['url']
        print(name)
        my_map[name] = url

    return my_map


# Function that prints out information regarding a Pokémon from a JSON object.
# Arg: A JSON object from a Pokémon name endpoint
def output_pokemon_info(json_obj):
    print('\nInformation regarding \'{}\':'.format(json_obj['name']))

    print('\nHeight: {}'.format(json_obj['height']))

    print('\nWeight: {}'.format(json_obj['weight']))

    print('\nSpecies: {}'.format(json_obj['species']['name']))

    print('\nGames: ', end='')
    for game in json_obj['game_indices']:
        print(game['version']['name'], end=', ')

    print('\n\nTypes: ', end='')
    for poke_type in json_obj['types']:
        print(poke_type['type']['name'], end=', ')

    # Print no more than 10 moves
    limit = 10 if len(json_obj['moves']) >= 10 else len(json_obj['moves'])
    print('\n\n{} Moves: '.format(limit), end='')
    for i in range(0, limit):
        print(json_obj['moves'][i]['move']['name'], end=', ')

    print('\n')


POKEMON_TYPES = {'normal', 'fire', 'water', 'grass', 'electric', 'ice', 'fighting', 'poison',
                 'ground', 'flying', 'psychic', 'bug', 'rock', 'ghost', 'dark', 'dragon', 'steel', 'fairy'}

print('Welcome to my OIT Coding Challenge!\n')

# Get Pokémon type from user
userInputType = input('Enter a Pokémon type: ')

if userInputType in POKEMON_TYPES:
    # Get response from pokemon type endpoint
    responseForType = get_json_response('https://pokeapi.co/api/v2/type/{}/'.format(userInputType))

    if responseForType.status_code == 200:
        # Get dictionary with name and url pairs from responseForType
        name_url = get_all_pokemon(json.loads(responseForType.text))

        # Get Pokémon name from user
        userInputName = input('\nEnter a Pokémon name from above: ')

        # Verify that userInputName is a key in nameAndURL
        if userInputName in name_url:
            # Get response from pokemon name endpoint
            responseForName = get_json_response(name_url[userInputName])

            if responseForName.status_code == 200:
                # Print Pokémon information
                output_pokemon_info(json.loads(responseForName.text))
