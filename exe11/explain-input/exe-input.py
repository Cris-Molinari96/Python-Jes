def execute_command():
    name = input("what is your name?! ")
    print(type(name))
    print(f"Hi {name}, your welcome in my program!!")
#execute_command()

# Possiamo concatenare le due funzioni print e input:
# print("Hi " + input("What is your name? ") + " your welcome in my program!")

def brand_name():
    print("The name that think for you is " + input("What is your favorite city? ") + input("What is your favorite animals?"))
#brand_name()

def countNumbers():
    num = input("Insert a number please ")
    print("The number have "+ f"{len(num)}" + " numerics")
# countNumbers()