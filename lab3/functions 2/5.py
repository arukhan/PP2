from dictofmovies import movies
a=[]
movie_category=input()
def func(movie_category):
    for movie in movies:
        if movie_category == movie['category']:
            a.append(movie['imdb'])
    #print(a)
    print(sum(a)/len(a))
func(movie_category)