import media
import fresh_tomatoes

# following code creates the instances for each film
goodfellas = media.Movie("Goodfellas", # movie title instance variable
    # movie storyline instance variable
    "The story of a mafia made man",
    # movie poster instance variable                     
    "https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",
    # movie trailer instance variable                     
    "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

fight_club = media.Movie("Fight Club",
    "Fight Club is a 1999 American drama film based on the 1996 novel of the same name by Chuck Palahniuk.",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
    "https://www.youtube.com/watch?v=J8FRBYOFu2w")

memento = media.Movie("Memento",
    "Memento is a 2000 American neo-noir psychological thriller film directed by Christopher Nolan.",
    "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",
    "https://www.youtube.com/watch?v=0vS0E9bBSL0")

the_shining = media.Movie("The Shining",
    "The Shining is a 1980 British-American psychological horror film produced and directed by Stanley Kubrick,",
    "https://upload.wikimedia.org/wikipedia/en/2/25/The_Shining_poster.jpg",
    "https://www.youtube.com/watch?v=5Cb3ik6zP2I")

inception = media.Movie("Inception",
    "Inception is a 2010 science fiction heist thriller film written, produced, and directed by Christopher Nolan.",
    "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
    "https://www.youtube.com/watch?v=66TuSJo4dZM")

heat = media.Movie("Heat",
    "Heat is a 1995 American crime film written, produced and directed by Michael Mann, and starring Robert De Niro, Al Pacino, and Val Kilmer.",
    "https://upload.wikimedia.org/wikipedia/en/6/6c/Heatposter.jpg",
    "https://www.youtube.com/watch?v=0xbBLJ1WGwQ")

# setting a variable containing the list of movies
movies = [goodfellas, fight_club, memento, the_shining, inception, heat]

# calling the function that generates the web page
fresh_tomatoes.open_movies_page(movies)
