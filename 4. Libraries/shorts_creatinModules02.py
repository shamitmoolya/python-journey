# a package is a collection of many modules 

# import museum

from museum.artists import get_artists
from museum.artwork import get_artworks

def main():
    artwork = input("Artwork: ")
    artworks = get_artworks(query=artwork, limit=3)

    for artwork in artworks:
        print(f"* {artwork}")


    artist = input("Artist: ")
    artists = get_artists(query=artist, limit=3)

    for artist in artists:
        print(f"* {artist}")


main()