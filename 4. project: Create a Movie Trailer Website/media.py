import webbrowser

class Movie():
    '''
    Movie class.
    '''
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        '''
        Init method.
        :param movie_title: title.
        :param movie_storyline: storyline.
        :param poster_image: poster.
        :param trailer_youtube: trailer.
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def play_trailer(self):
        '''
        Method for play trailer.
        :return:
        '''
        webbrowser.open_new(self.trailer_youtube_url)
