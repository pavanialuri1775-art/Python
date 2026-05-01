#The __str__() Method
#The __str__() method is a special method that controls what is returned when the object is printed.
#without _str_ ()
class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Emil", 36)
print(p1)

#
class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age
      def __str__(self):
        return f"{self.name} ({self.age})"
p1 = Person("Tobias",36)
print(p1)

#a class can have multiple methods that work together
class Playlist:
    def __init__(self,name):
        self.name=name
        self.songs=[]
    def add_song(self,song):
        self.songs.append(song)
        print(f'Added:{song}')
    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed:{song}")
    def show_songs(self,song):
        print(f"Playlist'{self.name}':")
        for song in self.songs:
            print(song)
my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs("Stairway to Heaven")