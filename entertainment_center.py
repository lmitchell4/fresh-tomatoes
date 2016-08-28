""" This script generates code to create and open the Fresh Tomatoes
    Video Trailers website, which contains links to video trailers
    for movies and tv shows.

    Example of how to run the script:

        $ python entertainment_center.py

"""

import media
import fresh_tomatoes

## Movie Entries
toy_story = media.Movie(
    "Toy Story", "A story of a boy and his toys that come to life.",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc", "G")

avatar = media.Movie(
    "Avatar", "A marine on an alien planet.",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "www.youtube.com/watch?v=8KAtG68bIUc", "PG-13")

school_of_rock = media.Movie(
    "School of Rock", "Using rock music to learn",
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc", "PG-13")


## TV Show Entries
breaking_bad = media.TVShow(
    "Breaking Bad", "High school chemistry teacher makes drugs.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/6/61/Breaking_Bad_title_card.png/375px-Breaking_Bad_title_card.png", # NOQA
    "https://www.youtube.com/watch?v=HhesaQXLuRY", "AMC", 5)

walking_dead = media.TVShow(
    "The Walking Dead", "A post-apocalyptic world filled with zombies.",
    "https://upload.wikimedia.org/wikipedia/en/1/17/The_Walking_Dead_title_card.jpg", # NOQA
    "https://www.youtube.com/watch?v=SmUz88zoIg0", "AMC", 6)


movies = [toy_story, avatar, school_of_rock]
tv_shows = [breaking_bad, walking_dead]
fresh_tomatoes.open_entries_page(movies, tv_shows)
