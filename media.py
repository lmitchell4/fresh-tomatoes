""" This module contains the following classes for defining media items:
    Media
    Movie(Media)
    TVShow(Media)
"""

import webbrowser

class Media(object):
    """ Provides a template for different media classes.
    
    Attributes:
        title (str): A string containing the title of the media item.
        description (str): A string containing a short description of the 
            media item.
        image_url (str): A string containing the URL for an image 
            representing the item
        trailer_youtube_url (str): A string containing the URL for a video 
            trailer for the item.
    """
    
    def __init__(self, title, description, image_url, trailer_youtube):
        self.title = title
        self.description = description
        self.image_url = image_url
        self.trailer_youtube_url = trailer_youtube
        
    def show_info(self):
        """ Displays the title and description of the media item. """

        print("Title: " + self.title + "\nDescription: " + self.description)


class Movie(Media):
    """ Stores information on a specific movie.
    
    Attributes:
        rating (str): A string containing the parent guidance rating for 
            the movie.
    """    

    def __init__(self, title, description, image_url, trailer_youtube, rating):
        Media.__init__(self, title, description, image_url, trailer_youtube)
        self.rating = rating
    
    def show_info(self):
        """ Displays the rating of the movie."""

        super(Movie, self).show_info()
        print("Rating: " + self.rating)
    
    def show_trailer(self):
        """ Opens the YouTube trailer for the movie. """

        webbrowser.open(self.trailer_youtube_url)


class TVShow(Media):
    """ Stores information on a specific TV show.

    Attributes:
        network (str): A string containing the name of the network on which 
            the show airs.
        num_of_seasons (int): An number giving the number of seasons the show
            was on, or the number of the current season if it is still
            currently on.          
    """     
    
    def __init__(self, title, description, image_url, trailer_youtube,
                 network, num_of_seasons):
        Media.__init__(self, title, description, image_url, trailer_youtube)
        self.network = network
        self.num_of_seasons = num_of_seasons

    def show_info(self):
        """ Displays the network and number of seasons. """

        super(TVShow, self).show_info()
        print("Network: " + self.network + "\nNumber of seasons: " + 
              str(self.num_of_seasons))

    def show_trailer(self):
        """ Opens the YouTube trailer for the tv show. """

        webbrowser.open(self.trailer_youtube_url)              


