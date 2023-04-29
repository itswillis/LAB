def create_artist_dictionary(movies_list):
    artist_dictionary = {}
    for data in movies_list:
        artist = data[1]
        movie_name = data[0]
        if artist not in artist_dictionary:
            artist_dictionary[artist]= [movie_name]
        else:
            artist_dictionary[artist].append(movie_name)

    for value in artist_dictionary.keys():
        artist_dictionary[value].sort()
    return artist_dictionary

data = [('Avengers: Endgame', 'Robert Downey, Jr'), ('Avengers: Endgame', 'Scarlett Johansson'), ('Avengers: Endgame', 'Chris Hemsworth'), ('Avatar: The Way of Water', 'Zoe Saldana'), ('Avatar: The Way of Water', 'Sam Worthington'), ('Top Gun: Maverick', 'Tom Cruise'), ('Top Gun: Maverick', 'Miles Teller'),  ('Fantastic Four', 'Miles Teller'), ('Fantastic Four', 'Kate Mara')]
a_dict = create_artist_dictionary(data)
for key in sorted(a_dict.keys()):
    print(key, a_dict[key])