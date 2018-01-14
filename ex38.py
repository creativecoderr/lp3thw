## Doing things to lists


ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')

more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items remaining now.")

print("There we go: ", stuff)

print("Let's do some other things with stuff list")

print("Stuff: ", stuff)
print("Sorted Stuff: ", sorted(stuff))

print(stuff[1])
print(stuff[-1]) # Whoa! Fancy
print(sorted(stuff).pop())

print(' '.join(stuff)) # What? Cool!
print("#".join(stuff)) # Super stellar

a = []
for i in range(1,31):
    a.append(i)

print(a)
print(a[-7:])


