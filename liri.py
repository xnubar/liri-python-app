import inquirer
import spotify
import omdb
import sys
import do_what_it_says  as comp_choice
from dotenv import load_dotenv
load_dotenv()

COMMAND_1 = '1: spotify-this-song'
COMMAND_2 = '2: movie-this'
COMMAND_3 = '3: do-what-it-says'
COMMAND_4 = 'Q: Quit'
question = [
    inquirer.List('command',
                  message="Enter command",
                  choices=[COMMAND_1, COMMAND_2,
                           COMMAND_3, COMMAND_4
                  ]
                )
]
while True:
    answers = inquirer.prompt(question)
    command = answers['command']

    if answers["command"] == COMMAND_1 or answers["command"] == COMMAND_2:
        search_text = input("[?] Enter search text: ")


    if command == COMMAND_1:
        spotify.search_song(search_text)
    elif command == COMMAND_2:
        omdb.search_movie(search_text)
    elif command == COMMAND_3:
        comp_choice.get_result()
    elif command == COMMAND_4:
        break


