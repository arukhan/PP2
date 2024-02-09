import itertools
string=input()
def permutations(string):
    output = itertools.permutations(string, len(string))
    for p in output:
        print("".join(p))
permutations(string)