import fileio
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2
import keys


def search_song(search_text):
    default_song = "The Sign"

    market = ["AD", "AR", "AT", "AU", "BE", "BG", "BO", "BR", "CA", "CH", "CL", "CO", "CR", "CY",
              "CZ", "DE", "DK", "DO", "EC", "EE", "ES", "FI", "FR", "GB", "GR", "GT", "HK", "HN", "HU",
              "ID", "IE", "IS", "IT", "JP", "LI", "LT", "LU", "LV", "MC", "MT", "MX", "MY", "NI", "NL",
              "NO", "NZ", "PA", "PE", "PH", "PL", "PT", "PY", "SE", "SG", "SK", "SV", "TH", "TR", "TW",
              "US", "UY", "VN"]

    credentials = oauth2.SpotifyClientCredentials(
        client_id=keys.spotify["id"],
        client_secret=keys.spotify["secret"])

    token = credentials.get_access_token()
    s = spotipy.Spotify(auth=token)


    track = search_text and search_text or default_song
    res = s.search(track, type="track", market=market, limit=1)
    song_info(res)


def song_info(song):
    tracks = song["tracks"]
    items = tracks["items"]

    if items:
        for item in items:
            artist = item["artists"][0]['name'] and item["artists"][0]['name'] or 'None'
            album = item["album"]["name"] and item["album"]["name"] or "None"
            song_name = item["name"]
            preview_link = item["preview_url"] and item["preview_url"] or "None"

            result_str = "Artist: " + artist + ";" "Name of song: "+song_name + ";" + "Preview link: " + preview_link + ";" + "Album name: " + album
            
            print("_______________________________________________\n")
            for item in result_str.split(";"):
                 print(item)
            print("_______________________________________________")
        fileio.write_to_file(result_str.replace(";","\n"))
