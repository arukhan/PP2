from dictofmovies import movies

def func(movie_name):
    for movie in movies:
        if movie_name == movie['name'] and movie['imdb'] > 5.5:
            return True
    return False

print(func(input()))