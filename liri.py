import inquirer
import spotify
import omdb
import sys
import do_what_it_says  as comp_choice
from dotenv import load_dotenv
load_dotenv()


question = [
    inquirer.List('command',
                  message="Enter command",
                  choices=['my-tweets', 'spotify-this-song',
                           'movie-this', 'do-what-it-says'],
                  )
]

answers = inquirer.prompt(question)
command = answers['command']

if answers["command"] != 'do-what-it-says':
    search_text = input("[?] Enter search text: ")
        

if command == 'my-tweets':
    pass
elif command == 'spotify-this-song':
    spotify.search_song(search_text)
elif command == 'movie-this':
    omdb.search_movie(search_text)
elif command == 'do-what-it-says':
    comp_choice.get_result()

# omdb.search_movie("")


# spotify.search_song("")
