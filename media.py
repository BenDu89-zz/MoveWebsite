import webbrowser # To open urls in a webbrowser in the def show_movie

class Movies():
    ''' The class movie contains the basic data of the movie, as title, storyline, trailer url and poster image url'''

    VALID_RATINGS = ["G","PG","PG-13","R"] # diffrent posible rankings for the movies

    def __init__(self, title, storyline, trailer_youtube_url, poster_image_url): # init ist the creater and will reserve storage for the object
        self.title = title # title of the movie 
        self.storyline = storyline # storyline of the movie
        self.trailer_youtube_url = trailer_youtube_url # the youtube url for the tailer of the movie
        self.poster_image_url = poster_image_url # url of the poster image of the movie

    def show_movie(self):
        ''' This def will take as an input the name of the movie and than play the trailer of the movie, by opening a webbrowser'''
        webbrowser.open(self.trailer_url)
