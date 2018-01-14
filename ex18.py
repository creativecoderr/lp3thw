#   Names, Variables, Codes, Functions

def print_two(*args):
    arg1, arg2, arg3 = args
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")
    
def print_always():
    print("After all this time? Always!")


print_two("Jinal", "Ratul", "Ramchandani")
print_two_again("Jinal","Ratul")
print_one("Together forever")
print_always()

