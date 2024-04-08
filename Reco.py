from test import games

def get_genres(dict):
    genre_list = []
    for value in dict.values():
        if value[0] not in genre_list:
            genre_list.append(value[0])
    return genre_list


def get_genre_choice():
    print(get_genres(games))
    choice = input("Which genre would you like to play?")
    return choice

def find_game():
    multiplayer = input("Do you want a singleplayer game or a multiplayer game?")
    choice = get_genre_choice()
    for game, genre in games.items():
        if genre[1] == multiplayer:
            if genre[0] == choice:
                return game
        

print(find_game())


    


