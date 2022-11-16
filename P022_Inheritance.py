#Inheritance in Python
class Music:
    lang = 'English'
    Color = 'Green'

    def __init__(self):
        print("Inheritance in Python")

M1 = Music()

print(M1.lang)

class MusicPlayer:
    Songs = 100;
    def __init__(self):
        print("parent class")

MP1 = MusicPlayer()
print(MP1.Songs)

class Spotify (MusicPlayer,Music):

    def __init__(self):
        print("Child Class- Single Inheritance")


spotify1 = Spotify()
spotify1. quality = 'Good'


print(spotify1.Songs, spotify1.quality)
print(spotify1.lang)
