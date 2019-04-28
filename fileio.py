import random

def write_to_file(content):
    filename = "log.txt"    

    with open(filename,"a") as f:
        f.write("_______________________________________________\n\n")
        f.write(content)
        f.write("\n_______________________________________________\n")

def read_from_file():
        filename = "random.txt"

        with open(filename,"r") as f:
                content = f.read()

                return content