from dictofmovies import movies
a=["Dark Knight", "Exam", "What is the name", "Joking muck", "AlphaJet"]
b=[]
def func(a):
    for movie in movies:
        for i in a:
            if i == movie['name']:
                b.append(movie['imdb'])
    #print(b)
    print(sum(b)/len(b))
func(a)