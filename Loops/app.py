

def func1():
    characters="Python"
    for character in characters:
        print(character)
    

def func2():
    characters="Java"
    for x in characters:
        print(x)
    print(func1())        
func2()
    