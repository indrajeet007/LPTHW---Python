class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# happy_bday = Song(["Happy birthday to you!", "I don't want to get sued", "So I'll stop right there!"])
# bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"])

# putting above lyrics in different variables
happy_bday_lyrics = ["Happy birthday to you!", "I don't want to get sued", "So I'll stop right there!"]
bulls_on_parade_lyrics = ["They rally around the family", "With pockets full of shells"]

# using above variables in the class itself
happy_bday = Song(happy_bday_lyrics)
bulls_on_parade = Song(bulls_on_parade_lyrics)

# calling class function
happy_bday.sing_me_a_song()
print("\n")
bulls_on_parade.sing_me_a_song()
