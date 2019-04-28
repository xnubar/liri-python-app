def write_to_file(content):
    filename = "log.txt"    

    with open(filename,"a") as f:
        f.write("_______________________________________________\n\n")
        f.write(content)
        f.write("\n_______________________________________________\n")

