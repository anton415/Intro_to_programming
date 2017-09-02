import webbrowser

class Video():
    def __init__(self, title, poster_image, trailer_youtube):
        self.title = title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def play_trailer(self):
        webbrowser.open_new(self.trailer_youtube_url)
