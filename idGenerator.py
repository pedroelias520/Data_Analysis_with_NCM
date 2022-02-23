from random  import randint

class main():
    def __init__(self):
        print("Hello")
        print(GenerateIds())


def GenerateIds(): 
    group0 = ""
    IdGenerated = ""
    for t in range(3):
        for i in range(4):
            value = randint(0, 9)
            group0 = group0 + str(value)
        if t < 2:
            group0 = group0 + " "
        IdGenerated = group0 
    return IdGenerated
        
main()    