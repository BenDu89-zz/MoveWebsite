import media
''' media is holding the class that we a going to use, to creat diffrent Film objects '''
import fresh_tomatoes
''' fresh_tomatoes will take all your objects and turn them into a good looking website '''

# below the diffrent objects that
DieVerurteilten = media.Movies("Die Verurteilten", "Unschuldig im Knast",
                                "https://www.youtube.com/watch?v=Uxgv5udgjjY",
                                "https://images-na.ssl-images-amazon.com/images/I/517SDGYY26L.jpg")

HerrDerRinge = media.Movies("Der Herr der Ringe - Die Rueckkehr des Koenigs", "Kleine Hobbits",
                                "https://www.youtube.com/watch?v=PMQaJpQXmDc",
                                "https://assets.cdn.moviepilot.de/files/a6de299b4f227399a0700d76d69a66bc42bdc33aca836ee2b5de3c122ed6/Der_Herr_der_Ringe_-_Die_Gef_hrten.jpg")

StarWars = media.Movies("Das Imperium schlaegt zurueck", "Krieg",
                                "https://www.youtube.com/watch?v=qOV61eL9XDE",
                                "http://vignette3.wikia.nocookie.net/jedipedia/images/d/d4/Episode_5_%28Roman%29.jpg/revision/latest?cb=20080801211647&path-prefix=de")

movielist = [DieVerurteilten, HerrDerRinge, StarWars]
# All objects in one list
fresh_tomatoes.open_movies_page(movielist)
# creating the movie page with the list of objects as an input

print (media.Movies.VALID_RATINGS)
doc = media.Movies.__module__ # look at the provided doc from media
print doc
