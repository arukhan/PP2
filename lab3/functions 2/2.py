from dictofmovies import movies
a=[]
def func(movies):
    for i in movies:
        if i['imdb'] > 5.5:
            a.append(i['name'])
    print(a)

func(movies)