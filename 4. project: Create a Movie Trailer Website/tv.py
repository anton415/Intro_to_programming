import webbrowser
import video

class Tv(video.Video):
    def __init__(self, tv_title, tv_seasons, poster_image, trailer_youtube):
        self.title = tv_title
        self.seasons = tv_seasons
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def play_trailer(self):
        webbrowser.open_new(self.trailer_youtube_url)
