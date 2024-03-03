def all_elements_true(t):
    return all(t)

def main():
    t = (True, True, True, True) 
    if all_elements_true(t):
        print("All elements of the tuple are True.")
    else:
        print("Not all elements of the tuple are True.")

if __name__ == "__main__":
    main()
