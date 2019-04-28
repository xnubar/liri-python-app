import keys, requests, fileio

def movie_info(movie):
    rotten_tomatoes_rating=str(round(10-float(movie['imdbRating']),2))
    result_str="\nTitle: "+movie['Title']+";"+'Year: '+movie['Year']+";" +'IMDB rating: '+movie['imdbRating']+";"+'Rotten Tomatoes Rating:'+rotten_tomatoes_rating+";"+'Country: '+movie['Country']+";"+'Language: '+movie['Language']+";"+'Plot: '+movie['Plot']+";"+'Actors: '+movie['Actors']
    fileio.write_to_file(result_str.replace(";","\n"))
    print("_______________________________________________")
    for item in result_str.split(";"):
        print(item)
    print("_______________________________________________")
    
    

def search_movie(movie_name):
    default_movie = "Mr. Nobody"

    if not movie_name:
        movie_name = default_movie
    apikey = keys.omdb["apikey"]
    url = keys.omdb["url"]+"/?apikey="+apikey+"&t="+movie_name
    result = requests.get(url).json()

    if result['Response'] == 'True':
        movie_info(result)
    else:
        print(result['Error'])
       

