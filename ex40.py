# Modules, Classes and Objects

class MyStuff(object):
    
    def __init__(self):
        print(self)
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print(self)
        print("I am classy Apples!")



item = MyStuff()
item.apple()
#item.apple("hello_apple")
print(item.tangerine)

''' # --------------------------------------------------------------------------------
print("\n Songs Class \n")



class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday_song = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])
bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"])
black_or_white  = Song(["It does't matter", "If it's black or white"])

happy_bday_song.sing_me_a_song()
print("\n")
bulls_on_parade.sing_me_a_song()
print("\n")
black_or_white.sing_me_a_song() '''