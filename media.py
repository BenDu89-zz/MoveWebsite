# hier wird ein class enstehen um wakebaord filme anzuzeigen
import webbrowser

class Movies():
    ''' This class with be creating the ins. for your movie page'''

    VALID_RATINGS = ["G","PG","PG-13","R"]

    def __init__(self, title, storyline, trailer_youtube_url, poster_image_url): # ist der creater
        self.title = title
        self.storyline = storyline
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url

    def show_movie(self):
        webbrowser.open(self.trailer_url)
