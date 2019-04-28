import fileio
import spotify


def get_result():
    result = fileio.read_from_file()
    spotify.search_song(result)