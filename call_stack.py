def greet2(name):
    print("How are you, "+name+"?")
def bye():
    print("Ok! Bye")

def greet(name):
    print("Hello ", name, "!")
    greet2(name)
    print("Getting ready to say bye")
    bye()

greet2('Thong')
